"""
Bisogna indovinare una  sequenza  numerica segreta X composta da
una permutazione dei primi N interi.
Vengono fornite   M sequenze numeriche  con 5<=M<=N.
Delle M sequenze sappiamo che ciascuna  e' ottenuta a partire X
applicando il seguente procedimento:
a) viene selezionato un elemento della stringa X.
b) l'elemento selezionato viene cancellato da X ricompattando la sequenza
c) l'elemento cancellato viene reinserito in X in una qualunque delle
possibili posizioni diversa da quella originale.
Sappiamo inoltre che gli elementi selezionati per creare le M sequenze
son tutti diversi tra loro.
Date le M sequenze vogliamo scoprire la sequenza numerica X

Ad esempio si cosiderino le seguenti 6 sequenze:

1) 2 3 4 7 1 5 6 8
2) 7 2 1 3 4 5 6 8
3) 7 2 3 4 1 6 5 8
4) 7 2 3 4 1 6 5 8
5) 7 4 2 3 1 5 6 8
6) 8 7 2 3 4 1 5 6

la sequenza segreta X e' 7 2 3 4 1 5 6 8
infatti gli spostamenti di  X che hanno prodotto le 6 sequenze sono:
1) il 7 selezionato e poi reinserito in posizione 4
2) l' 1 selezionato e poi reinserito in posizione 3
3) il 6 selezionato e poi reinserito in posizione 1
4) il 5 selezionato e poi reinserito in posizione 6
5) il 4 selezionato e poi reinserito in posizione 2
6) l' 8 selezionato e poi reinserito in posizione 1

Scrivere una funzione es2(ftesto,ftesto1) che prende in input  il
nome del file di testo ftesto contenente le  M sequenze  e
e produce il file di testo di nome  ftesto1 con la sequenza segreta X

Gli elementi delle  sequenze in ftesto sono in linee consecutive e
ciascun elemento e'
separato dal successivo da uno o piu' spazi bianchi o dal return.
Ciascuna sequenza e' separata dalla precedente da almeno una linea vuota.

Gli elementi della sequenza in ftesto1 sono in linee consecutive, ogni linea
contiene esattamente tre elementi della sequenza tranne l'ultima che puo'
contenerne di meno. Ogni elemento elemento della sequenza e'
separato dal successivo da uno spazio o un return.

'''2 3 4 7 1 5 6 8\n\n
7 2 1 3 4 5 6 8\n\n
7 2 3 4 1 6 5 8\n\n
6 7 2 3 4 1 5 8\n\n
7 4 2 3 1 5 6 8\n\n
8 7 2 3 4 1 5 6'''

allora ftesto1 conterra' il testo
''7 2 3\n4 1 5\n6 8''

NOTA: il timeout previsto per questo esercizio è di 6 secondi per ciascun test

ATTENZIONE: sono proibite tutte le librerie aggiuntive

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder)
"""

def es2(fin, fout):
    sequenze = []
    last     = []
    with open(fin, encoding='utf8') as f:
        for line in f:
            line = line.strip()
            if line:
                last += line.split()
            else:
                if last:
                    sequenze.append(last)
                    last = []
    if last:
        sequenze.append(last)
    sequenza = trova_sequenza(sequenze)
    with open(fout, mode='w', encoding='utf8') as f:
        while sequenza:
            f.write(' '.join(sequenza[:3]) + '\n')
            sequenza = sequenza[3:]

def move(lista, i, j):
    seq = lista.copy()
    el = seq.pop(i)
    seq.insert(j, el)
    return seq

def trova_sequenza(sequenze):
    tot = len(sequenze)
    N = len(sequenze[0])
    ipotesi = {}
    for sequenza in sequenze:
        for i in range(N):
            for j in range(N):
                if i != j:
                    seq = move(sequenza, i, j)
                    seq = tuple(seq)
                    ipotesi[seq] = ipotesi.get(seq, 0) + 1
    mm = max(ipotesi.values())
    ss = sum(ipotesi.values())
    #print(N, tot, mm, ss)
    sol = []
    for s, n in ipotesi.items():
        if n == mm:
            sol.append(s)
    if len(sol)>1:
        print(sol, sequenze)
    return sol[0]

def genera_sequenze(N, scramble=False):
    import random
    sequenza = list(range(1, N+1))
    if scramble:
        for _ in range(N):
            i = random.randint(0,N-1)
            j = random.randint(0,N-1)
            while i == j:
                j = random.randint(0,N-1)
            sequenza = move(sequenza, i, j)
    sequenze = []
    selected = set()
    for _ in range(random.randint(5, N)):
        i = random.randint(0,N-1)
        while i in selected:
            i = random.randint(0,N-1)
        j = random.randint(0,N-1)
        while i == j:
            j = random.randint(0,N-1)
        selected.add(i)
        seq = move(sequenza, i, j)
        if seq not in sequenze:
            sequenze.append(seq)
        #print(seq)
    #print('>>>',sequenza)
    return list(sequenze)
