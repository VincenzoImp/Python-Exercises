'''
In enigmistica il crucipuzzle  e' uno schema di parole crociate dove non sono 
presenti le definizioni. E' composto da un elenco di parole ed un diagramma.
Per risolvere il crucipuzzle bisogna ricercare e poi cancellare dal diagramma TUTTE LE
OCCORRENZE (se multiple) delle parole presenti nell'elenco.
Le lettere del diagramma che rimarranno, prese tutte nel loro ordine per righe e per colonne,
formeranno la soluzione del gioco.
Le parole possono comparire  nel diagramma  in orizzontale (da destra verso sinistra, 
o da sinistra verso destra), in verticale  (dall'alto verso il basso o  dal basso verso 
l'alto)  e in diagonale (dall'alto verso il basso oppure dal basso verso l'alto).

Definire una funzione es1(ftesto), che prende l'indirizzo di un file di testo ftesto, 
contenente  diagramma ed elenco di parole di un crucipuzzle e restituisce la stringa 
soluzione del gioco. 
Il file fname  contiene  il diagramma  e, di seguito a questo  l'elenco delle parole.
Una serie di 1 o piu'  linee vuote precede il diagramma, separa il diagramma dall'elenco
delle parole e segue l'elenco delle parole.
Il diagramma e' registrato per righe (una riga per linea e in linee consecutive) gli 
elementi di ciascuna riga sono separati da un singolo carattere tab ('\t').
La lista delle parole occupa linee consecutive, una parola per ciascuna linea. 
Per un esempio si vedano i file di testo cp*.txt.

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)
''' 

'''
ALGORITHM
Dopo aver ottenuto la matrice di lettere e la lista delle parole da ricercare, ho creato
una lista contenente le righe della matrice, una contenente le colonne, una le diagonali
in un verso e una le diagonali nell'altro verso. Una volta fatto ciò, ho cercato ogni parola della
lista di parole da cercare in ognuna delle quattro liste (successivamente ho cercato
la stessa parola ma rovesciata).
Ho creato, poi, un'altra matrice composta da 0 e 1, dove gli zeri occupano le posizioni delle lettere
mai utilizzate. Infatti, per trovare la parola finale ho messo in una stringa
tutte le lettere che avevano il valore zero nella nuova matrice.
'''

def es1(ftesto):

    matr, words = importa(ftesto)

    lar = len(matr[0])
    orz,ver,didx ,disx = newlist(matr)
    mat2 = matrix(len(ver) , len(orz))
    for word in words:
        mat2 = search_or(word,orz,mat2)
        mat2 = search_ve(word,ver,mat2)
        mat2 = diagdx(word,didx,mat2)
        mat2 = diagsx(word,disx,mat2)

    testo = ''
    for i in range(len(matr)):
        for k in range(lar):
            if not mat2[i][k]:
                testo += matr[i][k]

    return testo


def matrix(x ,y ):
    mat2=[[0]*x for i in range(y)]
    return mat2

def newlist(matr):
    orz = []
    for i in matr:
        orz.append(''.join(i))
    ver = []
    for k in range(len(matr[0])):
        temp=''
        for i in matr:
            temp += i[k]
        ver.append(temp)
    didx = ['']*(len(matr[0])+ len(matr) -1)
    for i,riga in enumerate(matr):
        j = 0
        for k in range(i , i + len(riga)):
            didx[k] += riga[j]
            j += 1
    disx = ['']*(len(matr[0])+ len(matr) -1)
    for i,riga in enumerate(matr):
        j = len(matr[0])-1
        for k in range(i , i + len(riga)):
            disx[k] += riga[j]
            j -= 1
    return orz, ver, didx, disx

def search_ve(word,ver , mat2):
    for i, colonna in enumerate(ver):
            if word in colonna:
                temp = colonna
                n_colonna = i
                while word in temp:
                    n_lettera = temp.index(word)
                    inizio = (n_colonna  , n_lettera )
                    for count in range(inizio[1] , inizio[1]+len(word)):
                        mat2[count][n_colonna] = 1
                    temp = temp.replace(word, '0'*len(word) ,1)
    return mat2

def search_or(word,orz , mat2):
    for i, riga in enumerate(orz):
            if word in riga:
                temp = riga
                n_riga = i
                while word in temp:
                    n_lettera = temp.index(word)
                    inizio = (n_lettera , n_riga)
                    for count in range(inizio[0] , inizio[0]+len(word)):
                        mat2[n_riga][count] =1
                    temp = temp.replace(word, '0'*len(word) ,1)
    return mat2

def importa(ftesto):
    matrice= []
    with open(ftesto,'r',encoding='utf-8') as f:
        for riga in f:
            if riga == '\n':
                if matrice:
                    break
                continue
            else:
                matrice.append(riga.strip().split('\t'))
        words=funzione(f)
        ins = set()
        for word in words:
            ins.add(word[::-1])
        words = words | ins
    return matrice,words

def diagdx(word,didx , mat2):
    lar = len(mat2[0])
    for i ,dia in enumerate(didx):
            temp = dia
            if word in dia:
                while word in temp:
                    posizione = temp.index(word)
                    if i < lar:
                        x_1 = i
                    else:
                        x_1 = lar-1
                    if i < lar-1:
                        y_1 = 0
                    else:
                        y_1 =i - lar+1
                    inizio = (x_1 - posizione , y_1 +posizione)
                    for count in range(len(word)):
                        mat2[inizio[1] + count][inizio[0] - count]  =1
                    temp = temp.replace(word, '0'*len(word) ,1)

    return mat2



def diagsx(word,disx , mat2):
    lar = len(mat2[0])
    for i, dia in enumerate(disx):
            temp = dia
            if word in dia:
                while word in temp:
                    posizione = temp.index(word)
                    if i < lar:
                        x_1 = (lar-1) - i
                    else:
                        x_1 = 0
                    if i < lar-1:
                        y_1 = 0
                    else:
                        y_1 =i - lar+1
                    inizio = (x_1 + posizione , y_1 +posizione)
                    for count in range(len(word)):
                        mat2[inizio[1] + count][inizio[0] + count]  =1
                    temp = temp.replace(word, '0'*len(word) ,1)
    return mat2

def funzione(f):
    u= set()
    for riga in f.readlines():
        if riga =='\n':
            continue
        u.add(riga.replace('\n',''))
    return u

