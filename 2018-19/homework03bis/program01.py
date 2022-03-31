# -*- coding: utf-8 -*-

'''
Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine.

Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro
spostandosi solo su pixel adiacenti e dello stesso colore (ovviamente perche'
cio' sia possibile e' necessario che i due pixel abbiano lo stesso colore).

Scrivere una funzione es1(fname, colore, fnameout) che, presi:
    -un nome di file contenente una immagine in formato PNG
    -una tupla con un colore in formato RGB
    -un nome di file su cui salvare una immagine in formato PNG
legge l'immagine in fname, cerca l'area massima di pixel adiacenti dell'immagine
con il colore preso in input e registra una nuova immagine nel file fnameout,
contenente soltanto i pixel dell'area massima individuata. Il colore di sfondo
dell'immagine di output deve essere il complementare del colore preso in input
(ovvero il colore che si ottiene complementando a 255 le componenti RGB).

La funzione deve ritornare il numero di pixel dell'area massima individuata.

Assumete che l'area massima sia unica.

Il TIMEOUT per ciascun test è di 5 secondi.

Per caricare e salvare immagini PNG si possono usare le funzioni load e save del
modulo immagini.py.

ATTENZIONE: sono vietate tutte le librerie aggiuntive.

ATTENZIONE: assicuratevi che questo file sia in ecoding UTF8 (ad esempio editandolo in Spyder o Notepad++)

'''

import immagini

def es1(fname, colore, fnameout):
    # inserite qui il vostro codice
    img = immagini.load(fname)

    area_max = []

    h =len(img)-1
    l = len(img[0])-1

    c2 = (255-colore[0],255-colore[1],255-colore[2])


    for i in range(h+1):

        if colore in img[i]:

            for i2 in range(l+1):
                if img[i][i2] == colore:
                    area_trovata = trova_area(img,i,i2,colore,c2,h,l)
                    if len(area_trovata) > len(area_max):
                        area_max = area_trovata[:]

        img[i] = [c2]*(l+1)

    for i in area_max:
        img[i[0]][i[1]] = colore

    immagini.save(img,fnameout)
    return len(area_max)



def trova_area(img,i,i2,colore,c2,h,l):

    img[i][i2] = c2
    coda = [(i,i2)]
    area = [(i,i2)]

    while len(coda) > 0:
        i = coda[0][0]
        i2 = coda[0][1]
        area_temp = controlla_vicini(img,i,i2,colore,c2,h,l)
        coda+= area_temp
        area+= area_temp
        coda = coda[1:]

    return area

def controlla_vicini(img,i,i2,colore,c2,h,l):
    ls_vicini = []


    if i > 0 and img[i-1][i2] == colore:
        ls_vicini+= [(i-1,i2)]
        img[i-1][i2] = c2

    if i2 > 0 and img[i][i2-1] == colore:
        ls_vicini+= [(i,i2-1)]
        img[i][i2-1] = c2

    if i < h and img[i+1][i2] == colore:
        ls_vicini+= [(i+1,i2)]
        img[i+1][i2] = c2

    if i2 < l and img[i][i2+1] == colore:
        ls_vicini+= [(i,i2+1)]
        img[i][i2+1] = c2

    return ls_vicini

