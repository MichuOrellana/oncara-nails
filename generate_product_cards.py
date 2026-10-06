import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

img_dir = r"C:\Users\Mishu\.gemini\antigravity\scratch\oncara-nails\assets\images"

def create_luxury_product_card(crop_path, output_name, title_text, dark_mode=False):
    # Base canvas 600x600
    w, h = 600, 600
    
    # Background color
    if not dark_mode:
        bg_col = (247, 244, 238)
        border_col = (194, 160, 107, 180)
        inner_bg = (252, 250, 246)
        shadow_col = (0, 0, 0, 45)
    else:
        bg_col = (20, 20, 16)
        border_col = (194, 160, 107, 200)
        inner_bg = (26, 26, 20)
        shadow_col = (0, 0, 0, 120)

    canvas = Image.new('RGB', (w, h), bg_col)
    draw = ImageDraw.Draw(canvas)

    # Subtle radial gradient / vignette
    for r in range(0, 300, 10):
        alpha = int((r / 300) * 15)
        fill = (235, 230, 220) if not dark_mode else (14, 14, 10)
        draw.ellipse([r, r, w - r, h - r], outline=fill, width=5)

    # Inner card frame
    card_margin = 35
    card_rect = [card_margin, card_margin, w - card_margin, h - card_margin]
    
    # Draw soft shadow behind inner card
    shadow_img = Image.new('RGBA', (w, h), (0,0,0,0))
    s_draw = ImageDraw.Draw(shadow_img)
    s_draw.rectangle([card_margin + 5, card_margin + 8, w - card_margin + 5, h - card_margin + 8], fill=(0, 0, 0, 35))
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=8))
    canvas.paste(shadow_img, (0, 0), shadow_img)

    # Draw inner card surface
    draw.rectangle(card_rect, fill=inner_bg)

    # Double delicate gold border
    draw.rectangle(card_rect, outline=(194, 160, 107), width=1)
    inner_inset = 8
    draw.rectangle([card_rect[0] + inner_inset, card_rect[1] + inner_inset, 
                   card_rect[2] - inner_inset, card_rect[3] - inner_inset], 
                   outline=(194, 160, 107), width=1)

    # Load and upscale nail set
    if os.path.exists(crop_path):
        nail_im = Image.open(crop_path)
        nw, nh = nail_im.size
        
        # Target size for nails on the card: ~320px wide
        scale = 320.0 / nw
        target_w = int(nw * scale)
        target_h = int(nh * scale)
        
        nail_upscaled = nail_im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        nail_upscaled = nail_upscaled.filter(ImageFilter.UnsharpMask(radius=1.8, percent=140, threshold=2))
        
        # Position centered
        pos_x = (w - target_w) // 2
        pos_y = ((h - target_h) // 2) - 15

        # Drop shadow for nails
        nail_shadow = Image.new('RGBA', (w, h), (0,0,0,0))
        ns_draw = ImageDraw.Draw(nail_shadow)
        ns_draw.ellipse([pos_x + 15, pos_y + target_h - 10, pos_x + target_w - 15, pos_y + target_h + 20], fill=(0, 0, 0, 45))
        nail_shadow = nail_shadow.filter(ImageFilter.GaussianBlur(radius=12))
        canvas.paste(nail_shadow, (0, 0), nail_shadow)

        # Paste nail set
        canvas.paste(nail_upscaled, (pos_x, pos_y))

    # Corner stars
    star_col = (194, 160, 107)
    for cx, cy in [(card_margin + 18, card_margin + 18), 
                   (w - card_margin - 18, card_margin + 18),
                   (card_margin + 18, h - card_margin - 18), 
                   (w - card_margin - 18, h - card_margin - 18)]:
        draw.line([cx - 4, cy, cx + 4, cy], fill=star_col, width=1)
        draw.line([cx, cy - 4, cx, cy + 4], fill=star_col, width=1)

    out_path = os.path.join(img_dir, output_name)
    canvas.save(out_path, quality=95)
    print(f"Generated luxury card: {output_name} (600x600)")

# Generate the 4 main sets
create_luxury_product_card(os.path.join(img_dir, 'test_nail1.jpg'), 'card_prod_salvaje.jpg', 'SALVAJE')
create_luxury_product_card(os.path.join(img_dir, 'test_nail2.jpg'), 'card_prod_oraculo.jpg', 'ORACULO')
create_luxury_product_card(os.path.join(img_dir, 'test_nail3.jpg'), 'card_prod_ocaso.jpg', 'OCASO')
create_luxury_product_card(os.path.join(img_dir, 'test_nail4.jpg'), 'card_prod_hechizo.jpg', 'HECHIZO')

# Create Selva Negra and Alquimia with high-res crops
# Selva Negra: crop from im403 packaging or im417 box
im417 = Image.open(r'C:\Users\Mishu\.gemini\antigravity\brain\91d930c9-4fa0-4a39-81bf-25ecdd5446cf\.user_uploaded\media_1790832886417.jpg')
# Crop box nails from 417
selva_crop = im417.crop((485, 435, 595, 545))
selva_crop.save(os.path.join(img_dir, 'test_selva_nails.jpg'))
create_luxury_product_card(os.path.join(img_dir, 'test_selva_nails.jpg'), 'card_prod_selva_negra.jpg', 'SELVA NEGRA')

# Alquimia: crop from im403 or im417
alquimia_crop = im417.crop((840, 25, 960, 155))
alquimia_crop.save(os.path.join(img_dir, 'test_alquimia_nails.jpg'))
create_luxury_product_card(os.path.join(img_dir, 'test_alquimia_nails.jpg'), 'card_prod_alquimia.jpg', 'ALQUIMIA')

print("All 6 luxury product cards created successfully!")
