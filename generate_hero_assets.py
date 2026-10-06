import os
from PIL import Image, ImageFilter, ImageEnhance

img_dir = r"C:\Users\Mishu\.gemini\antigravity\scratch\oncara-nails\assets\images"
brain_dir = r"C:\Users\Mishu\.gemini\antigravity\brain\91d930c9-4fa0-4a39-81bf-25ecdd5446cf\.user_uploaded"

# 1. Home Hero Hand:
im417 = Image.open(os.path.join(brain_dir, "media_1790832886417.jpg"))
# x=325 to 676, y=50 to 350
crop_hero = im417.crop((328, 52, 676, 350))
# upscale 2.2x
w, h = crop_hero.size
hero_perfect = crop_hero.resize((int(w * 2.2), int(h * 2.2)), Image.Resampling.LANCZOS)
hero_perfect = hero_perfect.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))
hero_perfect.save(os.path.join(img_dir, "hero_hand_perfect.jpg"), quality=95)
print("Saved hero_hand_perfect.jpg:", hero_perfect.size)

# 2. Personalizados Hero Hand:
im403 = Image.open(os.path.join(brain_dir, "media_1790832886403.jpg"))
# In 403, hand is on right: x=365 to 682, y=52 to 308
crop_pers = im403.crop((360, 52, 682, 308))
pw, ph = crop_pers.size
pers_perfect = crop_pers.resize((int(pw * 2.2), int(ph * 2.2)), Image.Resampling.LANCZOS)
pers_perfect = pers_perfect.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))
pers_perfect.save(os.path.join(img_dir, "personalizados_hand_perfect.jpg"), quality=95)
print("Saved personalizados_hand_perfect.jpg:", pers_perfect.size)

# 3. Sobre Oncara Hero Master Banner:
# In 399, the hero banner is x=0 to 700, y=55 to 335
im399 = Image.open(os.path.join(brain_dir, "media_1790832886399.jpg"))
crop_sobre = im399.crop((0, 55, 700, 335))
sw, sh = crop_sobre.size
sobre_perfect = crop_sobre.resize((int(sw * 2), int(sh * 2)), Image.Resampling.LANCZOS)
sobre_perfect.save(os.path.join(img_dir, "sobre_hero_master.jpg"), quality=95)
print("Saved sobre_hero_master.jpg:", sobre_perfect.size)

# 4. Diseños que cuentan tu historia - Mirror Hand:
# In 417, top right mirror is x=830 to 1024, y=0 to 175
crop_mirror = im417.crop((830, 0, 1024, 175))
mw, mh = crop_mirror.size
mirror_perfect = crop_mirror.resize((int(mw * 2.5), int(mh * 2.5)), Image.Resampling.LANCZOS)
mirror_perfect = mirror_perfect.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))
mirror_perfect.save(os.path.join(img_dir, "mirror_hand_perfect.jpg"), quality=95)
print("Saved mirror_hand_perfect.jpg:", mirror_perfect.size)

# 5. Leopard Jewelry:
# In 399, bottom right leopard is x=700 to 1024, y=520 to 682
crop_leopard = im399.crop((700, 520, 1024, 682))
lw, lh = crop_leopard.size
leopard_perfect = crop_leopard.resize((int(lw * 2.2), int(lh * 2.2)), Image.Resampling.LANCZOS)
leopard_perfect = leopard_perfect.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=2))
leopard_perfect.save(os.path.join(img_dir, "leopard_jewelry_perfect.jpg"), quality=95)
print("Saved leopard_jewelry_perfect.jpg:", leopard_perfect.size)

print("All hero and master assets created successfully!")
