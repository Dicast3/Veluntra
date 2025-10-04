# Veluntra

Cos’è: script che scarica immagini da una pagina web e le salva in una cartella sul PC.

License / Disclaimer: linkati nel repo (leggi se vuoi responsabilità e limiti).

Requisiti: PC (Windows presumibile), Microsoft Edge, Python.

Conoscenze richieste: base di uso strumenti sviluppatore e HTML/CSS (selector).

Varianti (scegli una):

Veluntra I: usa requests + beautifulsoup4. Devi impostare url, elementi (CSS selector), download_dir.

Veluntra V: come I + necessita di EdgeDriver (impostare percorso service).

Veluntra X: usa playwright (pip install playwright + playwright install), impostare url e download_dir.

Installazioni comuni: pip install requests beautifulsoup4 (o pip3); per X: pip install playwright e playwright install. Per V: scarica msedgedriver e punta il percorso nel codice.

Modifiche obbligatorie nel codice: cambiare url, elementi (selector) e download_dir (e service per V).

Avvio: posizionati nella cartella dello script e lancia python Veluntra.py (o python3 Veluntra.py).

Avvertenza rapida: scegli nomi di cartelle non esistenti per evitare sovrascritture; progetto NON è plug-and-play, serve qualche adattamento.

Se vuoi, te lo sintetizzo ancora di più in 3 parole: configura, punta, lancia.
