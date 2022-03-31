################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################

'''
    Es 10: 3 punti
Abbiamo una lista  di quadruple di interi. 
Ciascuna quadrupla (x1,y1,x2,y2) individua un rettangolo nel piano con lati 
perpendicolari agli assi. I primi due interi sono  l'ascisse e l'ordinata del vertice 
del rettangolo in altro a sinistra e gli ultimi due sono l'ascisse e l'ordinata del 
vertice in basso a destra. 
Data una quadrupla R rappresentante un rettangolo e la lista con le quadruple di 
rettangoli,  vogliamo sapere quali rettangoli della lista intersecano il rettangolo R.

Progettare una funzione es10(R, lista) che prende come parametri la quadrupla del rettangolo 
R e la lista con le quadruple degli altri rettangoli e restituisce un insieme 
contente le posizioni della lista in cui  compaiono rettangoli che intersecano con R.

Ad esempio per R= (2,4,6,2) e lista1=[(3,6,5,1),(6,6,7,5),(1,8,8,1)] la funzione 
deve restituire l'insieme {0,2}

NOTA: la lista NON deve essere modificata

'''

def es10(R, lista):
    # inserisci qui il tuo codice
    return { i for i,r in enumerate(lista) if intersecaR(R, r) }

def intersecaR(R, r):
    X1, Y1, X2, Y2 = R
    x1, y1, x2, y2 = r
    return intersecaI( X1, X2, x1, x2) and intersecaI(Y2, Y1, y2, y1)

def intersecaI(X1, X2, x1, x2):
    return not ( x1 > X2 or X1 > x2)

################################################################################

'''
Es 1: 3 punti

Una terna pitagorica e' un insieme di tre interi x,y,z tali che x**2+y**2=z**2.

Si definisca  la funzione es1(lis) che, riceve come argomento una lista lis 
di interi distinti e cerca in lis eventuali terne pitagoriche. 
La funzione deve restituire una lista contenente tutte le terne pitagoriche 
presenti in lis.
Ciascuna terna pitagorica  deve essere rappresentata tramite tupla, 
in ciascuna tupla  le coordinate devono avere valori crescenti e le tuple nella lista 
devono comparire in ordine crescente.
La lista iniziale non deve essere modificata.

Ad esempio:
es1([7,4,3,25,5,2,12,24,13,14]) deve restituire la lista:
[(3,4,5),(5,12,13),(7,24,25)]
'''


def es1(lis):
    # inserisci qui il tuo codice
    lista = sorted(lis)
    risultato = { (x, y, z)
                          for i,x in enumerate(lista[     :-1])
                          for j,y in enumerate(lista[i    :-1])
                          for z   in           lista[i+j+1:]
                          if pitagorica(x, y, z) }
    return sorted(risultato)

def pitagorica(a, b, c):
    return c*c == a*a + b*b

#####################################################################################

'''
Es 4: 3 punti.

Un file contiene una sequenza  di uguaglianze tra somme di interi positivi,
un'uguaglianza  per riga, ciascuna terminata da un punto e virgola, e senza spazi. 

Come esempio, si consideri il  file f4a.txt contenente le 4 righe:

2+3+12=9+8;
2+3+4=9;
22=3+4+5+10;
3+5+1=4+44;

Si noti che le uguaglianze possono essere sia corrette (le prime tre) che 
sbagliate (l’ultima).

Si progetti una funzione es4(ftesto) che riceve come argomento  l'indirizzo 
del file contenente la sequenza di uguaglianze e restituisce 
il numero di uguaglianze corrette presenti nel file. 

Per il file dell'esempio la funzione deve restituire il numero 3. 
'''

def es4(ftesto):
    # inserisci qui il tuo codice
    quante = 0
    with open(ftesto, encoding='utf8') as f:
        for linea in f:
            uguaglianza, *_ = linea.split(';')
            pre, post = uguaglianza.split('=')
            pre  = sum(map(int, pre.split('+')))
            post = sum(map(int, post.split('+')))
            if pre == post:
                quante += 1
    return quante


######################################################################################

import immagini

'''    
    Es 5: 3 punti
    Progettare la  funzione es5(fimm) che prende come parametro 
    l'indirizzo di un file .PNG e restituisce una tupla.
    La tupla e' una coppia di interi. L'intero nella prima coordinata e' 
    l'indice della colonna dell' immagine in cui compaiono il numero massimo 
    di colori distinti. L'intero nella seconda coordinata e' l'indice della riga 
    dell'immagine in cui compaiono il numero massimo di colori distinti.
    A parita' di numero massimo di colori viene scelta la colonna o la riga  
    di indice minimo.
    Ad esempio per la foto f5a.png (di 30 colonne e 20 righe ) la funzione 
    restituira' la coppia (20,10)
    
    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

def es5(fimm):
    # inserisci qui il tuo codice
    img = immagini.load(fimm)
    w = len(img[0])
    h = len(img)
    coloriC = [ set() for _ in range(w) ]
    coloriR = [ set() for _ in range(h) ]
    for y, line in enumerate(img):
        for x, colore in enumerate(line):
            coloriC[x].add(colore)
            coloriR[y].add(colore)
    conteggioC = list(map(len,coloriC))
    conteggioR = list(map(len,coloriR))
    C = max(conteggioC)
    R = max(conteggioR)
    x, y = -1, -1
    for x,N in enumerate(conteggioC):
        if N == C:
            break
    for y,N in enumerate(conteggioR):
        if N == R:
            break
    return (x, y)


############################################################################

import albero

'''
    Es 100: 3 punti
    Si definisca la funzione es100(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata, 
    torna come risultato la lista degli identificativi dei nodi dell'albero. 
    La lista deve risultare ordinata in modo crescente.

    
    Esempio:  la funzione es100
    - sull'albero a sinistra restituisce  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20] 
    - sull'albero a destra restituisce [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15].


              5                                     7              
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              5              9        
     |     _____|______                 ___|___        ___|__      
     11   |   |  |  |  |               |       |      |      |     
          10  2  9  8  7               10      8      3      1     
            __|__                     _|_     _|_    _|_    _|_    
           |     |                   |   |   |   |  |   |  |   |   
           3     1                   1   2   12  13 15  6  4   0   
                                                                   
    '''

def es100(tree):
    # inserisci qui il tuo codice
    return sorted(nodi(tree))

def nodi(tree):
    ris = [ tree.id ]
    for son in tree.f:
        ris += nodi(son)
    return ris


###########################################################################

import albero

'''
    Es 101: 3 punti

    Si definisca la funzione es101(tree) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py allegata e 
    torna come risultato una lista.
    La lista contiene tuple, una tupla per ogni livello dell'albero, 
    la tupla contiene in ordine crescente gli identificatori dei nodi 
    che si trovano ad uno stesso livello.
    Nella lista le tuple devono risultare ordinate per numero di coordinate crescente 
    e, a parita' di coordinate, in ordine lessicografico crescente.
        
    Esempio:  la funzione es101
    - sull'albero a sinistra restituisce [(5,), (22, 30), (4, 6, 20), (2, 7, 8, 9, 10, 12)]
    - sull'albero a destra restituisce [(5,),(4,20),(1,2,7,9)].

              5                                    5                    
      ________|_____________               ________|_                   
     |          |           |             |          |                  
     20         4           6             20         4                  
     |     _____|______                   |       ___|___               
     |    |   |  |  |  |                  |      |   |   |              
     12   10  2  9  8  7                  1      2   9   7              
            __|__                                                       
           |     |                                                      
           30    22                                                     
                                                                        
    '''

def es101(tree):
    # inserisci qui il tuo codice
    nodi_per_livello = []
    esplora(tree, nodi_per_livello, 0)
    nodi_per_livello = list(map( lambda l: tuple(sorted(l)), nodi_per_livello))
    return sorted(nodi_per_livello, key=lambda n: (len(n), n))

def esplora(tree, lista_id, livello):
    try:
        lista_id[livello].append(tree.id)
    except:
        lista_id.append([tree.id])
    for son in tree.f:
        esplora(son, lista_id, livello+1)



###########################################################################


'''
Es 200: 6 punti

Si definisca la funzione es200(dirpath, testo, soglia), ricorsiva o che fa uso di funzioni ricorsive,
che esplora ricorsivamente la directory indicata da dirpath cercando tutti i file che contengono
la stringa testo in un numero di righe maggiori o uguale a soglia.
Tutti i file e le directory che iniziano per '.' oppure per '_' devono essere ignorati.
La funzione deve tornare come risultato un dizionario contenente:
- come chiave i nomi dei file (senza directory) che contengono almeno soglia righe con il testo cercato
- come valore il numero di righe del file che contengono la stringa testo
Se in directory diverse si trovano file con lo stesso nome, il valore da inserire nel dizionario 
è quello del file più profondo, ed a parimerito di profondità il più grande.

Esempio: se dirpath è 'dirs/Disney' e testo è 'Topolino' e soglia è 1 il risultato sarà
    { 'Topolinia.txt': 2, }

NOTA: è vietato usare la funzione os.walk o altre librerie oltre os

'''
import os
def es200(dirpath, testo, soglia):
    trovati = scandir(dirpath, testo)
    trovati.sort(reverse=True)
    result = {}
    for livello, numero, filename in trovati:
        if filename not in result and numero >= soglia:
            result[filename] = numero
    return result

def scandir(dirpath, testo, level=0):
    result = []
    for filename in os.listdir(dirpath):
        if filename[0] in ['.','_']:
            continue
        fullpath = os.path.join(dirpath, filename)
        if os.path.isdir(fullpath):
            result += scandir(fullpath, testo, level + 1)
        else:
            count = conta(fullpath, testo)
            #print(f"{fullpath} {testo} {level} {count}")
            if count:
                result.append((level, count, filename))
    return result

def conta(filename, stringa):
    quanti = 0
    with open(filename, encoding='utf8') as f:
        for line in f:
            if stringa in line:
                quanti += 1
    return quanti


