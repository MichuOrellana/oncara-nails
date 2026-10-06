import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os

font_path = 'assets/fonts/Cinzel.ttf'

def create_gold_stamp(text, font_size=42, letter_spacing=5):
    font = ImageFont.truetype(font_path, font_size)
    
    dummy = Image.new('RGBA', (10, 10))
    d_draw = ImageDraw.Draw(dummy)
    
    total_w = 0
    max_h = 0
    for ch in text:
        bbox = d_draw.textbbox((0, 0), ch, font=font)
        cw = bbox[2] - bbox[0]
        ch_h = bbox[3] - bbox[1]
        total_w += cw + letter_spacing
        max_h = max(max_h, ch_h)
    total_w -= letter_spacing
    
    pad = 20
    text_canvas = Image.new('RGBA', (total_w + pad*2, max_h + pad*2), (0,0,0,0))
    t_draw = ImageDraw.Draw(text_canvas)
    
    cur_x = pad
    for ch in text:
        t_draw.text((cur_x, pad), ch, fill=(255, 255, 255, 255), font=font)
        bbox = d_draw.textbbox((0, 0), ch, font=font)
        cur_x += (bbox[2] - bbox[0]) + letter_spacing

    mask = np.array(text_canvas)[:, :, 3]
    gh, gw = mask.shape
    
    # Gold gradient
    gold_tex = np.zeros((gh, gw, 3), dtype=np.float32)
    for y in range(gh):
        for x in range(gw):
            t = (x / gw * 0.35 + y / gh * 0.65)
            # Rich luxury gold foil: (218, 192, 138) to (162, 132, 82)
            r = 218 * (1 - t) + 162 * t
            g = 192 * (1 - t) + 132 * t
            b = 138 * (1 - t) + 82 * t
            gold_tex[y, x] = [r, g, b]
            
    # Subtle metallic micro-noise
    noise = np.random.normal(0, 3.0, (gh, gw, 1))
    gold_tex = np.clip(gold_tex + noise, 0, 255).astype(np.uint8)
    
    # Emboss shading
    grad_x = cv2.Sobel(mask.astype(np.float32), cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(mask.astype(np.float32), cv2.CV_32F, 0, 1, ksize=3)
    
    light_dir = np.array([-0.6, -0.8])
    light_dir /= np.linalg.norm(light_dir)
    
    shading = -(grad_x * light_dir[0] + grad_y * light_dir[1]) / 255.0
    shading = np.clip(shading, -1, 1)
    
    gold_shaded = gold_tex.astype(np.float32)
    gold_shaded += np.maximum(shading, 0)[:, :, np.newaxis] * 40
    gold_shaded += np.minimum(shading, 0)[:, :, np.newaxis] * 45
    gold_shaded = np.clip(gold_shaded, 0, 255).astype(np.uint8)
    
    final_rgba = np.zeros((gh, gw, 4), dtype=np.uint8)
    final_rgba[:, :, :3] = gold_shaded
    final_rgba[:, :, 3] = mask
    
    return Image.fromarray(final_rgba, 'RGBA')

def overlay_stamp_on_image(im_bgr, stamp_rgba, center_pos, angle=0):
    if angle != 0:
        stamp_rot = stamp_rgba.rotate(angle, resample=Image.BICUBIC, expand=True)
    else:
        stamp_rot = stamp_rgba
        
    sw, sh = stamp_rot.size
    x1 = int(center_pos[0] - sw // 2)
    y1 = int(center_pos[1] - sh // 2)
    
    im_pil = Image.fromarray(cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)).convert('RGBA')
    
    # Soft letterpress deboss shadow
    shadow = Image.new('RGBA', stamp_rot.size, (0, 0, 0, 0))
    s_arr = np.array(stamp_rot)[:, :, 3]
    s_blur = cv2.GaussianBlur(s_arr, (5, 5), 1.2)
    shadow_np = np.zeros((sh, sw, 4), dtype=np.uint8)
    shadow_np[:, :, 0] = 70
    shadow_np[:, :, 1] = 55
    shadow_np[:, :, 2] = 35
    shadow_np[:, :, 3] = (s_blur * 0.28).astype(np.uint8)
    shadow_img = Image.fromarray(shadow_np, 'RGBA')
    
    im_pil.paste(shadow_img, (x1 + 1, y1 + 1), shadow_img)
    im_pil.paste(stamp_rot, (x1, y1), stamp_rot)
    
    return cv2.cvtColor(np.array(im_pil.convert('RGB')), cv2.COLOR_RGB2BGR)
