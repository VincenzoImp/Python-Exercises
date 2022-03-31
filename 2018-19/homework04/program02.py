''' 
    Si consideri il seguente gioco solitario: 
    abbiamo una sequenza iniziale di  N interi, 
    una mossa del gioco consiste nel selezionare nella sequenza  due numeri  consecutivi 
    la cui somma sia pari, i due numeri vengono eliminati dalla sequenza e 
    sostituiti dalla loro  media aritmetica. Il gioco e' vinto se si trova una sequenza 
    di mosse che riduce la sequenza  ad un unico numero.
    Una configurazione del gioco e' univocamente determinata dai numeri presenti nella 
    sequenza in quel momento.
    Data una configurazione iniziale noi siamo interessati a trovare la lista di tutte 
    le possibili configurazioni finali (vale a dire configurazioni per cui non c'e' possibilita' 
    di continuare il gioco per mancanza di possibili mosse).
    Si consideri ad esempio l'albero di gioco che si ottiene a partire dalla configurazione 
    10 20 30 40 5 1 e che e' riportato  nel file albero_di_gioco.pdf
    le possibili configurazioni finali sono 5:
    8, 14, 17, 15 20 1, 10 25 40 3.
    
    Definire una funzione es2(s) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che, data una  stringa  che codifica  una  configurazione iniziale 
    del gioco, retituisce  la lista delle codifiche delle possibili configurazioni finali.
    - le configurazioni di gioco vanno codificate tramite  stringhe (in queste stringhe i 
       numeri della sequenza compaiono uno di seguito all'altro e separati da uno spazio).
    - La lista delle codifiche delle configurazioni finali prodotta in output contiene 
      le configurazioni codificate come stringhe. Queste configurazioni devono comparire
      nella lista in ordine crescente rispetto alla loro lunghezza e, a parita' di lunghezza,  
      ordinate in modo crescente rispetto al primo numero in cui differiscono.
      Ad esempio la lista che la funzione es2 se invocata con s='10 20 30 40 5 1' 
      deve restituire la lista
      ['8', '14', '17', '15 20 1', '10 25 40 3']

NOTA: il timeout previsto per questo esercizio è di 3 secondi per ciascun test.

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe

ATTENZIONE: Non potete usare altre librerie

ATTENZIONE: Sono vietate le variabili globali

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

'''

'''
ALGORITHM
data la stringa in input la metto in una lista, cosi per ogni elemento della lista scorro i numeri che in essa compaiono e creo così tutte le combinazioni che si possono realizzare seguendo le regole del solitario, quindi inserisco le combinazioni create nella lista
eliminando la madrice di queste combinazioni, ovvero la stringa che ci ha permesso di generarle, questo verrà ripetuto fino a quando tutti gli elementi della lista sono impossibilitati a generare nuove combinazioni, il che significa che sono le soluzioni del solitario
che ritorno alla funzione principale che non fa altro che ordinarle mediante i criteri descritti nella consegna.
'''

def genera_insieme ( lista ) :                                                                                                      #inizzializzo la funzione 'genera_insieme'
    return { lista [ : c ] + ( str ( ( int ( lista [ c ] ) + int ( lista [ c + 1 ] ) ) // 2 ) , ) + lista [ c + 2 : ]               #avente 'lista' ritorno un insieme che ogni elemento è una stringa formata da tutti gli elementi di 'lista' fino alla posizione 'c' non compresa più l'elemento che è la media dell'elemento in posizione 'c' con quello in posizione 'c'+1 più tutti gli elementi della lista in posizione 'c'+2 in poi
            for c in range ( len ( lista ) - 1 )                                                                                    #per ogni valore 'c' che va da 0 alla lunghezza di 'lista'-1
            if int ( lista [ c ] ) % 2 == int ( lista [ c + 1 ] ) % 2 }                                                             #se il valore della lista in posizione 'c' e quello in posizione 'c'+1 sono entrambi pari o dispari

def funzione_1 ( tot , uscita ) :                                                                                                   #inizzializzo la funzione 'funzione_1'
    for lista in tot . copy ( ) :                                                                                                   #itero ogni 'lista' di 'tot'
        insieme = genera_insieme ( lista )                                                                                          #chiamo la funzione 'genera_insieme' che mi ritorna il valore che associo ad 'insieme'
        tot . remove ( lista )                                                                                                      #rimuovo da 'tot' la 'lista'
        tot |= insieme                                                                                                              #aggiungo a 'tot' tutti gli elementi di 'insieme'
        if insieme == set ( ) :                                                                                                     #se 'insieme' è vuoto
            uscita = funzione_2 ( lista , uscita , '' )                                                                             #richiamo la funzione 'funzione_2' che mi restituisce 'uscita'
    return tot , uscita                                                                                                             #ritorno 'tot' e 'uscita'

def funzione_2 ( lista , uscita , parola ) :                                                                                        #inizzializzo la funzione 'funzione_2'
    for elemento in lista :                                                                                                         #per ogni 'elemento' di 'lista'
        parola += elemento + ' '                                                                                                    #aggiungo a 'parola', 'elemento' più ' '
    uscita . add ( parola [ : - 1 ] )                                                                                               #aggiungo ad 'uscita' la variabile 'parola' meno l'ultimo suo elemento
    return uscita                                                                                                                   #ritorno 'uscita'

def ricorsione ( tot , uscita ) :                                                                                                   #inizzializzo la funzione 'ricorsione'
    tot , uscita = funzione_1 ( tot , uscita )                                                                                      #chiamo la funzione 'funzione_1' che mi restituisce 'tot' e 'uscita'
    if tot == set ( ) :                                                                                                             #se 'tot' è un insieme vuoto
        return uscita                                                                                                               #allora ritorno 'uscita'
    return ricorsione ( tot , uscita )                                                                                              #altrimenti ritorno la funzione 'ricorsione'

def es2 ( s ) :                                                                                                                     #inizzializzo la funzione 'es2'
    return list ( sorted ( ricorsione ( { tuple ( s . split ( ) ) } , set ( ) ) ,                                                   #ritorno la lista ordinata di ciò che mi ritorna dalla chiamata della funzione 'ricorsione'
                       key = lambda x : [ len ( x . split ( )  ) ] + [ int ( x . split ( ) [ y ] )                                  #dove la chiave di ordinamento è una funzione che per ogni elemento dell'elemento ritornato da 'ricorsione' ordina in base alla lunghezza e con ugual lunghezza ordina ogni elemento in base al numero in posizione 'y'
                       for y in range ( len ( x . split ( ) ) ) ] ) )                                                               #per ogni 'y' che va da 0 alla lunghezza dell'elemento dato non compresa
