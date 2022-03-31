'''
Data una lista di parole ed un testo, vogliamo trovare un anagramma del testo.
L'anagramma da trovare deve essere formato esattamente da 3 parole di almeno 2 caratteri, diverse tra loro, tra quelle fornite, se esiste (altrimenti tornate None).
Nel confrontare i caratteri ignorate la differenza tra minuscole e maiuscole.
Ignorate inoltre differenze nel numero di spazi presenti.
Potete assumere che le lettere del testo e delle parole siano tutte alfabetiche (oppure spazio nel testo).

Definite la funzione es3(parole, testo) che torna la tupla delle tre parole diverse che formano l'ultimo anagramma in ordine alfabetico.
NOTA: la lista delle parole non deve essere modificata dalla funzione.

Esempio: la terna corrispondente all'ultimo anagramma di 3 parole dei testi seguenti,
ottenuto usando le 60000 parole italiane contenute nel file allegato, è:
    "Andrea Sterbini"       -> ('treni', 'sia', 'brande')
    "Angelo Monti"          -> ('toni', 'nego', 'mal')
    "Angelo Spognardi"      -> ('sragion', 'pend', 'lago')
    "Ha da veni Baffone"    -> ('video', 'beh', 'affanna')

ATTENZIONE: non è permesso usare librerie aggiuntive

ATTENZIONE: sono vietate le variabili globali

ATTENZIONE: prima di consegnare assicuratevi che il file del programma sia nell'encoding UTF8, 
ad esempio editandolo in Notepad++ oppure Spyder.

'''

def es3(parole, testo):
    # tutte le parole minuscole
    parole = [ p.lower() for p in parole if len(p) > 1 ]
    # e anche il testo, a cui tolgo gli spazi
    testo = testo.lower().replace(' ', '')
    # lunghezza del testo (senza spazi)
    N = len(testo)
    # insieme dei caratteri del testo
    t_caratteri = set(testo)
    # istogramma del loro conteggio
    t_histo = { c: 0 for c in t_caratteri }
    for c in testo:
        t_histo[c] += 1
    # dizionario parola-> insieme delle lettere contenute nella parola
    lettere = {}
    # dizionario parola-> histogramma delle lettere contenute nella parola
    histo   = {}
    for p in parole:
        # ignoro le parole troppo lunghe
        if len(p) > N:
            continue
        chars = set(p)
        # ignoro le parole che hanno caratteri non presenti nel testo
        if chars - t_caratteri:
            continue
        # ricordo il set di lettere della parola
        lettere[p] = chars
        # e l'istogramma della parola
        histo[p] = { c : 0 for c in lettere[p] }
        for c in p:
            histo[p][c] += 1
    print(t_caratteri, t_histo, N, len(lettere), sep='\n')
    #print(t_caratteri, t_histo, N, len(lettere), lettere, histo, sep='\n')
    return cerca_istogramma(t_caratteri, t_histo, N, lettere, histo )


def cerca_istogramma(caratteri_mancanti, conteggio_mancanti, N, caratteri_parole, histo_parole ):
    # prima parola
    parole = sorted(caratteri_parole.keys(), reverse=True)
    NC=len(caratteri_mancanti)
    for i, p1 in enumerate(parole[:-2]):
        # ignoro le parole troppo lunghe
        if len(p1)> N:
            continue
        if len(caratteri_parole[p1]) > NC:
            continue
        # ignoro la parola se ha bisogno di troppi caratteri rispetto ai presenti
        if any( [ histo_parole[p1][c]>conteggio_mancanti[c] for c in p1 ] ):
            continue
        # e aggiorno il calcolo dei rimanenti
        c_restanti1 = conteggio_mancanti.copy()
        for c in caratteri_parole[p1]:
            c_restanti1[c] -= histo_parole[p1][c]
        #print(p1, c_restanti1)
        # e il numero di caratteri da cercare
        N1 = N - len(p1)
        NC1 = len({ k for k,v in c_restanti1.items() if v } )
        for j, p2 in enumerate(parole[i:]):
            # ignoro le parole troppo lunghe
            if len(p2)> N1:
                continue
            if len(caratteri_parole[p2]) > NC1:
                continue
            # ignoro la parola se ha bisogno di troppi caratteri rispetto ai presenti
            if any( [ histo_parole[p2][c]>c_restanti1[c] for c in p2 ] ):
                continue
            # e aggiorno il calcolo dei rimanenti
            c_restanti2 = c_restanti1.copy()
            for c in caratteri_parole[p2]:
                c_restanti2[c] -= histo_parole[p2][c]
            #print('\t', p2, c_restanti2)
            # e il numero di caratteri da cercare
            N2 = N1 - len(p2)
            NC2 = len({ k for k,v in c_restanti2.items() if v } )
            for k, p3 in enumerate(parole[j:]):
                # ignoro le parole troppo lunghe
                if len(p3) != N2:
                    continue
                if len(caratteri_parole[p3]) != NC2:
                    continue
                #print('\t1t', p3)
                # ignoro la parola se non ha bisogno degli stessi caratteri
                if any( [ histo_parole[p3][c] != c_restanti2[c] for c in p3 ] ):
                    continue
                return p1, p2, p3

