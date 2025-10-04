# Tutorial
## Setup preliminare (continua con la variante)
Mi dispiace, questa roba non è plug and play ed è un po sbatti, ma ne vale la pena se <mark> nE Hai ReAlMeNtE BiSoGnO</mark>.
> <sub> Altra cosa, me ne stavo quasi per dimenticare, sto scrivendo pensando di parlare con qualcuno che utilizza come sistema operativo windows, in caso il tuo sistema operativo fosse differente alcune parti dello script vanno riadattare (principalmente come vengono trovati i file e i vari percorsi) </sub>\

Prima di tutto bisogna scegliere quale _variante_ di Veluntra vogliamo utilizzare per svolgere il nostro _***esperimento didattico***_, nel dubbio ti consiglio di dirigerti [qui](https://github.com/Dicast3/Veluntra/tree/main/Code) e scaricare tutto il contenuto di questa cartella.\
Ho vomitato 3 varianti che operano in modo differente ma che hanno lo stesso scopo, possiamo vederele più o meno così (te la faccio breve, se vuoi una spiegazione dettagliata vai [qui](https://github.com/Dicast3/Veluntra/blob/main/Assets/spiegone-ita.md)):

Una volta che abbiamo scelto la variante, tenetevi forte, avremo bisogno di altra roba che installeremo a seconda di cosa abbiamo scelto.

---
---

### Veluntra I
Per questa variante abbiamo bisogno di installare con il terminale `requests` e `beautifulsoup4`.\
Per fare questo ci basterà digitare ```pip install requests``` e fare la stessa cosa anche per `beautifulsoup4`.
> [!TIP]
> In caso non dovesse funzionare con ```pip```, possiamo provare scrivendo ```pip3```

Una volta fatto questo dobbiamo prendere alcune parti del codice e modificarle a seconda delle nostre esigenze, possiamo farlo con il blocco note se ci sentiamo abbastanza badass.\
Le parti da modificare sono le seguenti:
* La variabile `url`, al posto di `♥♥♥` ci va messo l'url della pagina esatta (quella con le immagini) dentro alle virgolette.

```python
url = "♥♥♥"
```

* La variabile `elementi`, al posto di `★★★` ci va messo il css selector dentro alle partentesi

```python
elementi = soup.select("img.★★★")
```

> [!NOTE]
> ecco un esempio, questa roba la trovi nell'html e sono specificati da qualcosa come `div class=main`. Come puoi notare, se "sotto" al primo ce ne sono di altri, ci basterà separare il tutto con uno spazio fino a che non arriveremo a quello dell'immagine che di solito presenta anche un link (quello dell'immagine che vogliamo scaricare):

```python
elementi = soup.select("div.main div.upper_class-name img.class-name")")
```

* La variabile `download_dir` al posto di `◼◼◼` ci va messo un nome qualsiasi.\

```python
download_dir = Path.home() / "Downloads" / "◼◼◼"
```

> [!WARNING]  
> Questa è la cartella di destinazione, chiamala come ti pare, ti consiglio di chiamarla diversamente rispetto a quelle che hai già per evitare spiacevoli sorprese.

---

### Veluntra V
Per questa variante abbiamo bisogno di installare e modificare le solite cose che sono necessarie per [Veluntra I](https://github.com/Dicast3/Veluntra/blob/main/README-ita.md#veluntra-i), con una piccola aggiunta.

Fatte tutte le modifiche come indicato per Veluntra I, adesso possiamo ultimare gli ultimi dettagli:
* Scaricare la versione corretta per il tuo computer di [edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)
* Modificare la variabile `service`: al posto di `C:\Users\⬤⬤⬤\edgedriver_win64\msedgedriver.exe` ci va messo il percorso preciso per trovare i driver.

---

### Veluntra X
Per questa variante abbiamo bisogno di installare `playwright` con `pip install playwright` e con `playwright install`.\
Le cose da modificare sono:
* La variabile `url`
* La variabile `download_dir`


<sub> Per sapere come fare, vedi le varianti precedenti, non ho più voglia di scrivere. </sub>

---
---

## Utilizzo
Per utilizzare Veluntra ti basta cambiare la cartella in cui si trova lo script che hai scaricato (`ls` e `cd` sono i tuoi migliori amici)
> [!NOTE]
> puoi anche provare a scrivere `cd "`, trascinare la cartella in cui si trova lo script sulla finestra del terminale e chiudere con `"`

e aprire il terminale e scrivere `python Veluntra.py` oppure `python3 Veluntra.py`

