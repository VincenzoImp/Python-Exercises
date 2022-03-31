''' 
Sono stati appena corretti i compiti di N studenti ed in una lista sono riportati
i voti ottenuti dai vari studenti.
Sia C il voto massimo assegnato (questo significa che i voti sono interi da 0 a C compresi).
Bisona stabilire una soglia tra 0 e C a partire dalla quale gli studenti verranno ammessi all'orale.
(ovvero vengono ammessi tutti quelli con voti maggiori o uguali alla soglia)
Non volendo essere ne' troppo severo ne' troppo generoso nella valutazione, il docente, prima di scegliere la soglia,
decide di generare per ognuna delle possibili C+1 soglie (da 0 a C compreso)
il numero di studenti che verrebbero ammessi all'orale per quella soglia.
Definire una funzione es1(voti) che, data lista non vuota 'voti'  con i voti degli studenti,
restituisce la lista di C+1 interi dove in posizione i si trova  il numero di studenti ammessi
all'orale nel caso la soglia venga fissata al valore i.
ATTENZIONE: la lista ls dei voti al termine della funzione NON DEVE risultare modificata.
Ad esempio per voti=[7,5,8,3,7,2,9] la funzione es2 restituisce la lista
[7, 7, 7, 6, 5, 5, 4, 4, 2, 1]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''

'''
ALGORITHM
Nella funzione principale genero un dizionario le cui chiavi sono tutti i numeri dal massimo numero nella lista voti fino a zero compreso, e i valori tutti zero, che rappresentano il numero
di volte che ho trovato la chiave corrispondente nella lista voti. Quindi aggiungo un'unità al valore della chiave che appare scorrendo numero per numero la lista, così che alla fine avremo
il dizionario dove per ogni chiave corrisponderà il numero di volte che essa si è presentata nella lista. Infine ritorno una lista capovolta generata da una funzione esterna che dato il
dizionario è in grado di dire quante persone passano per ogni soglia. Questo è possibile perchè il dizionario resta nell'ordine di quando abbiamo inserito le chiavi e valori, e lo abbiamo
fatto dal massimo della lista voti fino a zero. Questo è utilissimo perchè possiamo generare la lista di uscita senza controlli siccome chi ha preso ad esempio nove sarà promosso per
qualsiasi soglia al di sotto e quindi anche per le restanti chiavi che seguono. Utilissimo quindi in questo caso è il totalizzatore che viene usato nell'apposita funzione per generare la
lista di uscita. In questa funzione vengono iterati i valori del dizionario e viene aggiunto alla lista il risultato dei valori totalizzati fino a quel momento.
'''

def genera_lista_output ( dizionario ) :                                            #dichiarazione funzione 'genera_lista_output'
    lista_output = [ ]                                                              #inizzializzazione 'lista_output'
    totalizzatore = 0                                                               #inizzializzazione 'totalizzatore'
    for valore in dizionario.values ( ) :                                           #iterazione dei valori del 'dizionario'
        totalizzatore += valore                                                     #totalizzazione dei valori tramite il 'totalizzatore'
        lista_output.append ( totalizzatore )                                       #aggiungere alla 'lista_output' 'totalizzatore'
    return lista_output                                                             #ritornare 'lista_output'

def es1 ( voti ) :                                                                  #dichiarazione funzione 'es1'
    dizionario = { chiave : 0 for chiave in range ( max ( voti ) , - 1 , - 1 ) }    #dichiarazione 'dizionario' con chiavi dal massimo della lista 'voti' fino a zero e valori uguali a zero
    for voto in voti :                                                              #iterazione della lista 'voti'
        dizionario [ voto ] += 1                                                    #aggiunta di un'unità al valore della chiave iterata
    return list ( reversed ( genera_lista_output ( dizionario ) ) )                 #ritornare la lista capovolta ottenuta dal richiamo della funzione 'genera_lista_output'
