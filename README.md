# Veluntra

## Cos’è?
Script che scarica immagini da una pagina web (la versione ```X``` supporta anche [lazy scrolling/loading](https://github.com/Dicast3/Veluntra/blob/main/Glossario.md#lazy-scrollingloading) e le salva in una cartella sul PC.

> [!WARNING]  
> Scegli nomi di cartelle non esistenti per evitare di sovrascrivere dati importanti
> 
> Il progetto NON è plug-and-play!

## Roba noiosa
Nella repo ci sono il mio [disclaimer di reponsabilità](https://github.com/Dicast3/Veluntra/blob/main/Disclaimer.md) e la [licenza](https://github.com/Dicast3/Veluntra/blob/main/LICENSE).

Se non avessi voglia di leggere, ti riassumo tutto in poche parole:
1. Non sono responsabile di ciò che fai e quello che succede con questo strumento (sono fatti tuoi, non mi cercare se il gatto è stato mangiato dal computer)
2. Questo progetto è per scopi didattici, se non dovesse essere utilizzato per questo mi arrabbierò tantissimo

## Casi d'uso
Mettiamo caso tu abbia creato una tua pagina web con un sacco di immagini e per qualche motivo tu voglia provare a scaricarle. \
Mettiamo caso che però hai fatto una pagina schifosa, perché a quanto pare ti sei dimenticato di inserire un pulsate per scaricare tutto il contenuto del sito. \
Questo è il tool giusto per risolvere questa tua dimenticanza.

## Requisiti
* PC (OS: Windows)
* Microsoft Edge
* [Python](https://www.python.org/downloads/)

## Conoscenze richieste
* [uso base di strumenti sviluppatore](https://github.com/Dicast3/Veluntra/blob/main/Glossario.md#uso-base-di-strumenti-sviluppatore)
* HTML/CSS (selector)

## Varianti
* [Veluntra I](https://github.com/Dicast3/Veluntra/blob/main/Code/Veluntra%20I/Veluntra.py): usa ```requests``` + ```beautifulsoup4```.
* [Veluntra V](https://github.com/Dicast3/Veluntra/blob/main/Code/Veluntra%20V/Veluntra.py): come I + necessita di ```EdgeDriver```.
* [Veluntra X](https://github.com/Dicast3/Veluntra/blob/main/Code/Veluntra%20X/Veluntra.py): usa ```playwright```.

Installazioni comuni: ```pip install requests beautifulsoup4```.

## Modifiche obbligatorie nel codice
* url
* elementi (selector)
* download_dir
* (service per variante V).

## Utilizzo

> [!NOTE]  
> Per non appesantire questo readme, ho scelto di creare una [sezione separata](https://github.com/Dicast3/Veluntra/blob/main/Tutorial.md) che dovrebbe guidare l'utente passo passo.

Posizionati nella cartella dello script con il terminale e lancia ```python Veluntra.py```.
