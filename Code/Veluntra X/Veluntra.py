import time
from pathlib import Path
import os
import requests
from playwright.sync_api import sync_playwright

# URL target
url = "♥♥♥"

# Cartella download
download_dir = Path.home() / "Downloads" / "◼◼◼"
download_dir.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # True = invisibile
    page = browser.new_page()

    image_urls = set()

    def handle_request(route, request):
        if any(request.url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"]):
            image_urls.add(request.url)
        route.continue_()

    page.route("**/*", handle_request)

    page.goto(url)
    time.sleep(2)

    last_height = page.evaluate("document.body.scrollHeight")
    y = 0
    scroll_step = 300
    while y < last_height:
        page.evaluate(f"window.scrollTo(0, {y});")
        time.sleep(0.5)  # pause
        y += scroll_step
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height > last_height:
            last_height = new_height

    time.sleep(2)

    browser.close()

print(f"Trovate {len(image_urls)} immagini uniche.")

for i, img_url in enumerate(image_urls, start=1):
    try:
        r = requests.get(img_url)
        r.raise_for_status()
        estensione = os.path.splitext(img_url)[1].split("?")[0] or ".jpg"
        file_path = download_dir / f"img_{i}{estensione}"
        with open(file_path, "wb") as f:
            f.write(r.content)
        print(f"[{i}] Veluntra: {file_path}")
    except Exception as e:
        print(f"[{i}] Errore: {e}")
