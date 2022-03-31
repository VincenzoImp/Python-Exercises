'''
Una regione e' stata suddivisa concettualmente in quadrati adiacenti.
Ogni  quadrato della griglia risultante e' univocamente identificato da una 
coppia di interi positivi (x,y) ad indicare che il quadrato appartiene alla x-ma colonna 
e y-ma riga della griglia, CON IL QUADRATO (1,1) SITUATO IN BASSO A SINISTRA (ATTENZIONE!).

Disponiamo di robottini in grado di muoversi tra i quadrati della griglia ma solo in 
orizzontale (da sinistra verso destra) e verticale (dal basso verso l'alto). 
Uno spostamento del robottino viene indicato da un intero A (positivo o negativo). 
Se il robottino si trova nel quadratino di coordinate (x,y):
-  l'intero +A positivo indica uno spostamento in verticale fino al quadrato (x,y+|A|)
-  l'intero -A negativo indica uno spostamento in orizzontale della griglia fino al quadrato (x+|A|,y)
Una sequenza di interi (positivi o negativi) indica dunque un percorso del robottino.
Ad esempio se il robottino e' nel quadrato (1,1), la sequenza 5,-2,-2,2,-4 lo porta nel quadrato (9,8). 

Ci vengono forniti un insieme I di quadrati della griglia indicati dalle loro coordinate (x,y)
e due percorsi di due robottini, che partono entrambi dal quadrato (1,1) e terminano in uno stesso quadrato.
Il primo percorso comincia con un numero positivo, il secondo con un numero negativo 
e il quadrato iniziale e quello finale sono gli unici quadrati che i due percorsi hanno in comune.
Vogliamo sapere quanti dei quadrati dell'insieme I ricadono nella zona circoscritta dai due percorsi. 
Nota che un quadrato (x,y) e' nella zona circoscritta se i due robottini  
attraversano la colonna x della griglia e i quadrati di quella colonna attraversati
dai due robottini  sono rispettivamente (x,y1) ed (x,y2) con y1>y>y2).
(quindi i quadrati di I che si trovano sui percorsi NON vanno contati)

Ad esempio per per l'insieme 
    I={ (11, 2), (8,5), (4,6), (7,1), (2,9), (3,4), (7,6), (6,6), (5,2)}
e i due percorsi: 
    p1 =  5 -2 -2 2 -4
    p2 = -3  2 -5 5
Ovvero (indicando con '+' i movimenti con A positivo, con '-' quelli con A negativo, 
        con '*' i quadrati di I, con 'o' l'origine e con 'X' la destinazione)
    y
    ^
  11|
  10|
   9| *
   8|    +---X
   7|    +   +
   6|+--*-** +
   5|+      *+
   4|+ *     +
   3|+  +-----
   2|+  +*     *
   1|o---  *
    |_______________________>x
              11111111112
     12345678901234567890

la risposta e' 4 perche' gli unici quadrati che ricadono nella zona circoscritta sono
{(3, 4), (6, 6), (7, 6), (8, 5)}

Scrivere una funzione es3(fmappa) che prende in input  il percorso del file di testo contenente 
i percorsi dei due robottini e l'insieme dei quadrati I e restituisce il numero di quadrati 
dell'insieme I che risultano circoscritti dai due percorsi.

I dati sono organizzati  nel file come segue:
- una serie di righe vuote
- il percorso del primo robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- il percorso del secondo  robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- una sequenza di coppie (x,y) che indicano i quadrati dell'insieme (le coppie separate 
 da virgole e spazi ed in una o piu' righe consecutive)
- una serie di righe vuote

Si veda ad esempio il file mp1.txt

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)
'''

'''
ALGORITHM
Il codice mediante dei controlli appena trova righe vuote le prossime non vuote verranno aggiunte in una lista per gli spostamenti del primo robot. Successivamente appena trova righe
vuote le prossime non vuote saranno appese alla lista dei movimenti del robot 2 e di nuovo se si incontrano altre righe vuote le prossime non vuote verranno usate per generare un
dizionario che ha per chiavi le ascisse e per valori le ordinate. Poi grazie alla lista del robot 1 genero il dizionario delle cordinate indispensabili per il confronto del robot 1 e
analogamente faccio per il robot 2. Infine itero per ogni chiave valore del dizionario delle coordinate da confrontare e le coordinate con la stessa chiave verranno confrontate le y con
quelle di robot 1 e robot 2 con la stessa chiave e contate solo quelle che sono comprese.
'''

def genera_coordinate_robot1 ( movimenti_robot1 , coordinate_robot1 , x = 1 , y = 1 ) :                                                                             #eseguo la funzione 'genera_coordinate_robot1'
    for indice in movimenti_robot1 :                                                                                                                                #inizio un ciclo che itera ogni elemento in 'movimenti_robot1'
        indice = int ( indice )                                                                                                                                     #inizializzare il valore iterato come un intero
        if indice < 0 :                                                                                                                                             #se questo valore è minore di zero
            for _ in range ( - indice ) :                                                                                                                           #inizio un ciclo che va da zero fino a questo valore
                x += 1                                                                                                                                              #incremento la 'x' di uno
                coordinate_robot1 [ x ] = y                                                                                                                         #aggiungo la chiave 'x' in 'coordinate_robot1' con 'y' come valore
        elif indice > 0 :                                                                                                                                           #altrimenti se il valore iterato è maggiore di zero
            y += indice                                                                                                                                             #aggiorno 'y' incrementandogli 'indice'
    del coordinate_robot1 [ x ]                                                                                                                                     #elimino dal dizionario l'ultima chiave inserita
    return coordinate_robot1                                                                                                                                        #ritorno 'coordinate_robot1'

def genera_coordinate_robot2 ( movimenti_robot2 , coordinate_robot2 , x = 1 , y = 1 ) :                                                                             #eseguo 'genera_coordinate_robot2'
    for indice in movimenti_robot2:                                                                                                                                 #inizio un ciclo che itera ogni elemento in 'movimenti_robot2'
        indice = int ( indice )                                                                                                                                     #inizializzare il valore iterato come un intero
        if indice < 0 :                                                                                                                                             #se questo valore è minore di zero
            for _ in range ( - indice ) :                                                                                                                           #inizio un ciclo che va da zero fino a questo valore
                x += 1                                                                                                                                              #incremento la 'x' di uno
                coordinate_robot2 [ x ] = y                                                                                                                         #aggiungo la chiave 'x' in 'coordinate_robot2' con 'y' come valore
        elif indice > 0 :                                                                                                                                           #altrimenti se il valore iterato è maggiore di zero
            y += indice                                                                                                                                             #aggiorno 'y' incrementandogli 'indice'
            coordinate_robot2 [ x ] = y                                                                                                                             #aggiungo la chiave 'x' in 'coordinate_robot2' con 'y' come valore
    del coordinate_robot2 [ x ]                                                                                                                                     #elimino dal dizionario l'ultima chiave inserita
    return coordinate_robot2                                                                                                                                        #ritorno 'coordinate_robot2'

def genera_coordinate_confronto ( dati_confronto_grezzi , coordinate_confronto ) :                                                                                  #eseguo 'genera_coordinate_confronto'
    for indice in range( 0 , len ( dati_confronto_grezzi ) , 2 ) :                                                                                                  #inizio un ciclo che itera un indice da zero fino alla lunghezza di 'dati_confronto_grezzi'
        if int ( dati_confronto_grezzi [ int ( indice ) ] ) in coordinate_confronto . keys ( ) :                                                                    #se l'elemento in posizione 'indice' che è il valore iterato è una chiave di 'coordinate_confronto'
            coordinate_confronto [ int ( dati_confronto_grezzi [ int ( indice ) ] ) ] . append ( int ( dati_confronto_grezzi [ int ( indice ) + 1 ] ) )             #allora appendo il valore nella posizione successiva nella lista di quella chiave
        else:                                                                                                                                                       #altrimenti
            coordinate_confronto [ int ( dati_confronto_grezzi [ int ( indice ) ] ) ] = [ ]                                                                         #creo la chiave e come valore gli metto una lista vuota
            coordinate_confronto [ int ( dati_confronto_grezzi [ int ( indice ) ] ) ] . append ( int ( dati_confronto_grezzi [ int ( indice ) + 1 ] ) )             #aggiungo a quella lista il valore alla posizione successiva di quello individuato grazie alla iterazione
    return coordinate_confronto                                                                                                                                     #ritorno 'coordinate_confronto'

def genera_dati ( file , movimenti_robot1 , movimenti_robot2 , dati_confronto_grezzi , passaggio ) :                                                                #eseguo genera_dati
    for elemento in file :                                                                                                                                          #inizio un ciclo che iteri ogni 'elemento' del file
        if elemento != '\n' and passaggio == 0 :                                                                                                                    #se 'elemento' è diverso da '\n' e 'passaggio' è uguale a zero
            movimenti_robot1 += elemento . split ( )                                                                                                                #incremento 'movimenti_robot1' con la lista generata dallo split di 'elemento'
        elif elemento == '\n' and movimenti_robot1 != [ ] and movimenti_robot2 == [ ] :                                                                             #altrimenti se 'movimenti_robot1' non è vuota e 'movimenti_robot2' è vuota
            passaggio = 1                                                                                                                                           #allora inizzializzo 'passaggio' uguale a 1
        elif elemento != '\n' and passaggio == 1 :                                                                                                                  #altrimenti se 'elemento' non è '\n' e 'passaggio' è 1
            movimenti_robot2 += elemento . split ( )                                                                                                                #allora incremento 'movimenti_robot2' con la lista generata dallo split di 'elemento'
        elif elemento == '\n' and passaggio == 1 :                                                                                                                  #altrimenti se 'elemento' è '\n' e 'passaggio' è 1
            passaggio = 2                                                                                                                                           #allora 'passaggio' diventa 2
        elif elemento != '\n' and passaggio == 2 :                                                                                                                  #altrimenti se 'elemento' non è '\n' e 'passaggio' è 2
            dati_confronto_grezzi += elemento . replace ( '(' , ' ' ) . replace ( ')' , ' ' ) . replace ( ',' , ' ' ) . split ( )                                   #allora incremento 'dati_confronto_grezzi' con la lista generata dallo split di 'elemento' rimuovento dei caratteri che non servono
    return movimenti_robot1 , movimenti_robot2 , dati_confronto_grezzi                                                                                              #'ritorno movimenti_robot1' , 'movimenti_robot2' , 'dati_confronto_grezzi'

def uscita ( coordinate_robot1 , coordinate_robot2 , coordinate_confronto , uscita ) :                                                                              #eseguo la funzione 'uscita'
    for chiave , valore in coordinate_confronto . items ( ) :                                                                                                       #inizio un ciclo che itera le chiavi e i valori di 'coordinate_confronto'
        if chiave in coordinate_robot1 . keys ( ) :                                                                                                                 #se la chiave iterata è anche una chiave di 'coordinate_robot1'
            for indice in valore :                                                                                                                                  #allora inizio un ciclo che itera il valore iterato
                if coordinate_robot2 [ chiave ] < indice < coordinate_robot1 [ chiave ] :                                                                           #se il valore iterato è compreso tra i valori della chiave iterata nei dizionari 'coordinate_robot1' e 'coordinate_robot2'
                    uscita += 1                                                                                                                                     #incremento di uno 'uscita'
    return uscita                                                                                                                                                   #ritorno 'uscita'

def es3 ( fmappa ) :                                                                                                                                                #eseguo la funzione 'es3'
    with open ( fmappa , 'r' , encoding = 'utf-8' ) as f :                                                                                                          #apro 'fmappa' in lettura e lo associo a 'f'
        file = f . readlines ( )                                                                                                                                    #inizializzo 'file' come lista delle righe di 'f'
    movimenti_robot1 , movimenti_robot2 , dati_confronto_grezzi = genera_dati ( file , [ ] , [ ] , [ ] , 0 )                                                        #chiamo la funzione 'genera_dati'
    coordinate_robot1 = genera_coordinate_robot1 ( movimenti_robot1 , { } )                                                                                         #chiamo la funzione 'genera_coordinate_robot1'
    coordinate_robot2 = genera_coordinate_robot2 ( movimenti_robot2 , { } )                                                                                         #chiamo la funzione 'genera_coordinate_robot2'
    coordinate_confronto = genera_coordinate_confronto ( dati_confronto_grezzi , { } )                                                                              #chiamo la funzione 'genera_coordinate_confronto'
    return uscita ( coordinate_robot1 , coordinate_robot2 , coordinate_confronto , 0 )                                                                              #ritorno la chiamata della funzione 'usicta'
