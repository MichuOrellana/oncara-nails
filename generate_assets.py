import os

icons_dir = r"C:\Users\Mishu\.gemini\antigravity\scratch\oncara-nails\assets\icons"
os.makedirs(icons_dir, exist_ok=True)

svgs = {
    'logo-jaguar.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 40" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M15 28 C20 28, 25 24, 30 22 C35 20, 45 19, 55 20 C65 21, 75 18, 80 14 C83 11, 86 10, 89 12 C91 13, 90 16, 88 18 C85 20, 82 22, 80 25 C78 28, 77 34, 76 36 M80 25 C75 27, 72 32, 70 36 M50 20 C48 24, 46 30, 45 36 M38 21 C36 26, 34 32, 32 36 M25 24 C20 22, 16 18, 12 18 C8 18, 5 21, 6 25 C7 29, 11 31, 15 28" />
  <circle cx="86" cy="13" r="1" fill="#C2A06B" />
  <circle cx="42" cy="22" r="1" fill="#C2A06B" />
  <circle cx="52" cy="22" r="1" fill="#C2A06B" />
  <circle cx="62" cy="21" r="1" fill="#C2A06B" />
</svg>''',

    'eye-rays.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M8 32 C18 18, 46 18, 56 32 C46 46, 18 46, 8 32 Z" />
  <circle cx="32" cy="32" r="8" />
  <circle cx="32" cy="32" r="3.5" fill="#C2A06B" />
  <line x1="32" y1="8" x2="32" y2="16" />
  <line x1="32" y1="48" x2="32" y2="56" />
  <line x1="8" y1="32" x2="16" y2="32" stroke-dasharray="1 3" />
  <line x1="48" y1="32" x2="56" y2="32" stroke-dasharray="1 3" />
  <line x1="15" y1="15" x2="21" y2="21" />
  <line x1="49" y1="15" x2="43" y2="21" />
  <line x1="15" y1="49" x2="21" y2="43" />
  <line x1="49" y1="49" x2="43" y2="43" />
  <circle cx="32" cy="6" r="1" fill="#C2A06B" />
</svg>''',

    'moon-phases.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 24" fill="none" stroke="#C2A06B" stroke-width="1.2" stroke-linecap="round">
  <path d="M12 4 A8 8 0 0 0 12 20 A6 8 0 0 1 12 4" fill="#C2A06B" fill-opacity="0.3" />
  <path d="M28 4 A8 8 0 0 0 28 20 A2 8 0 0 1 28 4" />
  <circle cx="40" cy="12" r="7" fill="#C2A06B" fill-opacity="0.2" />
  <path d="M52 4 A8 8 0 0 1 52 20 A2 8 0 0 0 52 4" />
  <path d="M68 4 A8 8 0 0 1 68 20 A6 8 0 0 0 68 4" fill="#C2A06B" fill-opacity="0.3" />
</svg>''',

    'snake.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 64" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M24 10 C21 10, 18 12, 18 16 C18 20, 30 22, 30 28 C30 34, 18 36, 18 42 C18 48, 30 50, 30 54 C30 58, 26 60, 22 58 C18 56, 17 52, 19 50" />
  <circle cx="24" cy="10" r="4" />
  <circle cx="23" cy="9" r="1" fill="#C2A06B" />
  <path d="M24 6 L24 3 M22 2 L24 3 L26 2" />
  <path d="M22 25 Q24 23 26 25 M22 39 Q24 37 26 39" stroke-width="1" />
</svg>''',

    'moth.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="32" cy="24" rx="3" ry="12" fill="#C2A06B" fill-opacity="0.2" />
  <path d="M31 12 C28 6, 22 4, 18 6 M33 12 C36 6, 42 4, 46 6" />
  <path d="M32 16 C20 10, 6 12, 4 24 C2 32, 18 34, 30 26" />
  <path d="M32 16 C44 10, 58 12, 60 24 C62 32, 46 34, 34 26" />
  <path d="M30 26 C18 28, 12 38, 20 44 C28 50, 31 38, 32 34" />
  <path d="M34 26 C46 28, 52 38, 44 44 C36 50, 33 38, 32 34" />
  <circle cx="18" cy="22" r="2" fill="#C2A06B" />
  <circle cx="46" cy="22" r="2" fill="#C2A06B" />
  <circle cx="32" cy="10" r="1.5" fill="#C2A06B" />
</svg>''',

    'mystic-hand.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 64" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M16 48 C16 48, 14 36, 16 30 C18 24, 20 16, 20 12 C20 10, 22 10, 22 12 L23 26 C23 26, 25 14, 26 10 C27 8, 29 8, 29 11 L29 27 C29 27, 31 16, 32 13 C33 11, 35 12, 35 14 L34 30 C34 30, 36 22, 38 20 C40 19, 41 21, 40 24 C38 32, 36 44, 32 50 C28 56, 18 56, 16 48 Z" />
  <circle cx="21" cy="6" r="1.5" fill="#C2A06B" />
  <circle cx="28" cy="4" r="1.5" fill="#C2A06B" />
  <circle cx="34" cy="7" r="1.5" fill="#C2A06B" />
  <path d="M24 38 L25 36 L26 38 L28 39 L26 40 L25 42 L24 40 L22 39 Z" fill="#C2A06B" stroke="none" />
</svg>''',

    'star-4point.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#C2A06B">
  <path d="M12 0 C12 7, 12 7, 19 12 C12 12, 12 12, 12 24 C12 17, 12 17, 5 12 C12 12, 12 12, 12 0 Z" />
</svg>''',

    'star-8point.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="#C2A06B">
  <path d="M16 0 C16 9, 16 9, 25 16 C16 16, 16 16, 16 32 C16 23, 16 23, 7 16 C16 16, 16 16, 16 0 Z" />
  <path d="M16 4 C16.7 10, 16.7 10, 22 16 C16.7 16.7, 16.7 16.7, 16 28 C15.3 22, 15.3 22, 10 16 C15.3 15.3, 15.3 15.3, 16 4 Z" opacity="0.6" transform="rotate(45 16 16)" />
</svg>''',

    'botanical-branch.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 120" fill="none" stroke="#C2A06B" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M10 115 C25 90, 35 60, 45 10" />
  <path d="M38 35 C48 30, 52 22, 50 18 C45 20, 40 26, 38 35 Z" fill="#C2A06B" fill-opacity="0.2" />
  <path d="M34 50 C22 45, 18 36, 20 32 C25 34, 30 40, 34 50 Z" fill="#C2A06B" fill-opacity="0.2" />
  <path d="M28 70 C38 65, 42 58, 40 54 C35 56, 30 62, 28 70 Z" fill="#C2A06B" fill-opacity="0.2" />
  <path d="M22 88 C12 82, 8 74, 10 70 C15 72, 19 78, 22 88 Z" fill="#C2A06B" fill-opacity="0.2" />
</svg>''',

    'step-photo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <rect x="8" y="12" width="24" height="28" rx="2" />
  <rect x="16" y="8" width="24" height="28" rx="2" stroke-dasharray="2 2" />
  <circle cx="16" cy="22" r="2.5" />
  <path d="M10 34 L18 26 L26 34" />
</svg>''',

    'step-quill.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M38 8 C38 8, 22 14, 16 26 C14 30, 14 34, 12 38 C14 38, 18 37, 22 34 C32 26, 38 14, 38 8 Z" />
  <line x1="38" y1="8" x2="12" y2="38" />
</svg>''',

    'step-ruler.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <line x1="8" y1="40" x2="40" y2="8" stroke-width="2" />
  <line x1="14" y1="34" x2="18" y2="38" />
  <line x1="20" y1="28" x2="26" y2="34" />
  <line x1="26" y1="22" x2="30" y2="26" />
  <line x1="32" y1="16" x2="38" y2="22" />
</svg>''',

    'step-nails.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M16 38 L16 20 C16 14, 22 14, 22 20 L22 38 Z" />
  <path d="M26 38 L26 16 C26 10, 32 10, 32 16 L32 38 Z" />
  <path d="M17 35 C19 36, 19 36, 21 35" />
  <path d="M27 35 C29 36, 29 36, 31 35" />
</svg>''',

    'step-envelope.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <rect x="6" y="12" width="36" height="26" rx="2" />
  <path d="M6 14 L24 28 L42 14" />
  <circle cx="24" cy="28" r="1.5" fill="#C2A06B" />
</svg>''',

    'care-hands.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M14 36 C14 30, 16 24, 20 20 C22 18, 24 18, 25 21 L26 28" />
  <path d="M20 20 L22 14 C23 12, 25 12, 26 14 L27 24" />
  <path d="M27 18 L29 15 C30 13, 32 13, 33 15 L32 26" />
  <path d="M32 23 L35 21 C36 20, 38 21, 37 23 C35 28, 34 33, 30 38" />
  <circle cx="14" cy="14" r="1" fill="#C2A06B" />
  <circle cx="34" cy="10" r="1" fill="#C2A06B" />
</svg>''',

    'care-hourglass.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <line x1="14" y1="10" x2="34" y2="10" />
  <line x1="14" y1="38" x2="34" y2="38" />
  <path d="M16 10 L32 10 L25 24 L32 38 L16 38 L23 24 Z" />
  <circle cx="24" cy="28" r="1" fill="#C2A06B" />
</svg>''',

    'care-drop.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M24 10 C24 10, 14 24, 14 30 C14 35.5, 18.5 40, 24 40 C29.5 40, 34 35.5, 34 30 C34 24, 24 10, 24 10 Z" />
</svg>''',

    'care-moon.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M26 12 C18 12, 14 18, 14 26 C14 34, 20 40, 28 40 C32 40, 36 38, 38 34 C26 34, 22 24, 26 12 Z" />
  <circle cx="34" cy="14" r="1.5" fill="#C2A06B" />
</svg>''',

    'badge-wreath.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 36 C8 24, 14 14, 24 10" />
  <path d="M36 36 C40 24, 34 14, 24 10" />
  <circle cx="14" cy="22" r="1.5" fill="#C2A06B" />
  <circle cx="18" cy="16" r="1.5" fill="#C2A06B" />
  <circle cx="34" cy="22" r="1.5" fill="#C2A06B" />
  <circle cx="30" cy="16" r="1.5" fill="#C2A06B" />
</svg>''',

    'badge-crystals.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="24,6 29,14 29,38 24,42 19,38 19,14" />
  <line x1="24" y1="6" x2="24" y2="42" />
  <polygon points="14,20 18,24 18,40 13,42 10,38 10,26" />
  <polygon points="34,20 38,26 38,38 35,42 30,40 30,24" />
</svg>''',

    'badge-planet.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="24" cy="24" r="10" fill="#C2A06B" fill-opacity="0.1" />
  <ellipse cx="24" cy="24" rx="18" ry="6" />
  <circle cx="16" cy="12" r="1" fill="#C2A06B" />
</svg>''',

    'badge-heart.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M24 38 C24 38, 12 28, 12 18 C12 13, 16 10, 20 10 C22.5 10, 24 12, 24 14 C24 12, 25.5 10, 28 10 C32 10, 36 13, 36 18 C36 28, 24 38, 24 38 Z" fill="#C2A06B" fill-opacity="0.15" />
  <line x1="24" y1="4" x2="24" y2="7" />
  <line x1="14" y1="6" x2="16" y2="8" />
  <line x1="34" y1="6" x2="32" y2="8" />
</svg>''',

    'icon-search.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7" /><line x1="20" y1="20" x2="16" y2="16" /></svg>''',
    'icon-user.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>''',
    'icon-bag.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /><line x1="3" y1="6" x2="21" y2="6" /><path d="M16 10a4 4 0 0 1-8 0" /></svg>''',
    'icon-whatsapp.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>''',
    'icon-instagram.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>''',
    'icon-mail.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#C2A06B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'''
}

for name, code in svgs.items():
    with open(os.path.join(icons_dir, name), 'w', encoding='utf-8') as f:
        f.write(code)

print(f"Successfully generated {len(svgs)} SVG icons!")
