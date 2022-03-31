'''
I messaggi scambiati all'interno di un forum sono stati sottoposti ad uno studio.
Dai  vari post  sono state estrapolate parole significative e questi dati sono stati poi
raccolti in un  file di testo.
Nel file, l'inizio di ciascun post e' marcato da una linea che contiene  la stringa
"<POST>" e un intero utilizzato come identificativo del post (che nel seguito dovete lasciare come stringa).
la stringa e l'identificativo possono essere preceduti e seguiti da un numero arbitrario (anche 0) di spazi.
Le parole estrapolate  dal  post sono  nelle linee successive (zero  o piu' parole per 
linea) fino alla linea che marca il prossimo post 
o la fine del file.
Come esempio si veda il file "fp1.txt".
  
Per ognuna delle parole estrapolate si vogliono ora ricavare le seguenti informazioni: 
I1) Il numero totale di occorrenze della parola nei post,
I2) il numero di post in cui la parola compare,
I3) la coppia (occorrenze, post) dove nella seconda coordinata si ha l'identificativo del post 
in cui la parola e' comparsa piu' spesso e nella prima il numero di volte che vi e' comparsa,
(nel caso di  diversi post con pari numero massimo di occorrenze della parola va considerato 
il post con l'identificativo minore in ordine lessicografico).
Bisogna costruire una tabella avente una riga per ognuna delle differenti parole
utilizzate nel forum. La tabella deve avere 4 colonne  
In una colonna  comparira' la parola e nelle altre tre  le informazioni I1), I2) e I3) dette prima.
Le righe della colonna devono essere ordinate rispetto all'informazione I1) decrescente, a parita' 
del valore I1 vanno ordinate rispetto  alla cardinalita' decrescente dell'insieme degli itentificativi 
ed a parita', rispetto all'ordine lessicografico delle parole. 

Scrivere una funzione es2(fposts) che prende in input  il
percorso del file di testo contenente le estrapolazioni dei post del forum
e restituisce la tabella.
La tabella va restituita sotto forma di lista di dizionari dove
ciascun dizionario ha 4 chiavi: 'parola', 'I1','I2' e 'I3' e ad ogni chiave e'
associata la relativa informazione attinente la parola.
Ad esempio per il file di testo fp1.txt la funzione restituira' la lista:
[{'I1': 6, 'I2': 3, 'I3': (3, '30'), 'parola': 'hw1'},
 {'I1': 3, 'I2': 2, 'I3': (2, '30'), 'parola': 'python'},
 {'I1': 2, 'I2': 1, 'I3': (2,  '1'), 'parola': 'hw2'},
 {'I1': 1, 'I2': 1, 'I3': (1, '21'), 'parola': '30'},
 {'I1': 1, 'I2': 1, 'I3': (1, '30'), 'parola': 'monti'},
 {'I1': 1, 'I2': 1, 'I3': (1,  '1'), 'parola': 'spognardi'},
 {'I1': 1, 'I2': 1, 'I3': (1, '21'), 'parola': 'sterbini'}
 ]

NOTA: il timeout previsto per questo esercizio è di 3 secondi per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)
'''

'''
ALGORITHM
Nel programma leggo tutto il testo e genero una lista con tutte le parole che compaiono nel testo. Scorro ognuna di queste parole e se trovo un '<post>' saprò che quella subito dopo
sarà una chiave del mio dizionario e le parole di dopo fino a un nuovo '<post>' saranno tutte parole appartenenti a quel post. Infatti per ogni post creo un chiave di un dizionario
che prende l'id del post e il valore di essa è un dizionario che ha per chiavi tutte le parole in quel post e come valori quante volte queste parole vengono trovate nel post, cosi da
risolvere la seconda richiesta del problema. Contemporaneamente risolvo tutte le altre richieste, con un altro dizionario, che creo nello stesso ciclo che scorre tutte le parole della
lista, che ha per chiavi tutte le parole che compariranno in ogni post e come valori queste chiavi hanno una lista con quattro elementi, che servono a risolvere tutti i punti richiesti
dal problema tranne il numero due che viene risolto dall'altro dizionario. In fine non devo far altro che creare la lista di uscita appendendo ad essa un dizionario specifico per ogni
parola che fa da chiave e come valore la lista dei punti del problema da risolvere.
'''

from collections import defaultdict                                                                             #import 'defaultdict' da 'collections'

def genera_dati ( fposts ) :                                                                                    #eseguo funzione genera_dati
    with open ( fposts , 'r' , encoding = 'utf-8' ) as f :                                                      #apro 'fposts' in lettura e lo associo ad 'f'
        testo = f . read ( )                                                                                    #associo a 'testo' la lettura di tutto il file
    testo = testo . replace ( '<post>' , '<post>\n' ) . split ( )                                               #aggiungo uno spazio dopo '<post>' e faccio diventare 'testo' una lista con tutte le sue parole
    dizionario_parole = defaultdict ( lambda : [ 0 , 0 , 0 , '' ] )                                             #genero 'dizionario_parole' con valori di default
    return genera_dizionari ( testo , { } , dizionario_parole )                                                 #chiamo la funzione 'genera_dizionari' che genera i dizionari che risolvono le richieste del testo

def genera_dizionari ( testo , dizionario , dizionario_parole , boole = False , chiave = '' ) :                 #eseguo funzione 'genera_dizionari'
    for parola in testo :                                                                                       #apro un ciclo che legge ogni 'parola' del 'testo'
        if parola == '<post>' :                                                                                 #se la parola è '<post>'
            boole = True                                                                                        #allora 'boole' diventa True
            if dizionario != { } :                                                                              #e di conseguenza se 'dizionario' non è vuoto
                dizionario_parole = genera_I3 ( chiave , dizionario , dizionario_parole )                       #allora chiamo la funzione 'genera_I3' che risolve la richiesta I3 per ogni parola del post che ho appena terminato
        elif boole :                                                                                            #altrimenti se 'boole' è già True
            dizionario [ parola ] = { }                                                                         #creo una chiave in 'dizionario' che chiamo 'parola' e le associo un dizionario vuoto
            chiave = parola                                                                                     #inizializzo 'chiave' come 'parola'
            boole = False                                                                                       #boole torna False
        else:                                                                                                   #altrimenti
            dizionario_parole [ parola ] [ 0 ] += 1                                                             #incremento di uno il primo elemento della lista nella chiave 'parola' in 'dizionario_parole'
            if parola in dizionario [ chiave ] . keys ( ) :                                                     #se 'parola' è una chiave di 'dizionario'
                dizionario [ chiave ] [ parola ] += 1                                                           #allora incremento di 1 il valore della chiave 'parola', nel dizionario che è il valore della chiave 'chiave'
            else:                                                                                               #altrimenti
                dizionario [ chiave ] [ parola ] = 1                                                            #creo questa chiave e gli do come valore 1
                controllo = True                                                                                #inizializzo 'controllo' come True
            if controllo :                                                                                      #se 'controllo' è True
                dizionario_parole [ parola ] [ 1 ] += 1                                                         #incremento di 1 il secondo valore della lista della chiave 'parola'
                controllo = False                                                                               #inizializzo 'controllo' come False
    return chiave , dizionario , dizionario_parole                                                              #ritorno 'chiave', 'dizionario' e 'dizionario_parole'

def genera_I3 ( chiave , dizionario , dizionario_parole ) :                                                     #eseguo la funzione 'genera_I3'
    for key, values in dizionario [ chiave ] . items ( ) :                                                      #inizio un ciclo che iteri i 'values' e le 'key' del dizionario che ha per chiave 'chiave' che è stata passata alla funzione
        if values > dizionario_parole [ key ] [ 2 ] :                                                           #se 'values' è maggiore del terzo elemento nella lista della chiave 'key' nel 'dizionario_parole'
            dizionario_parole [ key ] [ 2 ] = values                                                            #allora sostituiamo quel valore con 'values'
            dizionario_parole [ key ] [ 3 ] = chiave                                                            #e il valore successivo della lista con 'chiave'
        elif values == dizionario_parole [ key ] [ 2 ] :                                                        #altrimenti se questo valore è uguale a 'values'
            if chiave < dizionario_parole [ key ] [ 3 ] :                                                       #se 'chiave' è minore del valore successivo nella lista
                dizionario_parole [ key ] [ 3 ] = chiave                                                        #allora sostituiamo quest'ultimo con 'chiave'
    return dizionario_parole                                                                                    #ritorno dizionario_parole

def genera_uscita ( dizionario_parole ) :                                                                       #eseguo la funzione 'genera_uscita'
    lista_uscita = [ { 'I1' : valore [ 0 ] , 'I2' : valore [ 1 ] ,                                              #creo 'lista_uscita' che è composta da dei dizionari
                    'I3' : tuple ( valore [ 2 : ] ) , 'parola' : parola }                                       #che contengono informazioni per ciascun elemento di 'dizionario_parole'
                    for parola , valore in dizionario_parole . items ( ) ]                                      #tutto attraverso un ciclo di for
    return sorted ( lista_uscita , key = lambda x : ( - x [ 'I1' ] , - x [ 'I2' ] , x [ 'parola' ] ) )          #ritorno 'lista_uscita' ordinata in base alla funzione lambda

def es2 ( fposts ) :                                                                                            #eseguo la funzione 'es2'
    chiave , dizionario , dizionario_parole = genera_dati ( fposts )                                            #richiamo la funzione 'genera_dati' per ottenere 'chiave', 'dizionario' e 'dizionario_parole'
    dizionario_parole = genera_I3 ( chiave , dizionario , dizionario_parole )                                   #richiamo la funzione 'genera_I3' per aggiornare 'dizionario_parole'
    return genera_uscita ( dizionario_parole )                                                                  #ritorno la chiamata della funzione 'genera_uscita'
