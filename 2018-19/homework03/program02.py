'''
Possiamo rappresentare lo skyline di una citta' con un numero di rettangoli di 
diversi colori e dimensioni su di uno sfondo omogeneo. Vedi ad esempio i file es2_risTest*.png .
Uno skyline e' dunque una sequenza di rettangoli posizionati sull'asse x delle ascisse. 
La posizione del rettangolo all'interno dello skyline (nel seguito posizione del rettangolo) 
e' individuata univocamente dalla coordinata x occupata dal suo vertice in basso a sinistra.
Uno stesso rettangolo puo' essere presente piu' volte all'interno della sequenza in diverse posizioni. 

Per i nostri skyline valgono i seguenti vincoli:
1) nello skyline non compaiono mai due rettangoli con la stessa posizione.
2) nello skyline non compare mai un rettangolo che ha lo stesso colore dello sfondo.
3) Se due rettangoli si intersecano, quello che ha luminosita' massima appare in primo piano e 
in caso di pari luminosita'  e' in primo piano il rettangolo posizionato piu' a sinistra 
(la luminosita' di un rettangolo e' la somma delle tre componenti  del suo colore)
 
Definire una classe Colore, una classe Rettangolo e una classe Skyline secondo le seguenti specifiche.

La classe Colore deve implementare i seguenti metodi:
- __init__(self,r=0,g=0,b=0)  che inizializza un colore con la terna RGB (r,g,b) valida.
- utilizzo(self, sk) dove sk e' un oggetto di tipo Skyline. Il metodo ritorna  il numero di occorrenze 
  di rettangoli con il colore self presenti nello skyline sk 
  (ricorda che in uno skyline uno stesso rettangolo puo' comparire piu' volte in diverse posizioni)
- to_tuple(self) che torna la terna (r, g, b)

La classe Rettangolo deve implementare i seguenti metodi:
- __init__(self,base, altezza, colore) Base ed altezza sono due interi positivi e 
  rappresentano la lunghezza della base e dell'altezza del rettangolo, colore e' un oggetto 
  della classe Colore. 
- cancella(self) cancella le occorrenze del rettangolo da tutti gli skyline in cui e' presente. 
- to_tuple(self) che torna la terna (base, altezza, colore)

La classe Skyline deve implementare i seguenti metodi:
- __init__(self, sfondo) dove sfondo e' un oggetto di tipo Colore. 
  definisce uno skyline vuoto con colore di sfondo uguale a 'sfondo'. 
- aggiungi(self, ret, x) l' oggetto ret di tipo Rettangolo viene aggiunto  
  allo skyline a partire dall'ascissa x, l'aggiunta avviene solo se non vengono violate le regole 1), 2) e 3) 
  dello skyline. 
- fondi(self, other) con argomento other di tipo Skyline, che inserisce nello skyline self tutte le occorrenze  
  di rettangoli dello skyline other. I rettangoli vanno inseriti nelle stesse posizioni che occupavano in other 
  e l'inserimento di ciascun rettangolo avviene solo se non viola le regole degli skyline 
  (ricorda che in uno skyline non e' possibile inserire rettangoli che hanno lo stesso colore dello sfondo 
  ne' rettangoli da posizionare ad una ascissa gia' occupata).
- salva(self, fimg)   salva  l'immagine dello skyline sotto forma di file PNG all'indirizzo fimg. 
- larghezza(self) restituisce la larghezza dello skyline (vale a dire il valore massimo di x+base, 
  dove base e' la base del rettangolo inserito alla posizione x).
  Uno skyline vuoto ha per convenzione larghezza zero.
- altezza(self) restituisce l'altezza dello skyline (vale a dire l'altezza massima tra quelle dei 
  rettangoli presenti nello skyline). Uno skyline vuoto ha per convenzione altezza zero.
- edifici(self) restituisce il numero di rettangoli presenti nello skyline.
- to_tuple(self) che torna la tupla (sfondo,)

DEFINIZIONE DELLE CLASSI
Siete liberi di scegliere sia gli attributi da usare in ciascun oggetto che la loro implementazione.
Se lo ritenete utile potete aggiungere altri metodi alle vostre classi.

GESTIONE DEGLI ERRORI
Tutti i metodi ed i costruttori devono controllare che gli argomenti forniti siano corretti, 
e altrimenti lanciare l'eccezione ValueError (già presente in Python).

Per  salvare i file PNG si possono usare la funzione  save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: non potete usare altre librerie.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

'''

import immagini, copy

class Colore:
    def __init__(self,r=0,g=0,b=0):
        for p in [r,g,b]:
            if not (type(p) == int and 0 <= p <= 255):
                raise ValueError( str(p) )
        self.colore = r, g, b

    def utilizzo(self, sk):
        if not isinstance(sk, Skyline):
            raise ValueError()
        count = 0
        for r in sk.rettangoli.values():
            if r.colore == self:
                count += 1
        return count

    def luminosita(self):
        return sum(self.colore)

    def __eq__(self, other):
        return isinstance(other, Colore) and self.colore == other.colore

    def to_tuple(self):
        return self.colore


class Rettangolo:
    def __init__(self,base,altezza,colore):
        if not (type(base) == int and 0 < base):
            raise ValueError( str(base) )
        if not (type(altezza) == int and 0 < altezza):
            raise ValueError( str(altezza) )
        if not isinstance(colore, Colore):
            raise ValueError()
        self.base     = base
        self.altezza  = altezza
        self.colore   = colore
        self.skylines = set()

    def cancella(self):
        for sk in self.skylines:
            for x, r in [ _ for _ in sk.rettangoli.items() ]:
                if r is self:
                    del sk.rettangoli[x]
        self.skylines = set()

    def to_tuple(self):
        return (self.base,
                self.altezza,
                self.colore)

class Skyline:
    def __init__(self,sfondo):
        if not isinstance(sfondo, Colore):
            raise ValueError()
        self.sfondo=sfondo
        self.rettangoli = {}

    def aggiungi(self,rettangolo,x):
        if not isinstance(rettangolo, Rettangolo):
            raise ValueError(str(rettangolo))
        if not (type(x) == int and 0 < x):
            raise ValueError(str(x))
        if self.sfondo != rettangolo.colore and x not in self.rettangoli:
            self.rettangoli[x] = rettangolo
            rettangolo.skylines.add(self)

    def salva(self, fimg):
        '''Salva lo skyline nel file fimg di tipo png'''
        def ordine(args):
            x, r = args
            return ( r.colore.luminosita(), -x)
        if not (type(fimg) == str and fimg[-4:] == '.png'):
            raise ValueError(str(fimg))
        rettangoli = list(self.rettangoli.items())
        rettangoli.sort(key=ordine)
        w = self.larghezza()
        h = self.altezza()
        s = self.sfondo.to_tuple()
        img = [ [ s ] * w for _ in range(h) ]
        for x, r in rettangoli:
            c = r.colore.to_tuple()
            for X in range(x, x+r.base):
                for Y in range(h-r.altezza, h):
                    img[Y][X] = c
        immagini.save(img, fimg)

    def fondi(self, other):
        if not isinstance(other, Skyline):
            raise ValueError(str(other))
        for x, r in other.rettangoli.items():
            self.aggiungi(r, x)

    def larghezza(self):
        return max( ( x + r.base for x,r in self.rettangoli.items() ) , default=0)

    def altezza(self):
        return max( ( r.altezza for r in self.rettangoli.values() ), default=0)

    def edifici(self):
        return len(self.rettangoli)

    def to_tuple(self):
        return (self.sfondo,)


