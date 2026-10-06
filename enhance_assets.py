import os
from PIL import Image, ImageEnhance, ImageFilter

p = r"C:\Users\Mishu\.gemini\antigravity\scratch\oncara-nails\assets\images"

# List of images to upscale 2x with lanczos
targets = [
    'hero_hand_home.jpg', 'box_pack_home.jpg', 'candle_moss_home.jpg', 'mirror_hand_home.jpg',
    'sobre_hero_hand.jpg', 'leopard_head_profile.jpg', 'leopard_jewelry.jpg',
    'card_rings_bottom.jpg', 'card_mirror_bottom.jpg',
    'personalizados_hero_hand.jpg', 'personalizados_box_still.jpg', 'candle_vase.jpg',
    'contacto_hand_mirror.jpg', 'contacto_box_left.jpg', 'cuidados_hand_candle.jpg',
    'set_salvaje.jpg', 'set_oraculo.jpg', 'set_ocaso.jpg', 'set_hechizo.jpg',
    'test_collections.jpg'
]

for name in targets:
    fpath = os.path.join(p, name)
    if os.path.exists(fpath):
        im = Image.open(fpath)
        w, h = im.size
        # upscale 2.5x
        nw, nh = int(w * 2.5), int(h * 2.5)
        im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
        # slight unsharp mask
        im_enhanced = im_resized.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
        im_enhanced.save(fpath, quality=95)

print("Images upscaled and enhanced successfully!")
