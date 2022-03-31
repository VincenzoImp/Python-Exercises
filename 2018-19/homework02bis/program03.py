'''
Abbiamo un file contenente dei dati in forma tabellare:
- la prima riga contiene i nomi dei campi che individuano le informazioni, separati da tab
- la seconda riga contiene le indicazioni del tipo dei contenuti delle colonne (int/float/str) separati da tab
- le linee successive contengono i dati, sempre separate da tab, che devono essere intepretati come indicato nella seconda riga
    Nota: può succedere che una riga non contenga l'informazione in una o più colonne
Esempio: il file es3_esempio.txt che contiene dei dati presi da un gruppo di sensori ad intervalli di 1 minuto

Anno	Mese	Giorno	Ora	Minuto	Sensore1	Sensore2	Sensore3	Note
int	int	int	int	int	float	float	float	str
2018	12	25	0	0		3	45.3	manca il Sensore 1
2018	10	25	0	1	1	36		manca il Sensore 3
2017	11		0	2	14	5	82	manca il giorno
2016		23	11	17	13	4.5	32	manca il mese

Si vuol calcolare una "tabella pivot" per esaminare i dati e confrontarli tra loro.
(vedi https://en.wikipedia.org/wiki/Pivot_table)

Una tabella pivot è definita indicando:
    - quali campi devono essere mostrati in orizzontale come intestazioni di colonna nella prima riga
    - quali campi devono essere mostrati in verticale   come intestazioni di riga    nella prima colonna
    - quale campo deve   essere mostrato nella tabella in ciascuna delle altre caselle
    - come vanno aggregate le informazioni selezionate per una determinata casella (vedi sotto)
        - count     conta quanti valori diversi da '' sono presenti
        - min       trova il minimo
        - max       trova il massimo
        - sum       calcola la somma dei valori (solo per colonne numeriche)
        Nota: se non ci sono valori nelle righe selezionate, il risultato è '' (stringa vuota)

Nota: potete assumere che l'input di es3 sarà sempre corretto (p.es. si chiede 'sum' solo per campi con valori numerici)

La tabella viene costruita elencando come intestazioni delle colonne(righe) tutte le combinazioni di valori distinti che sono presenti nei campi selezionati.
Se come intestazione sono stati selezionati più campi, separatene i valori col carattere spazio ' '.
    Esempio, se nella tabella precedente si seleziona il campo 'Anno' le intestazioni delle colonne(righe) saranno, nell'ordine
        '2016'
        '2017'
        '2018'
    Se invece si selezionano i due campi ['Anno', 'Mese'] le intestazioni delle righe/colonne saranno, nell'ordine
        '2016 '         (qui il campo 'Mese' ha valore '')
        '2017 11'
        '2018 10'
        '2018 12'

Una volta individuate le combinazioni di valori da mostrare come intestazioni delle righe e delle colonne della tabella pivot, 
ciascuna casella della tabella individua una combinazione di valori unica dei valori dei campi di riga e di quelli di colonna. 
A ciascuna combinazione di valori corrispondono le 0 o più righe dei dati che hanno esattamente quei valori nei campi selezionati.
Nella corrispondente casella della tabella pivot va inserito il risultato che si ottiene 
applicando la funzione di aggregazione indicata al sottoinsieme di dati così selezionati che corrispondono a quella casella.

Esempio: vedi il file es3_Ris_esempio.txt che si ottiene dal file es3_esempio.txt selezionando:
    - per le colonne i campi ['Anno', 'Mese']
    - per le righe  il campo ['Giorno']
    - come dato da aggregare il campo 'Sensore1'
    - come funzione di aggregazione la funzione 'sum'
Ottenendo la tabella (in cui evidenzio le colonne con caratteri | )
-----------------------
|       |    |23  |25 |
|2016   |    |13.0|   |
|2017 11|14.0|    |   |
|2018 10|    |    |1.0|
|2018 12|    |    |   |
-----------------------

in cui possiamo notare: 
    la seconda colonna che ha intestazione di colonna ''      perchè una riga dei dati non conteneva il Giorno
    la seconda riga    che ha intestazione di riga    '2016 ' perchè una riga dei dati non conteneva il Mese
    diverse caselle della tabella che contengono il valore '' perchè non esisteva il dato per il Sensore1 
            per quella combinazione di valori di Anno, Mese, Giorno

Si implementi la funzione es3(fin, fout, colonne, righe, dato, aggregatore) che:
    - legge dal file fin una tabella di dati separati da tab, in cui
        - la prima riga indica i nomi dei campi 
        - la seconda riga i tipi dei dati delle colonne
        - dalla terza in poi contiene i dati
    - costruisce la tabella pivot che ha:
        - come intestazioni delle colonne le combinazioni uniche di valori per i campi elencati nella lista 'colonne', in ordine alfabetico crescente
        - come intestazioni delle righe   le combinazioni uniche di valori per i campi elencati nella lista 'righe',   in ordine alfabetico crescente
        - come valori di tutte le altre caselle i valori ottenuti aggregando i valori della colonna 'dato' con la funzione indicata da 'aggregatore'
            Nota: se per una casella non esistono righe dei dati oppure i dati non contengono valori, il valore per la casella è ''
    - salva la tabella pivot nel file fout
    - torna come risultato la coppia (nrighe, ncolonne) che indica la dimensione della tabella ottenuta, intestazioni di riga e colonna comprese

NOTA: potete assumere che i nomi delle colonne/righe indicate siano sempre presenti nella prima riga del file dei dati, 
    che i tipi ci siano e che ci sia almeno una riga di dati

TIMEOUT: il timeout per ciascun test è di 5 secondi.

ATTENZIONE: è proibito l'uso di ogni libreria aggiuntiva (non potete fare import)

ATTENZIONE: assicuratevi che il file del programma sia in encoding UTF8 (ad esempio editandolo in Spyder o Notepad++)

'''

def es3(fin, fout, colonne, righe, dato, aggregatore):
    nomi, tipi, dati = leggi_dati(fin)
    tipo = tipi[nomi.index(dato)]
    pivot, v_u_r, v_u_c = calcola_pivot(nomi, dati, righe, colonne, dato, aggregatore, tipo)
    pivot = crea_pivot(pivot, v_u_r, v_u_c)
    print_pivot(pivot, fout)
    w = len(pivot[0])
    h = len(pivot)
    return h, w

def leggi_dati(fin):
    # legge i dati e torna la coppia <nomi> <righe>
    f = open(fin, encoding='utf8')
    nomi = f.readline().rstrip('\n').split('\t')
    tipi = f.readline().rstrip('\n').split('\t')
    return nomi, tipi, ( line.rstrip('\n').split('\t') for line in f )

def crea_pivot(pivot, v_u_r, v_u_c):
    '''dati i valori aggregati e gli id unici di riga e colonna costruisce la matrice pivot'''
    v_u_r = sorted(v_u_r)
    v_u_c = sorted(v_u_c)
    matrice = [[ '' ] + list(map(' '.join, v_u_c))]
    for id_riga in v_u_r:
        matrice.append( [ ' '.join(id_riga) ] + [ pivot.get((id_riga,id_colonna), '') for id_colonna in v_u_c ] )
    return matrice

def print_pivot(pivot, fout):
    # stampa la tabella pivot nel file fout
    with open(fout, mode='w', encoding='utf8') as f:
        for riga in pivot:
            f.write('\t'.join(map(str, riga)) + '\n')

def calcola_pivot(nomi, dati, colonne, righe, dato, aggregatore, tipo):
    '''Dati i nomi delle colonne, i dati, le colonne e righe da usare, il nome del campo da aggregare e l'aggregatore, calcola i valori per tutte le combinazioni presenti
        e torna i valori aggregati e i due set di valori unici trovati per le righe e colonne '''
    # costruisce la tabella pivot
    campi = { v:i for i,v in enumerate(nomi) }
    # scandendo una volta le righe dei dati
    # - crea due elenchi di tuple di valori per le righe e per le colonne
    valori_unici_colonna = set()
    valori_unici_riga    = set()
    # - crea un dizionario ((riga),(colonna)) -> [valori]
    pivot = {}
    # - per ciascun item aggrega i dati con la funzione min/max/sum/count
    for riga in dati:
        id_riga    = tuple( riga[campi[nome]] for nome in righe   )
        id_colonna = tuple( riga[campi[nome]] for nome in colonne )
        valore     = riga[campi[dato]]
        valori_unici_riga.add(id_riga)
        valori_unici_colonna.add(id_colonna)
        pivot_id = id_riga, id_colonna
        aggrega(pivot, pivot_id, valore, aggregatore, tipo)
    return pivot, valori_unici_riga, valori_unici_colonna

def aggrega(pivot, pivot_id, valore, aggregatore, tipo):
    '''aggrega il valore con l'aggregato precedente.
        - se il valore è '' non è presente e lo si ignora
        - lo converte al tipo di dato richiesto
        - se l'aggregato precedente non c'è lo inizializzo con un valore nullo per quel tipo di aggregatore
        - e poi si aggrega come si deve
    '''
    if valore == '': return
    convert    = { 'int' : int, 'float' : float, 'str'   : str, }
    valore     = convert[tipo](valore)
    nullo      = { 'min' : valore, 'max': valore, 'sum' : 0,               'count' : 0               }
    incremento = { 'min' : min,    'max': max,    'sum' : lambda v,a: v+a, 'count' : lambda v,a: a+1 }
    aggregato  = pivot.get( pivot_id, nullo[aggregatore] )
    pivot[pivot_id] = incremento[aggregatore](valore, aggregato)
