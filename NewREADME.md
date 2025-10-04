# Veluntra

## Cos’è?
script che scarica immagini da una pagina web e le salva in una cartella sul PC.

> [!WARNING]  
> scegli nomi di cartelle non esistenti per evitare di sovrascrivere dati importanti
> 
> il progetto NON è plug-and-play! serve qualche adattamento

## Roba noiosa
linkati nel repo ci sono il mio disclaimer di reponsabilità e la licenza.

## Requisiti
* PC (OS: Windows)
* Microsoft Edge
* [Python](https://www.python.org/downloads/)

## Conoscenze richieste
uso base di strumenti sviluppatore

HTML/CSS (selector)

## Varianti
Veluntra I: usa ```requests``` + ```beautifulsoup4```.

Veluntra V: come I + necessita di ```EdgeDriver```.

Veluntra X: usa ```playwright```.

Installazioni comuni: ```pip install requests beautifulsoup4```.

## Modifiche obbligatorie nel codice
url

elementi (selector)

download_dir

(service per variante V).

Avvio: posizionati nella cartella dello script e lancia python Veluntra.py (o python3 Veluntra.py).
