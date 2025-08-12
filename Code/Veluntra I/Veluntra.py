import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os

url = "♥♥♥"

download_dir = Path.home() / "Downloads" / "◼◼◼"
download_dir.mkdir(parents=True, exist_ok=True)

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# CSS selector
elementi = soup.select("img.★★★")

for i, elem in enumerate(elementi, start=1):
    src = elem.get("src")
    if not src:
        continue

    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        src = url.rstrip("/") + src

    file_data = requests.get(src)
    file_data.raise_for_status()

    estensione = os.path.splitext(src)[1]
    file_path = download_dir / f"img_{i}{estensione}"

    with open(file_path, "wb") as f:
        f.write(file_data.content)

    print(f"Velutra: {file_path}")
