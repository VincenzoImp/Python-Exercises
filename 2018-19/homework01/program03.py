'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
    (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
    (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
    Nella lista di output ogni parola appare una sola volta e le parole
    risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
    (i.e. quella che compare per prima al primo posto ecc.ecc.)
    Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
    in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
    Ad esempio: se lista=['gatto','cane','topo']
    - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
    se lista=['ala','cena','elica','nave','luce','lana','vela']
    - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
    e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''

'''
ALGORITHM
Scorro il testo ritagliandone un pezzo e confrontandolo con la lista delle parole.
Ingrandisco il pezzo sempre di più fino a trovare una parola corrispondente e poi riparto.
Infine confronto il numero di utilizzi di ciascuna parola (salvati precedentemente) e trovo quella più utilizzata.
'''

def rem(lista, parole):
    for parola in parole:
        if parole[parola] > 0:
            lista.remove(parola)

def max_par(parole):
    n = parole[next(iter(parole))]
    par = []
    for parola in parole:
        if parole[parola] > n:
            n = parole[parola]
            par = [parola]
        elif parole[parola] == n:
            par.append(parola)
    par.sort()
    return par

def es3(lista, testo):
    zero = [0] * len(lista)
    parole = dict(zip(lista, zero))
    parole_usate = {}

    par_min = len(min(lista, key=len))

    i = 0
    j = par_min
    l = len(testo)

    while i < l:
        parola = testo[i:j]
        if parola in parole:
            parole[parola] += 1
            parole_usate[parola] = True
            i = j
            j += par_min
        else:
            j += 1

    rem(lista, parole)
    return (list(parole_usate.keys()), max_par(parole)[0])
