r'''

In una immagine in formato PNG è disegnato un albero secondo le seguenti convenzioni:
- lo sfondo dell'immagine è nero (0, 0, 0)
- la radice viene rappresentata da un pixel verde (0, 255, 0)
- tutti gli altri nodi sono rappresentati da un pixel rosso (255, 0, 0)
- due nodi sono in relazione padre-figlio se esiste una sequenza di pixel bianchi
    affiancati in orizzontale e/o verticale che li collega
- se più nodi sono collegati dalla stesso percorso bianco che si dirama,
    vuol dire che uno è il padre e gli altri sono tutti suoi figli
- una volta individuato il nodo radice è possibile individuare quali siano i padri
    e quali siano i figli in tutto l'albero navigandolo a partire dalla radice
- potete assumere che i percorsi non si intersechino (ma possono diramarsi)
    e che siano sempre larghi 1 pixel
- potete assumere che non esistano cicli (altrimenti sarebbe un grafo e non un albero)

Esempio: (R=rosso, w=bianco, V=verde, ' '=nero)
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   wwwwwww                                        | 1
         w      RwwwwwwwwwwwwwwwR         R       | 2
         w            w                   w       | 3
         w            wwwRwwwwwwww        w       | 4
         w            w          w        w       | 5
         wwwwRwwwwwwwww          Vwwwwwwwww       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------

La radice (V) è il pixel alle coordinate        (33, 6)
mentre gli altri nodi (R) sono alle coordinate  ( 3, 0), (13, 6), (15, 10), (16, 2), (25, 4), (25, 10), (32, 2), (42, 2)
L'albero che ne risulta è

                (33, 6)
               /   |   \
             /     |    \
         (25,10) (42,2)  (25,4)
                        /  |   \
                       /   |    \
                   (16,2)(32,2) (13,6)
                                /    \
                            (3,0)  (15,10)

Implementate la funzione es3(filePNGinput, filePNGoutput) che:
    - legge l'immagine PNG contenuta nel file filePNGinput
    - individua e costruisce l'albero corrispondente
    - individua i due nodi più distanti nell'albero e
        - colora di blu (0, 0, 255) tutti i pixel bianchi del percorso che li collega
          passando di nodo in nodo (se necessario ripassando su alcuni pixel 2 volte)
            (lasciando invariato lo sfondo ed i nodi rossi/verdi)
    - salva nel file filePNGoutput l'immagine risultante
    - torna come risultato il numero di pixel che sono stati colorati di blu
        (che potrebbero essere di meno della lunghezza del percorso più lungo
        perchè i tratti su cui si passa due volte vanno contati una sola volta)

NOTA: La distanza tra due nodi è il numero minimo totale dei SOLI pixel BIANCHI che li collegano
passando per i nodi interni (alcuni tratti potrebbero essere percorsi 2 volte).
SUGGERIMENTO: ispiratevi al calcolo del diametro di un albero
NOTA: per calcolare il percorso più lungo i pixel su cui si passa più volte vanno contati più volte
    (ad esempio il numero di pixel per il percorso (16,2)->(25,4)->(32,2) è 10+14=24)
NOTA: potete assumere che il percorso più lungo sia unico

Nel caso dell'esempio i due nodi più distanti sono (42,2) e (3,0) per cui l'immagine da salvare è
(b)=blu
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   bbbbbbb                                        | 1
         b      RwwwwwwwwwwwwwwwR         R       | 2
         b            w                   b       | 3
         b            bbbRbbbbbbbb        b       | 4
         b            b          b        b       | 5
         bbbbRbbbbbbbbb          Vbbbbbbbbb       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------
e la funzione torna 49 che è il numero di pixel bianchi che sono stati colorati di blu (b)

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe.
    Anche questa classe va definita esternamente alle funzioni.

ATTENZIONE: Non potete usare altre librerie a parte immagini.

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

In timeout per ciascuno dei test è di 1 secondo.

'''
import immagini

def es3(filePNGInput, filePNGOutput):
    # inserite qui il vosto codice
    img = immagini.load(filePNGInput)
    tree = Nodo.cercaAlbero(img)
    tree.altezza()
    tree.calcola_percorsi()
    print(tree)
    numPixel = tree.coloraPercorsi()
    tree.save(filePNGOutput)
    return numPixel

verde = (0, 255, 0)
rosso = (255, 0, 0)
blu   = (0, 0, 255)
nero  = (0, 0, 0)
bianco= (255, 255, 255)


class Nodo:
    @classmethod
    def cercaAlbero(cls, img):
        '''cerca i pixel e costruisce il grafo'''
        radice = cls.cercaRadice(img)
        visitati = { (radice.x, radice.y) }
        radice.cercaFigli(visitati)
        return radice

    @classmethod
    def cercaRadice(cls, img):
        for y, riga in enumerate(img):
            for x, pixel in enumerate(riga):
                if pixel == verde:
                    return cls(img, x, y, [])

    def __init__(self, img, x, y, percorso=None):
        self.img    = img
        self.x      = x
        self.y      = y
        self.sons   = []
        self.father = None      # nodo padre
        self.percorso     = set()       # percorso che porta al padre
        self.maxPercorso  = set()
        self.maxPercorsoH = set()
        self.H      = 0
        self.maxP   = 0
        if percorso:
            self.percorso = percorso

    def is_root(self):
        return not self.percorso

    def altezza(self):
        '''calcola l'altezza massima del nodo dalle foglie
            (somma delle altezze dei figli più lunghezze del percorso corrisp)
            e memorizza H max e max son
            e torna l'altezza massima'''
        if not self.sons:
            self.H            = 0
            self.maxPercorsoH = set()
        else:
            bestSon           = max( self.sons, key=lambda son: (son.altezza() + len(son.percorso)) )
            self.maxPercorsoH = bestSon.maxPercorsoH | bestSon.percorso
            self.H            = len(self.maxPercorsoH)
        return self.H

    def calcola_percorsi(self):
        # TODO: calcolare
        #   - maxpercorso fino a foglia
        #   - maxpercorso dentro al sottoalbero

        # per ogni figlio calcolo maxH->son e maxP->son
        for son in self.sons:
            son.calcola_percorsi()

        # se sono una foglia il max percorso è vuoto
        if not self.sons:
            self.maxP         = 0
            self.maxPercorso  = set()
            print(f"maxpercorso su foglia {self.x} {self.y} : {self.maxP}  {sorted(self.maxPercorso)}")

        #   se ho un solo figlio il percorso va dal padre alla foglia più lontana
        #   oppure è tutto nel sottoalbero del figlio
        #       maxP = (son.H+len(son.percorso)) -> son
        elif len(self.sons) == 1:
            son              = list(self.sons)[0]
            self.maxPercorso = son.percorso | son.maxPercorsoH
            self.maxP        = len(self.maxPercorso)
            # devo in ogni caso controllare se c'è un percorso maggiore nel sottoalbero
            if son.maxP > self.maxP:
                self.maxP        = son.maxP
                self.maxPercorso = son.maxPercorso.copy()
            print(f"maxpercorso su singolo figlio {self.x} {self.y} : {self.maxP} {sorted(self.maxPercorso)}")

        #   se ho più figli prendo le due altezze maggiori (H1->son1+len(son1.percorso)) e (H2->son2+len(son2.percorso))
        #       myP = (H1->son1+len(son1.percorso)) + (H2->son2+len(son2.percorso))
        #       e prendo il massimo tra myP e tutti quelli dei figli
        else:
            S1, S2, *_ = sorted(self.sons, key=lambda son: (son.H + len(son.percorso)), reverse=True)
            self.maxPercorso = S1.maxPercorsoH | S1.percorso | S2.maxPercorsoH | S2.percorso
            self.maxP        = len(self.maxPercorso)

            bestSon = max(self.sons, key=lambda son: son.maxP )
            if bestSon.maxP > self.maxP:
                self.maxP        = bestSon.maxP
                self.maxPercorso = bestSon.maxPercorso.copy()
            print(f"maxpercorso su più figli {self.x} {self.y} : {self.maxP}  {sorted(self.maxPercorso)}")

    def __repr__(self, level=0):
        s  = f"{'|   '*level} ({self.x}, {self.y}) {'    '*(3-level)}\t{self.percorso}\n"
        s += f"{'|---'*level} {self.maxP} {'    '*(3-level)}\t{self.maxPercorso}\n"
        for son in self.sons:
            s += son.__repr__(level+1)
        return s

    def cercaFigli(self, visti):
        figli = self._cercaFigli(visti)
        self.sons = figli
        for son in figli:
            son.father = self
            son.cercaFigli(visti)

    def _cercaFigli(self, visti=set()):
        img = self.img
        x, y = self.x, self.y
        vicinato = ((-1,0),(1,0),(0,-1),(0,1))
        w = len(img[0])
        h = len(img)
        figli = set()
        visitati = {}
        da_vedere = {(x, y)}
        while da_vedere:
            x, y = da_vedere.pop()
            visti.add((x,y))
            for dx,dy in vicinato:
                X,Y = x+dx, y+dy
                if 0 <= X < w and 0 <= Y < h and (X,Y) not in visti:
                    pixel = img[Y][X]
                    if pixel == bianco:
                        da_vedere.add((X,Y))
                        visitati[(X, Y)] = (x, y)
                    elif pixel == rosso:
                        visitati[(X, Y)] = (x, y)
                        XX, YY = X, Y
                        percorso = set()
                        while (XX,YY) in visitati:
                            XX,YY = visitati[XX,YY]
                            percorso.add((XX, YY))
                        figli.add(Nodo(img, X, Y, percorso))
        return figli

    def coloraPercorsi(self):
        N = 0
        for x, y in self.maxPercorso:
            if self.img[y][x] == bianco:
                self.img[y][x] = blu
                N += 1
        return N

    def save(self, filename):
        immagini.save(self.img, filename)


def salva_immagine(text, name):
    colore = {
        ' ': nero,
        'R': rosso,
        'V': verde,
        'w': bianco,
        'b': blu
    }
    filename = f"es3_{name}.png"
    img = [ [
        colore[c] for c in line
    ] for line in text.split('\n') if line != '']
    immagini.save(img, filename)
