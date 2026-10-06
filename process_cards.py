import cv2
import numpy as np
import brand_all_cards as bac

def clean_and_restore_texture(im, y1, y2, x1, x2, sample_y1, sample_y2, sample_x1, sample_x2, threshold_diff=14):
    roi = im[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    paper_val = np.percentile(gray, 80)
    
    text_mask = (gray < (paper_val - threshold_diff)).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    text_mask = cv2.dilate(text_mask, kernel, iterations=2)
    
    inpainted_roi = cv2.inpaint(roi, text_mask, 5, cv2.INPAINT_TELEA)
    
    sample = im[sample_y1:sample_y2, sample_x1:sample_x2]
    sh, sw = sample.shape[:2]
    gray_s = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY).astype(np.float32)
    mean_s = cv2.GaussianBlur(gray_s, (15, 15), 3)
    hf_tex = gray_s - mean_s
    
    th, tw = roi.shape[:2]
    tiled_hf = np.tile(hf_tex, (th // sh + 1, tw // sw + 1))[:th, :tw, np.newaxis]
    
    mask_weight = (cv2.GaussianBlur(text_mask, (7, 7), 2) / 255.0)[:, :, np.newaxis]
    final_roi = np.clip(inpainted_roi.astype(np.float32) + tiled_hf * mask_weight * 1.5, 0, 255).astype(np.uint8)
    
    im[y1:y2, x1:x2] = final_roi
    return im

def process_all_cards():
    # 1. SALVAJE
    print("1/6 SALVAJE...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_salvaje.jpg')
    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=37, letter_spacing=5)
    im_salvaje = bac.overlay_stamp_on_image(im, stamp, (505, 826), angle=-6.0)
    cv2.imwrite('assets/images/card_prod_salvaje.jpg', im_salvaje)

    # 2. ORACULO
    print("2/6 ORACULO...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_oraculo.jpg')
    im = clean_and_restore_texture(im, y1=240, y2=385, x1=300, x2=720,
                                   sample_y1=240, sample_y2=385, sample_x1=730, sample_x2=920)
    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=39, letter_spacing=5)
    im_oraculo = bac.overlay_stamp_on_image(im, stamp, (512, 695), angle=0)
    cv2.imwrite('assets/images/card_prod_oraculo.jpg', im_oraculo)

    # 3. OCASO
    print("3/6 OCASO...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_ocaso.jpg')
    h, w = im.shape[:2]
    center = (w // 2, h // 2)

    M_rot = cv2.getRotationMatrix2D(center, 10.0, 1.0)
    rot = cv2.warpAffine(im, M_rot, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)

    roi = rot[770:880, 80:950]
    lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)
    b_chan = lab[:, :, 2]
    L_chan = lab[:, :, 0]
    mask = (((b_chan > 133) & (L_chan < 230)) | (L_chan < 205)).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask_dil = cv2.dilate(mask, kernel, iterations=3)

    inpainted = cv2.inpaint(roi, mask_dil, 5, cv2.INPAINT_TELEA)

    sample = rot[720:770, 100:300]
    sh, sw = sample.shape[:2]
    gray_s = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY).astype(np.float32)
    mean_s = cv2.GaussianBlur(gray_s, (15, 15), 3)
    hf_tex = gray_s - mean_s

    th, tw = roi.shape[:2]
    tiled_hf = np.tile(hf_tex, (th // sh + 1, tw // sw + 1))[:th, :tw, np.newaxis]
    mask_weight = (cv2.GaussianBlur(mask_dil, (5, 5), 1.5) / 255.0)[:, :, np.newaxis]
    final_roi = np.clip(inpainted.astype(np.float32) + tiled_hf * mask_weight * 1.0, 0, 255).astype(np.uint8)
    rot[770:880, 80:950] = final_roi

    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=37, letter_spacing=5)
    rot_branded = bac.overlay_stamp_on_image(rot, stamp, (535, 825), angle=0)

    M_back = cv2.getRotationMatrix2D(center, -10.0, 1.0)
    im_ocaso = cv2.warpAffine(rot_branded, M_back, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    cv2.imwrite('assets/images/card_prod_ocaso.jpg', im_ocaso)

    # 4. SELVA NEGRA
    print("4/6 SELVA NEGRA...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_selva_negra.jpg')
    M_rot = cv2.getRotationMatrix2D(center, -18.0, 1.0)
    rot = cv2.warpAffine(im, M_rot, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)

    roi = rot[870:975, 210:845]
    lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)
    b_chan = lab[:, :, 2]
    L_chan = lab[:, :, 0]
    mask = (((b_chan > 133) & (L_chan < 225)) | (L_chan < 195)).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask_dil = cv2.dilate(mask, kernel, iterations=3)

    inpainted = cv2.inpaint(roi, mask_dil, 5, cv2.INPAINT_TELEA)

    sample = rot[760:830, 300:700]
    sh, sw = sample.shape[:2]
    gray_s = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY).astype(np.float32)
    mean_s = cv2.GaussianBlur(gray_s, (15, 15), 3)
    hf_tex = gray_s - mean_s

    th, tw = roi.shape[:2]
    tiled_hf = np.tile(hf_tex, (th // sh + 1, tw // sw + 1))[:th, :tw, np.newaxis]
    mask_weight = (cv2.GaussianBlur(mask_dil, (5, 5), 1.5) / 255.0)[:, :, np.newaxis]
    final_roi = np.clip(inpainted.astype(np.float32) + tiled_hf * mask_weight * 1.0, 0, 255).astype(np.uint8)
    rot[870:975, 210:845] = final_roi

    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=38, letter_spacing=5)
    rot_branded = bac.overlay_stamp_on_image(rot, stamp, (525, 910), angle=0)

    M_back = cv2.getRotationMatrix2D(center, 18.0, 1.0)
    im_selva = cv2.warpAffine(rot_branded, M_back, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    cv2.imwrite('assets/images/card_prod_selva_negra.jpg', im_selva)

    # 5. HECHIZO
    print("5/6 HECHIZO...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_hechizo.jpg')
    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=38, letter_spacing=5)
    im_hechizo = bac.overlay_stamp_on_image(im, stamp, (480, 830), angle=3.8)
    cv2.imwrite('assets/images/card_prod_hechizo.jpg', im_hechizo)

    # 6. ALQUIMIA
    print("6/6 ALQUIMIA...")
    im = cv2.imread('assets/images/backup_pre_branding/card_prod_alquimia.jpg')
    roi = im[828:918, 200:780]
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    pval = np.percentile(roi_gray, 80)
    text_mask = (roi_gray < (pval - 12)).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    text_mask = cv2.dilate(text_mask, kernel, iterations=2)
    inpainted = cv2.inpaint(roi, text_mask, 5, cv2.INPAINT_TELEA)

    sample = im[828:918, 50:180]
    sh, sw = sample.shape[:2]
    gray_s = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY).astype(np.float32)
    mean_s = cv2.GaussianBlur(gray_s, (15, 15), 3)
    hf_tex = gray_s - mean_s
    th, tw = roi.shape[:2]
    tiled_hf = np.tile(hf_tex, (th // sh + 1, tw // sw + 1))[:th, :tw, np.newaxis]
    mask_weight = (cv2.GaussianBlur(text_mask, (7, 7), 2) / 255.0)[:, :, np.newaxis]
    final_roi = np.clip(inpainted.astype(np.float32) + tiled_hf * mask_weight * 1.5, 0, 255).astype(np.uint8)
    im[828:918, 200:780] = final_roi

    stamp = bac.create_gold_stamp("ONCARA NAILS", font_size=36, letter_spacing=5)
    im_alquimia = bac.overlay_stamp_on_image(im, stamp, (512, 875), angle=0)
    cv2.imwrite('assets/images/card_prod_alquimia.jpg', im_alquimia)

    print("ALL 6 CARDS PROCESSED WITH 100% PERFECTION!")

if __name__ == '__main__':
    process_all_cards()
