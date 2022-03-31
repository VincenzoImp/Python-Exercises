'''
Abbiamo una immagine  .PNG . 
L'immagine presenta, su uno sfondo nero ( vale a dire di colore (0,0,0)), 
segmenti di colore bianco (vale a dire (255,255,255)) orizzontali e verticali di diversa lunghezza. 
Si veda ad esempio il file f1.png.
I segmenti, in alcuni casi, nell'incrociarsi creano rettangoli. 
Siamo interessati a trovare quei rettangoli di altezza e larghezza almeno 3 
(compreso il bordo, quindi con la parte nera alta e larga almeno 1 pixel)
e che, tranne il bordo completamente bianco, presentano tutti i pixel al loro interno di colore nero. 
A questo scopo vogliamo creare una nuova immagine identica alla prima se non per il 
fatto che questi rettangoli vengono evidenziati. 
Il bordo di questi rettangoli deve essere di colore verde (vale a dire (0,255,0)) e 
i pixel interni devono essere di colore rosso (vale a dire (255,0,0)).
Ad esempio l'immagine che vogliamo ricavare da quella nel file  f1.png e' nel file Risf1.png.

Scrivere una funzione es1(fimg,fimg1) che, presi in input gli indirizzi  di due file .PNG, 
legge dal primo l'immagine del tipo descritto sopra e salva nel secondo l'immagine 
con i rettangoli evidenziati. 
La funzione deve infine restituire  il numero di rettangoli che risultano evidenziati.

Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun test (sulla VM).

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

ATTENZIONE: non sono permesse altre librerie.
'''

'''
ALGORITHM
per prima cosa carico l'immagine in una variabile. Poi scorrendo i pixel dell'immagine mi salvo in una lista le coordinate dei pixel dove in basso e alla loro destra hanno un pixel bianco e in basso a destra hanno un pixel nero. Per ogni coordinata che risolve
questi controlli chiamo una funzione che scorre da quel pixel ogni valore alla sua destra che deve essere sempre bianco e sotto di lui nero. la funzione termina e mi restituisce la coordinata del pixel che sarà bianco ma sotto avrà unaltro pixel bianco. se questo
non avviene o qualche controllo non viene superato allora esco dalla funzione e non ritorno nulla. Infine la mia lista avrà solo delle liste che conterranno la coordinata superiore sinistra del possibile rettangolo e la corrispondente superiore destra. Per ognuna
di queste liste(coordinate vertici superiori del possibile rettangolo) controllo se i pixel con le stesse coordinate ma con y-1 siano bianchi, se è così controllo tutti i pixel tra quester due coordinate. se sono tutti bianchi allora il rettangolo è finito e lo
salvo, se i pixel sono tutti neri proseguo con le coordinate dei vertici -2 eccetera, altrimenti il rettangolo non rispetta le caratteristiche essenziali e quindi passo alla prossima coppia di coordinate di vertici superiori e così via. alla fine così avrò solo
i quattro vertici dei soli rettangoli utili, quindi coloro i loro bordi di verde e internamente di rosso e nel mentre conto quanti sono e riporto il loro conteggio come uscita della funzione.
'''

import immagini

def genera_lista_2(i, y, x, lista, bianco=(255, 255, 255), c=1):
    while i[y+1][x+c]!=bianco and i[y][x+c]==bianco and i[y][x+c+1]==bianco:
        c+=1
    if c!=1 and i[y+1][x+c] == bianco:
        lista.append([(x,y),(x+c,y)])
    return lista

def genera_lista(i, lista, bianco=(255,255,255)):
    for y in range(len(i)-2):
        for x, tupla in enumerate(i[:-2]):
            if i[y][x]==bianco and i[y+1][x]==bianco and i[y][x+1]== bianco and i[y+1][x+1]!=bianco:
                lista=genera_lista_2(i, y, x, lista)
    return lista, lista[:]

def funzione1(i, nuova, lista, lista_finali):
    for vertici in nuova:
        indice_iniziox=vertici[0][0]
        indice_finex=vertici[1][0]
        wile=True
        while wile:
            elemento, l=funzione2(i, vertici, indice_iniziox, indice_finex, vertici[0][1]+1)
            lista_finali+=l
            if elemento ==1 or elemento==0:
                wile=False
        if elemento==1:
            lista.remove(vertici)
    return lista_finali

def funzione2(i, vertici, indice_iniziox, indice_finex, scorrimentoy, uscita=0, bianco=(255,255,255)):
    if i[scorrimentoy][indice_iniziox]==bianco and i[scorrimentoy][indice_finex]==bianco:
        for scorrimentox in range(indice_iniziox+1, indice_finex):
            if i[scorrimentoy+1][scorrimentox]==bianco:
                uscita+=1
        if uscita==indice_finex-indice_iniziox-1:
            if i[scorrimentoy+1][scorrimentox+1]==bianco and i[scorrimentoy+1][indice_iniziox]==bianco:
                return 0, [(scorrimentox+1,scorrimentoy+1)]
            else:
                return 1, []
        elif 0<uscita<indice_finex-indice_iniziox-1:
            return 1, []
        else:
            return funzione2(i, vertici, indice_iniziox, indice_finex, scorrimentoy+1)
    else:
        return 1, []

def genera_uscita(fimg1, img, q, c=0):
    for w in q:
        c+=1
        for x in range(w[0][0][0]+1,w[1][0]):
            for y in range(w[0][0][1]+1,w[1][1]):
                img[y][x]=(255,0,0)
    immagini.save(img, fimg1)
    return c

def colora_linee(img, q):
    for w in q:
        costantez1=w[0][0][1]
        costantez2=w[1][1]
        costantev1=w[0][0][0]
        costantev2=w[1][0]
        for z in range(costantev1, costantev2+1):
            img[costantez1][z]=(0,255,0)
            img[costantez2][z]=(0,255,0)
        for v in range(costantez1,costantez2+1):
            img[v][costantev1]=(0,255,0)
            img[v][costantev2]=(0,255,0)
    return q

def es1(fimg, fimg1):
    '''scova in fimg i rettangoli da evidenziale, crea una copia dell'immagine
    in cui questi rettangoli risultano evidenziati (vale a dire hanno bordo  verde e
    interno  rosso) salva l'immagine in fimg1 e restituisce il numero di rettangoli
    evidenziati. '''
    i=immagini.load(fimg)
    lista, nuova=genera_lista(i,[])
    lista_finali=funzione1(i, nuova, lista, [])
    q=colora_linee(i[:], list(zip(lista,lista_finali)))
    return genera_uscita(fimg1, i[:], q)
