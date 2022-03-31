r'''
Abbiamo in un file JSON una lista di coppie: (nodo1, nodo2) in cui appaiono i nomi dei nodi (stringhe o interi)
di una foresta (un insieme di alberi).
Ciascuna coppia descrive una relazione figlio -> padre.
Un figlio appare sempre zero o una volta come primo elemento di una qualche coppia
e può apparire 0, 1, o più volte come secondo elemento della coppia.

Potete assumere che tutti i nodi della foresta siano dello stesso tipo (interi o stringhe) in modo che siano confrontabili.

Potete assumere che non siano mai presenti cicli e quindi che disegnando tutti i nodi e
collegandoli con le relazioni figlio->padre si ottenga un insieme di alberi (una foresta).

Esempio: se le coppie sono ('3','2'), ('2', '1'), ('4', '1'), ('6', '5'), ('8', '7'), ('9', '7'), ('12', '10'), ('11', '8'), ('10', '7')
La foresta corrispondente è

           1        5        7
         /  \       |       /|\ 
        2   4       6      8 9 10
       /                   |    |
      3                   11    12

Di ciascun albero della foresta bisogna trovare:
    - la radice
    - l'altezza
    - l'insieme delle foglie

Implementate la funzione es1(fileJsonInput, fileJsonOutput) che (se necessario usando altre funzioni, oggetti o metodi):
    - legge dal file fileJsonInput in formato JSON la lista di coppie di nomi di nodi
    - costruisce la foresta di alberi usando se volete delle classi per definire i nodi
    - calcola per ciascun albero della foresta i tre valori: (radice, altezza, insieme delle foglie)
    - scrive in formato JSON nel file fileJsonOutput un dizionario in cui:
        - le chiavi sono i nomi delle radici degli alberi individuati (delle stringhe)
        - i valori sono una coppia (profondità, lista dei nomi delle foglie)
            in cui la lista dei nomi delle foglie è ordinata in ordine crescente (alfabetico se stringhe, numerico se interi)
    - alla fine la funzione deve restituire il numero di alberi scovati nella foresta

Esempio, se il file 'es1_f1.json' contiene la lista precedente di coppie, es1('es1_f1.json', 'es1_test1.json')
la funzione produrrà un file 'es1_test1.json' contenente il dizionario:
{
    "5": (2, ["6"]),
    "7": (3, ["11", "12", "9"],
    "1": (3, ["3", "4"])
}

Il TIMEOUT per ciascun test è di 2 secondi per ciascun test.

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe

ATTENZIONE: Non potete usare altre librerie a parte json.

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

'''

'''
ALGORITHM
Come prima cosa apro con json il file in input che è una lista di liste e lo associo ad una variabile. itero ogni lista della variabile e genero l'oggetto nodo per ogni elemento delle liste. Aggiungo questi oggetti ad un dizionario che visualizza il loro nome
(ovvero la stringa contenente il numero che li rappresenta) come chiave e la loro lista figli e il loro padre come valori. le foglie dell'albero avranno la lista figli vuota e le radici avranno None come padre. adesso per ogni radice chiamo la funzione ricorsiva
che dalla radice ottiene i suoi figli e per ogni figlio visualizza la lista figli di ognuno e per ognuno di questi richiama la funzione ricorsiva. ogni chiamata incremento di uno l'altezza e se arrivo ad una foglia salvo la foglia e l'altezza a cui sono arrivato.
alla fine di tutte le ricorsioni mi ritroverò con la lista delle foglie di quella radice e la lista delle altezze di ogni foglia così compilo il dizionario che devo produrre in uscita che per ogni radice ha l'altezza dell'albero e la sua lista foglie (l'altezza
dell'albero equivale all'altezza della foglia più alta). Alla fine carico il dizionario prodotto nel file di output e ritorno il totale delle radici.
'''

import json                                                                                     #importo 'json'

class Nodo :                                                                                    #inizzializzo la classe 'Nodo'
    def __init__ ( self , p = None ) :                                                          #inizzializzo la funzione '__init__'
        self . figli = set ( )                                                                  #inizzializzo il metodo 'figli' con un insieme vuoto
        self . padre = p                                                                        #inizzializzo il metodo 'padre' con 'p'

def genera_dati_1 ( fileJsonInput , dizionario ) :                                              #inizzializzo la funzione 'genera_dati_1'
    with open ( fileJsonInput , encoding = 'utf8' ) as f :                                      #apro 'fileJsonInput' come 'f'
        file = json . load ( f )                                                                #associo il contenuto di 'f' alla variabile 'file' con 'json'
    for lista in file :                                                                         #itero ogni elemento di 'file' come 'lista'
        n = Nodo ( lista [ 1 ] )                                                                #genero per ogni secondo elemento di 'lista', 'n' che è un oggetto 'Nodo'
        dizionario [ lista [ 0 ] ] = [ n , n . padre , n . figli ]                              #in 'dizionario' aggiungo come chiave il primo elemento di 'lista' e come valore 'n', il padre di 'n' e il suo insieme figli
    return genera_dati_2 ( dizionario , file )                                                  #ritorno la funzione 'genera_dati_2'

def genera_dati_2 ( dizionario , file ) :                                                       #inizzializzo la funzione 'genera_dati_2'
    for lista in file :                                                                         #itero ogni elemento di 'file' come 'lista'
        if lista[ 1 ] in dizionario . keys ( ) :                                                #se il secondo elemento di 'lista' è una chiave di 'dizionario'
            dizionario [ lista [ 1 ] ] [ 0 ] . figli . add ( lista [ 0 ] )                      #allora aggiungo all'insieme figli dell'elemento il primo elemento di 'lista'
        else :                                                                                  #altrimenti
            n = Nodo ( )                                                                        #genero l'oggetto nodo 'n'
            n . figli . add ( lista [ 0 ] )                                                     #aggiungo all'insieme dei figli di 'n' il primo elemento di 'lista'
            dizionario [ lista [ 1 ] ] = [ n , n . padre , n . figli ]                          #in 'dizionario' aggiungo come chiave il primo elemento di 'lista' e come valore 'n', il padre di 'n' e il suo insieme figli
    return genera_alberi ( dizionario , { } )                                                   #ritorno la funzione 'genera_alberi'

def genera_alberi ( dizionario , alberi , tot_alberi = 0 ) :                                    #inizzializzo la funzione 'genera_alberi'
    for nodo , valore in dizionario . items ( ) :                                               #itero ogni chiave e valore di 'dizionario' come 'nodo' e 'valore'
        if valore [ 1 ] == None :                                                               #se il padre di 'nodo' è uguale a 'None'
            alberi [ nodo ] = [ 0 , set ( ) ]                                                   #allora in 'alberi' aggiungo la chiave 'nodo' che ha come valore '0' e un insieme vuoto che indicano altezza e insieme foglie
            tot_alberi += 1                                                                     #incremento di 1 'tot_alberi'
    return alberi , tot_alberi , dizionario                                                     #ritorno 'alberi', 'tot_alberi', 'dizionario'

def ricorsione ( nodo , dizionario , contatore , foglie , ins ) :                               #inizializzo la funzione 'ricorsione'
    if dizionario [ nodo ] [ 2 ] == set ( ) :                                                   #se la lista di figli di 'nodo' in 'dizionario' è un insieme vuoto
        foglie . add ( nodo )                                                                   #allora aggiungo 'nodo' all'insieme 'foglie'
        ins . add ( contatore )                                                                 #e aggiungo contatore all'insieme 'ins'
        return ins , foglie                                                                     #ritorno 'ins', 'foglie'
    for n in dizionario [ nodo ] [ 2 ] :                                                        #itero ogni elemento dell'insieme figli di 'nodo' in 'dizionario'
        ins , foglie = ricorsione ( n , dizionario , contatore + 1 , foglie , ins )             #chiamo la funzione 'ricorsione' che ritorna 'ins', 'foglie'
    return ins , foglie                                                                         #ritorno 'ins', 'foglie'

def es1 ( fileJsonInput , fileJsonOutput ) :                                                    #inizzializzo la funzione 'es1'
    alberi , tot_alberi , dizionario = genera_dati_1 ( fileJsonInput , { } )                    #chiamo la funzione 'genera_dati_1' che ritorna 'alberi', 'tot_alberi', 'dizionario'
    for radice in alberi . keys ( ) :                                                           #itero ogni chiave di 'alberi' come 'radice'
        ins , foglie = ricorsione ( radice , dizionario , 1 , set ( ) , set ( ) )               #chiamo la funzione 'ricorsione' che ritorna 'ins', 'foglie'
        alberi [ radice ] = ( max ( ins ) , sorted ( list ( foglie ) ) )                        #in 'alberi' aggiungo la chiave 'radice' che ha come valore il vaolre massimo di 'ins' e la lista ordinata di 'foglie'
    with open ( fileJsonOutput , 'w' ) as f :                                                   #apro 'fileJsonOutput' come 'f'
        json . dump ( alberi , f )                                                              #carico 'alberi' in 'f' con 'json'
    return tot_alberi                                                                           #ritorno 'tot_alberi'
