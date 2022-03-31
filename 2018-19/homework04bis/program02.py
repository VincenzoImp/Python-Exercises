
'''
    Considera alberi i cui nodi hanno come valore stringhe sempre composte da due caratteri. 
    Vogliamo costruire stringhe di testo che raffigurano questi alberi. Ad esempio:

                                                        60                                    
                                        ________________|________________                     
                                       |                                 |                    
                                       66                                25                   
                  _____________________|_____________________        ____|_____               
                 |                            |              |      |          |              
                 56                           58             19     96         77             
     ____________|____________           _____|_____       __|__         ______|______        
    |             |           |         |       |   |     |     |       |   |         |       
    36            33          55        67      66  05    54    50      52  42        72      
 ___|___     _____|_____     _|_     ___|___    |        _|_    |       |   |    _____|_____  
|   |   |   |   |   |   |   |   |   |   |   |   57      |   |   84      03  89  |   |   |   | 
70  99  05  28  52  80  84  79  66  48  80  16          28  86                  94  87  85  26

    Le stringhe di testo che rappresentano l'albero sono composte da un certo numero di righe tutte 
    con lo stesso numero di caratteri. Ne diamo di seguito la definizione ricorsiva 
        -Se l'albero T e' una foglia la stringa di testo e' composta da un'unica riga 
        in cui compaiono i due caratteri che corrispondono al valore  del nodo.  
        -Se l'albero T ha t figli:
         vengono prima ricorsivamente costruite le t stringhe di testo corrispondenti ai t sottoalberi.
          Le t stringhe vengono poi concatenate a formare la stringa corrispondente all'albero T. 
          L'operazione di fusione delle t stringhe avviene attraverso  i seguenti passi:  
         a) per ciascun sottoalbero la prima riga di ciascuna stringa di testo contiene il valore
            della radice del sottoalbero. Sia c la posizione nella riga della prima cifra di questo valore.
            In testa a ciascuna stringa viene inserita una nuova riga. La riga contiene 
            il simbolo '|' in posizione c e spazi in tutte altre posizioni.
         b) sia h il numero massimo di righe per le t stringhe di testo dei t sottoalberi. 
            Ad ognuna delle t stringhe vanno  aggiunte righe di soli spazi in modo che 
            tutte le stringhe risultino avere h righe. 
         c) dalle t  stringhe si ottiene poi un'unica stringa di testo T1 di h righe, 
            la stringa si ottiene concatenando le righe delle t stringhe e lasciando 
            tra ciascuna riga e la seguente  due  spazi. Piu' precisamente 
            la riga i-esima della nuova stringa e' ottenuta dalla concatenazione  delle righe 
            i-esime delle t  stringhe di testo (nel  concatenare due stringhe tra l'una e 
            l'altra vengono inseriti sempre DUE spazi).
         d) Considera la prima riga di T1. Sia a la posizione  in cui in questa riga  
            compare per la prima volta il carattere '|' 
            e sia b la posizione in cui il carattere '|' compare per l'ultima volta.
            Si costruisce una nuova riga, che conterra' un unico carattere '|' , 
            degli spazi ed eventualmente dei caratteri '_'.
            - Se a=b (questo significa che  la radice dell'albero  ha un unico figlio) 
            la nuova riga conterra' lo spazio in tutte le posizioni  tranne che 
            in posizione a dove compare il  carattere '|'.
            - Se a<b (questo significa  che la radice dell'albero ha piu' figli) 
            allora la nuova riga conterra' spazi fino alla posizione a e dalla posizione b in poi, 
            conterra' il simbolo '|' in posizione (a+b)//2 e le rimanenti posizioni 
            saranno occupate dal simbolo '_'.
            Questa nuova riga viene inserita in testa alla stringa T1. 
         e) Nella attuale prima riga di T1 sia c la posizione in cui compare il carattere '|' .
            Si crea una nuova riga che  contiene   spazi in tutte le posizioni
            tranne che nelle posizioni c e c+1 dove viene inserito il valore  della radice di T. 
            Questa nuova riga viene inserita in testa alla stringa T1.
         f) La stringa di testo T1 cosi' ottenuta dopo aver effettuato i passi a)-e) e' la stringa 
            di testo che rappresenta l'albero.
    
    Si definisca la funzione es(r) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
    riceve come argomento un nodo r radice  di un  albero  (i nodi dell'albero sono di tipo  
    Albero definito nella libreria albero.py allegata ed hanno tutti come valore stringhe 
    di due caratteri) e restituisce una stringa di testo che rappresenta l'albero.

NOTA: il timeout previsto per questo esercizio è di 0.5 secondi per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)
   
ATTENZIONE: non sono permesse altre librerie oltre a quelle già importate.
    
'''
    
import albero

def converti(root):
    if not root.f:
        #      stringa    c  w  h
        return [root.id], 0, 2, 1
    N = len(root.f)
    sottoalberi = [ converti(son) for son in root.f ]
    # se 1
    righe, c, w, H = sottoalberi[0]
    if N==1:
        prima_riga   = ' '*c + root.id + ' '*(w-c-2)
        seconda_riga = ' '*c + '|'     + ' '*(w-c-1)
        righe[0:0] = [prima_riga, seconda_riga]
        return righe, c, w, H+2
    # se N
    pad(sottoalberi)
    righe, A, B, W, H = concatena(sottoalberi)
    centro = (A+B)//2
    riga1 = ' '*centro + root.id + ' '*(W-centro-2)
    riga2 = ' '*(A+1) + '_'*(centro-A-1) + '|' + '_'*(B-centro-1) + ' '*(W-B)
    riga3 = '  '.join([ ' '*c + '|'+' '*(w-c-1) for _,c,w,_ in sottoalberi ] )
    righe[0:0] = [ riga1, riga2, riga3 ]
    return righe, centro, W, H+3

def concatena(sottoalberi):
    '''concatena le righe di sottoalberi di stesso numero di righe inserendo 2 spazi'''
    testi, a, W, h = sottoalberi[0]
    b = a
    for righe, c, w, h1 in sottoalberi[1:]:
        b  = W + c + 2
        W += w + 2
        for i, riga in enumerate(righe):
            testi[i] += '  ' + riga
    return testi, a, b, W, h

def pad(sottoalberi):
    H = 0
    for righe, _c, _w, _h in sottoalberi:
        H = max(H,len(righe))
    for righe, _c,  w, _h in sottoalberi:
        h = len(righe)
        if h < H:
            pad = ' '*w
            righe.extend([pad]*(H-h))

def es2(r):
    #inserisci qui il tuo codice
    righe, c, w, h = converti(r)
    return '\n'.join(righe)
