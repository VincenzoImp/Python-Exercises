
''' Abbiamo una sequenza circolare con i primi  n interi  (il numero 1 e' 
    seguito dal numero 2 che e' seguito dal numero 3 ..che e' seguito dal numero n che e' 
    seguito dal numero 1).  Uno  dopo l'altro alcuni numeri vanno eliminati dalla sequenza 
    fino a che non ne rimangono esattamente k con k<n.  
    I numeri vengono via via scartati in base alla seguente regola: 
    Dato un intero strettamente positivo c, a partire dal numero 1 si conta in senso orario 
    fino al c-mo, viene eliminato il numero seguente. 
    A partire dal numero alla destra del numero appena cancellato  si conta nuovamente in 
    senso orario per c posizioni e si elimina il numero seguente. 
    Si prosegue in questo modo spostandosi sempre verso destra di c posizioni alla ricerca 
    del nuovo numero da eliminare finche' non ne rimangono in sequenza esattamente k.
    
    Definire una funzione es1(n,c,k) che dati i tre interi n,c e k con k<n
    restituisce una lista di k interi. 
    I k interi della lista  sono  nell'ordine i k interi
     rimasti nella sequenza  al termine  delle eliminazioni.
    Ad esempio per n=9, c=5 e k=2 nell'ordine verranno eliminati i seguenti 7 numeri: 
    6,3,1,9,2,5,4
    e la funzione restituira' la lista [7,8].
    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: è proibito l'uso di altre librerie

    ATTENZIONE: sono vietate le variabili globali

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''

def es1(n,c,k):
    lista = [i for i in range(1,n+1)]
    a = 0

    while k < n:
        a += c
        if a >= n: a = a % n
        del lista[a]
        n = len(lista)

    return lista

