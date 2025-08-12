# Veluntra
La magia che taglia _(le foto da un sito e incolla su una cartella nel tuo computer)_\
<sub> [Click here for the english version](https://github.com/Dicast3/Veluntra/blob/main/README.md) </sub>

## Roba burocratica (noiaaaa)
Anche se non mi piace bisogna farlo, pertanto:\
Qui c'è la [licenza](https://github.com/Dicast3/Veluntra/blob/main/LICENSE)\
Qui c'è il mio [disclaimer di responsabilità](https://github.com/Dicast3/Veluntra/blob/main/Disclaimer-ita.md)

Se non avessi voglia di leggere, ti riassumo tutto in poche parole:
1. Non sono responsabile di ciò che fai e quello che succede con questo strumento (sono fatti tuoi, non mi cercare se adesso il computer si è mangiato il gatto)
2. Questo progetto è per scopi didattici, se non dovesse essere utilizzato per questo mi arrabbierò tantissimo

## Setup
Mi dispiace, questa roba non è plug and play ed è un po sbatti, ma ne vale la pena se <mark> nE Hai ReAlMeNtE BiSoGnO</mark>.
> <sub> Altra cosa, me ne stavo quasi per dimenticare, sto scrivendo pensando di parlare con qualcuno che utilizza come sistema operativo windows, in caso il tuo sistema operativo fosse differente alcune parti dello script vanno riadattare (principalmente come vengono trovati i file e i vari percorsi) </sub>\

Prima di tutto hai bisogno di [Python](https://www.python.org/downloads/).\
Installato python bisogna scegliere con quale _variante_ di Veluntra vogliamo svolgere il nostro _***esperimento didattico***_.\
Ho vomitato 3 varianti che operano in modo differente ma che hanno lo stesso scopo, possiamo vederele più o meno così (te la faccio breve, se vuoi una spiegazione dettagliata vai [qui](link alla spiegazione dettagliata.md)):\

![Immagine illustrativa](link all'immagine illustrativa)

Una volta che abbiamo scelto la variante, tenetevi forte, avremo bisogno di altra roba da installare dal terminale :)\
per favore, passa al capitolo della variante corretta in base a quella che hai scelto

---

### Veluntra I
Per questa variante abbiamo bisogno di installare con il terminale `requests` e `beautifulsoup4`.\
Per fare questo ci basterà digitare ```pip install requests``` e fare la stessa cosa anche per `beautifulsoup4`.\
Una volta fatto questo dobbiamo prendere alcune parti del codice e modificarle a seconda delle nostre esigenze, possiamo farlo con il blocco note se ci sentiamo abbastanza badass.\
Le parti da modificare sono le seguenti:
1. La variabile `url`, al posto di `♥♥♥` ci va messo l'url della pagina esatta (quella con le immagini) dentro alle virgolette.
2. La variabile `elementi`, al posto di `★★★` ci va messo il css selector dentro alle partentesi
3. La variabile `download_dir` al posto di `◼◼◼` ci va messo un nome qualsiasi.\
> [!Attenzione]  
> Questa è la cartella di destinazione, chiamala come ti pare, ti consiglio di chiamarla diversamente rispetto a quelle che hai già per evitare spiacevoli sorprese.

### Veluntra V

### Veluntra X
