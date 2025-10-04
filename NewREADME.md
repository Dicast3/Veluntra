# Veluntra

## Cos’è?
script che scarica immagini da una pagina web e le salva in una cartella sul PC.

## Roba noiosa
linkati nel repo ci sono il mio disclaimer di reponsabilità e la licenza.

## Requisiti
PC (OS: Windows)
Microsoft Edge
Python

## Conoscenze richieste
uso base di strumenti sviluppatore
HTML/CSS (selector)

## Varianti (scegli una)
Veluntra I: usa requests + beautifulsoup4. Devi impostare url, elementi (CSS selector), download_dir.
Veluntra V: come I + necessita di EdgeDriver (impostare percorso service).
Veluntra X: usa playwright (pip install playwright + playwright install), impostare url e download_dir.

Installazioni comuni: pip install requests beautifulsoup4 (o pip3); per X: pip install playwright e playwright install. Per V: scarica msedgedriver e punta il percorso nel codice.

## Modifiche obbligatorie nel codice
url
elementi (selector)
download_dir
(service per variante V).

Avvio: posizionati nella cartella dello script e lancia python Veluntra.py (o python3 Veluntra.py).

Avvertenza rapida: scegli nomi di cartelle non esistenti per evitare sovrascritture; progetto NON è plug-and-play, serve qualche adattamento
