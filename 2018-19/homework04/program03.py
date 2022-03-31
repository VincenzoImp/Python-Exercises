'''
Si vuole visualizzare una gerarchia di directory in modo grafico producendo una immagine PNG a forma di albero orizzontale.

Per visualizzare ciascun nome di file/directory si userà una codifica caratteri->componenti di colore.

Si assume che il nome del file abbia sempre lunghezza al piu’ 30 
e che, per ogni carattere c del nome, il codice unicode (ottenibile tramite la funzione ord(c)) dia sempre un intero tra 0 e 255.

NOTA: Tutti i file o le directory che iniziano col carattere '.' devono essere ignorati.

Stando cosi le cose il nome viene trasformato in una sequenza di 10 pixel nel seguente modo:
- si trasforma in una lista interi il testo utilizzando la funzione ord carattere per carattere.
- se la lista risulta avere meno di 30 elementi viene portata a 30 interi aggiungendo degli 0 in fondo.
- si codifica ciascuna tripletta ABC di interi  consecutivi in un colore con componenti (A, B, C)

Esempio:    'Paperino.txt'
in interi:  [80, 97, 112, 101, 114, 105, 110, 111, 46, 116, 120, 116] + [0]*18
in colori:  [(80, 97, 112), (101, 114, 105), (110, 111, 46), (116, 120, 116)] + [(0, 0, 0)]*6

L'albero delle directory viene rappresentato seguendo queste regole:
- la radice è posizionata a coordinate 0,0 (quindi occupa i primi 10 pixel della prima linea)
- se un nodo è una directory ed ha figli:
    - i corrispondenti sottoalberi vengono visualizzati uno sotto l'altro in ordine crescente alfabetico delle radici dei sottoalberi
    - il nodo è collegato al primo figlio da una linea bianca orizzontale di 10 pixel
    - i figli successivi sono raggiunti da una linea spezzata
        - 5 pixel orizzontali (ovvero la metà della linea che collega al primo figlio)
        - tanti pixel verticali quanti ne sevono ad arrivare al prossimo figlio
        - 5 pixel orizzontali per arrivare al prossimo figlio
    - L'altezza totale di un sottoalbero è la somma delle altezze dei sottoalberi
        lasciando uno spazio di 1 pixel tra ciascun sottoalbero
- se un nodo è una foglia viene disegnato con i suoi 10 pixel
    l'altezza del disegno della foglia è di 1 pixel

Vedete l'esempio in Informatica.png che rappresenta la sottodirectory dirs/Informatica

L'immagine da produrre e salvare deve avere:
    - larghezza sufficiente a contenere tutto l'albero
        (con 10 pixel per ogni nome e 10 pixel di separazione tra ciascun livello)
    - altezza pari all'altezza sufficiente a contenere tutto l'albero
    - sfondo nero (0,0,0)

Implementare la funzione es3(path, filePNG) che (se necessario usando altre funzioni, oggetti o metodi):
    - esplora la gerarchia di directory che parte dalla directory path
    - se necessario costruisce un albero che potete implementare come oggetti
    - costruisce una immagine come lista di liste di triple con il disegno dell'albero
    - la salva nel file filePNG
    - torna come risultato la coppia (larghezza, altezza) della immagine

NOTA: Il timeout per ciascun test per questo esercizio è di 4 secondi.

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe.

ATTENZIONE: Non potete usare altre librerie a parte os, os.path e immagini.

ATTENZIONE: è VIETATO usare la funzione di libreria os.walk

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)
'''

'''
ALGORITHM
per prima cosa creo l'abero con le directory scludendo quelle che iniziano per '.'
poi scorro l'albero con una funzioni ricorsiva con la qualle se sempre che vado
in avanti faccio la codifica del nome del nodo a colori + [(255,255,255)]*10 se il nodo
non è una foglia e mano a mano mi salvo la coordinata del nodo che è la len di una lista
che accumula i dati ad esempio 'l' -5 e ogni volta che trovo una foglia inserisco e approffitando
le propieta della ricorsione ho una variabile 'c' che si mantine a zero sempre che scorro i nodi
quando arrivavo a una foglia allora c incrementa e se c incrementa vuole dire che il quel dato va inserito
in nodo.pre.coordinate che contiene le coordinate del padre di quel nodo per tanto questo replica il
comportamento della funzione ricorsiva e posso creare l'immagine scorrendo soltanto l'albero delle directory
'''

import immagini, os

def es3(path, filePNG):
    tree = Tree(path)               # creo l'albero
    return tree.save(filePNG)       # lo salvo tornando larghezza ed altezza

class Tree:
    def __init__(self, path):
        """Il costruttore esplora la directory e costruisce l'albero"""
        self.path    = path
        self.name    = os.path.basename(path)
        self.content = []
        if os.path.isdir(path):
            for file in sorted(os.listdir(path)):
                if '.' != file[0]:
                    filepath = os.path.join(path, file)
                    self.content.append(Tree(filepath))
            #self.content.sort(key=lambda n: n.name)

    def __str__(self, level=0):
        '''stampa ricorsiva dei nodi e delle loro posizioni'''
        return "|   "*level + f"{self.name} ({self.x},{self.y})\n" + ''.join([son.__str__(level+1) for son in self.content])

    def name_to_pixels(self):
        '''Trasformo il nome di un file in una sequenza di 10 pixel'''
        caratteri = list(bytes(self.name, 'utf8')) + [0]*30
        caratteri = caratteri[:30]
        pixels = []
        while caratteri:
            r, g, b, *caratteri = caratteri
            pixels.append((r,g,b))
        return pixels

    def posizione_X(self, livello=0):
        '''calcolo le posizioni X di ciascun nodo (ovvero livello*20)
            torno la largezza massima (ultimo livello + 10 dell'ultimo nodo)
        '''
        self.x = livello * 20
        maxx = self.x + 10
        for son in self.content:
            maxx = max(maxx, son.posizione_X(livello+1))
        return maxx

    def posizione_Y(self, y=0):
        '''Calcolo le posizioni Y di ciascun nodo spaziando gli alberi di 1 pixel
            Torno la posizione y dell'ultimo nodo in basso
        '''
        self.y = y
        if self.content:
            first, *rest = self.content
            y = first.posizione_Y(y)
            for son in rest:
                y = son.posizione_Y(y+2)
            else:
                return y
        return y+1

    def draw(self, img):
        '''disegno l'albero sulla immagine'''
        # prima disegno il nodo
        for x,c in enumerate(self.name_to_pixels()):
            img[self.y][self.x+x] = c
        # poi se ci sono figli
        if self.content:
            # linea orizzontale di 5 pixel
            self.draw_H(img, self.x+10, self.x+15, self.y)
            for son in self.content:
                # figlio
                son.draw(img)
                # sua lineetta orizzontale di 5 pixel
                self.draw_H(img, son.x-5, son.x, son.y)
            # linea verticale dal padre all'ultimo figlio
            self.draw_V(img, self.x+15, self.y, self.content[-1].y)

    def draw_H(self, img, x0, x1, y):
        '''disegna una riga bianca orizzontale'''
        for x in range(x0, x1):
            img[y][x] = (255, 255, 255)

    def draw_V(self, img, x, y0, y1):
        '''disegna una riga bianca verticale'''
        for y in range(y0, y1):
            img[y][x] = (255, 255, 255)

    def save(self, filePNG):
        '''crea l'immagine e la salva tornando le dimensioni'''
        w = self.posizione_X()                      # calcola le posizioni X e la larghezza massima
        h = self.posizione_Y()                      # calcola le posizioni Y e l'altezza massima
        img = [[(0, 0, 0)] * w for _ in range(h)]   # crea l'immagine
        self.draw(img)                              # ci disegna l'albero
        immagini.save(img, filePNG)                 # la salva
        return w, h                                 # torna le dimensioni
