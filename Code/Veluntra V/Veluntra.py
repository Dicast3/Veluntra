import time
import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

url = "♥♥♥"

download_dir = Path.home() / "Downloads" / "◼◼◼"
download_dir.mkdir(parents=True, exist_ok=True)

edge_options = Options()
# edge_options.add_argument("--headless")  # ❌ Rimosso: finestra visibile
edge_options.add_argument("--start-maximized")

service = Service(r"C:\Users\⬤⬤⬤\edgedriver_win64\msedgedriver.exe")  # <-- qui il percorso giusto
driver = webdriver.Edge(service=service, options=edge_options)

driver.get(url)
time.sleep(3)  # attesa caricamento iniziale

# Scroll lento visibile
last_height = driver.execute_script("return document.body.scrollHeight")
y = 0
scroll_step = 300  # px
while y < last_height:
    driver.execute_script(f"window.scrollTo(0, {y});")
    time.sleep(0.5)  # mezzo secondo tra ogni scroll
    y += scroll_step
    last_height = driver.execute_script("return document.body.scrollHeight")

time.sleep(2)  # attesa finale per completare caricamenti

# HTML finale dopo lo scroll
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")
selector = "img.★★★"
elementi = soup.select(selector)

print(f"Trovati {len(elementi)} elementi.")

possible_attrs = ["src", "data-src", "data-original", "data-lazy", "data-image"]

for i, elem in enumerate(elementi, start=1):
    src = None
    for attr in possible_attrs:
        if elem.get(attr):
            src = elem.get(attr)
            break

    if not src:
        print(f"[{i}] Nessun URL trovato, salto.")
        continue

    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        src = url.rstrip("/") + src

    try:
        file_data = requests.get(src)
        file_data.raise_for_status()
        estensione = os.path.splitext(src)[1] or ".jpg"
        file_path = download_dir / f"immagine_{i}{estensione}"
        with open(file_path, "wb") as f:
            f.write(file_data.content)
        print(f"[{i}] Scaricato: {file_path}")
    except Exception as e:
        print(f"[{i}] Errore: {e}")
