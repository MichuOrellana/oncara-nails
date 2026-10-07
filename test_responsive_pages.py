import sys
import asyncio
from playwright.async_api import async_playwright

PAGES = [
    "index.html",
    "tienda.html",
    "personalizados.html",
    "sobre-oncara.html",
    "cuidados.html",
    "contacto.html"
]

VIEWPORTS = [
    {"name": "mobile_375", "width": 375, "height": 667},
    {"name": "mobile_414", "width": 414, "height": 896},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "desktop_1440", "width": 1440, "height": 900}
]

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        errors = []
        
        for page_name in PAGES:
            for vp in VIEWPORTS:
                context = await browser.new_context(viewport={"width": vp["width"], "height": vp["height"]})
                page = await context.new_page()
                
                console_msgs = []
                page.on("console", lambda msg: console_msgs.append(f"[{msg.type}] {msg.text}") if msg.type == "error" else None)
                
                url = f"http://localhost:8080/{page_name}"
                res = await page.goto(url, wait_until="networkidle")
                
                if res.status != 200:
                    errors.append(f"[{page_name} @ {vp['name']}] HTTP status {res.status}")
                
                # Check horizontal scroll overflow
                overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
                scroll_w = await page.evaluate("() => document.documentElement.scrollWidth")
                inner_w = await page.evaluate("() => window.innerWidth")
                
                if overflow and scroll_w > inner_w + 1:
                    errors.append(f"[{page_name} @ {vp['name']}] Horizontal overflow: scrollWidth={scroll_w} > innerWidth={inner_w}")
                
                # Check broken images (force lazy images to load first)
                await page.evaluate("""() => Promise.all(Array.from(document.querySelectorAll('img[loading=lazy]')).map(img => {
                    img.loading = 'eager';
                    return img.complete ? null : new Promise(r => { img.onload = img.onerror = r; });
                }))""")
                broken_imgs = await page.evaluate("""() => {
                    const imgs = Array.from(document.querySelectorAll('img'));
                    return imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src);
                }""")
                if broken_imgs:
                    errors.append(f"[{page_name} @ {vp['name']}] Broken images: {broken_imgs}")
                
                if console_msgs:
                    errors.append(f"[{page_name} @ {vp['name']}] Console errors: {console_msgs}")
                
                await context.close()
        
        await browser.close()
        
        if errors:
            print(f"FAILED with {len(errors)} errors:")
            for e in errors:
                print("  -", e)
            sys.exit(1)
        else:
            print("ALL 6 PAGES PASSED RESPONSIVE & IMAGE AUDITS AT ALL VIEWPORTS (0 overflows, 0 broken images, 0 console errors)!")

if __name__ == "__main__":
    asyncio.run(run_tests())
