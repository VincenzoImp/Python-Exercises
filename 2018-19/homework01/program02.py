'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x 
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti 
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere 
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche' 
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''

'''
ALGORITHM
Come prima cosa importo la libreria per utilizzare la radice quadrata, utile per migliorare l'efficenza della ricerca dei divisori. Poi definisco una funzione per questa ricerca, dove dato
un numero in ingresso, creo un insieme con i suoi divisori (ed esso compreso), da restituire in output. Parlando della funzione principale creo una copia dell'insieme dato e scorro tutte le
lampadine dall'ultima alla prima e controllo se queste sono nell'insieme. Se così è aggiungo la lampadina alla lista in uscita e richiamo la funzione dei divisori inviandogli come numero
quello della lampadina, cosi ottengo un insieme con tutte le lampadine di cui devo cambiare lo stato. Quindi i numeri nella lista divisori che non sono nell'insieme vengono aggiunti e quelli
che ci sono già vengono tolti. Infine restituisco la lista di uscita ordinata.
'''

import math                                                             #importo la libreria math per usufruire della radice quadrata

def ricerca_divisori ( numero ) :                                       #dichiarazione funzione 'ricerca_divisori' che permette di trovare i divisori di un numero in input
    divisori = set ( )                                                  #inizzializzazione insieme 'divisori'
    for indice in range ( 1 , int ( math.sqrt ( numero ) + 1 ) ) :      #iterazione da 1 fino all'intero della radice quadrata del numero di cui trovare i divisori compreso
        if numero % indice == 0 :                                       #controllo se la divisione del numero in input con il valore iterato da resto zero
            divisori |= { indice , numero / indice }                    #se è così aggiungo all'insieme 'divisori' il valore iterato e il quoziente della divisione tra numero in input e il valore iterato
    return divisori                                                     #ritorno l'insieme 'divisori'

def es2 ( N , ins ) :                                                   #dichiarazione funzione 'es2'
    insieme_lampadine_accese = ins.copy ( )                             #generazione di 'insieme_lampadine_accese' che è una copia dell'insieme in input
    lista_output = [ ]                                                  #inizzializzazione 'lista_output'
    for lampadina in range ( N , 0 , - 1 ) :                            #iterazione da 'N' fino a uno compreso
        if lampadina not in insieme_lampadine_accese :                  #controllo se il vaolre iterato non è presente in 'insieme_lampadine_accese'
            lista_output.append ( lampadina )                           #se è così aggiungo il valore iterato a 'lista_output'
            insieme_lampadine_accese ^= ricerca_divisori ( lampadina )  #e di conseguenza 'insieme_lampadine_accese' sarà lo XOR tra se stesso e l'insieme 'divisori' del valore iterato
    return list ( sorted ( lista_output ) )                             #ritorno 'lista_output' ordinata
