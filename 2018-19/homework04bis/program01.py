

''' 
    Alice e Bob si affrontano nel seguente gioco: 
    hanno  una sequenza iniziale di  N interi, 
    una mossa del gioco consiste nel selezionare dalla sequenza  due numeri  consecutivi 
    a e b, con a>b, i due numeri vengono eliminati dalla sequenza e 
    sostituiti dalla loro  differenza (a-b). Alice e Bob si alternano nelle mosse 
    con Alice che effettua la prima mossa, il gioco e' vinto se all'avversario viene 
    lasciata una sequenza per cui non e' possibile muovere (vale a dire: nella sequenza 
    non sono presenti due numeri consecutivi a e b con a>b).
    Data la sequenza  iniziale siamo interessati a trovare il numero 
    di possibili partite che portano alla vittoria di  Alice ed il numero di 
    possibili partite che portano alla vittoria di Bob. 
    
    Si consideri ad esempio l'albero di gioco che si ottiene a partire dalla 
    sequenza-configurazione '19 -3 2 -10 -20'  e che e' riportato  nel file 
    albero_di_gioco1.pdf:
    le possibili partite vittoriose per Alice sono tre (tutte portano alla 
    sequenza-configurazione '22 32') mentre le possibili partite vittoriose  per Bob sono 
    sei (tre partite con configurazione finale '10', due partite con configurazione 
    finale '30' e una partita con configurazione finale '50'). 
    
    Definire una funzione es(s) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che, data una  stringa  che codifica  una  configurazione iniziale 
    del gioco (i numeri della sequenza son separati da uno spazio), restituisce  
    una tupla di 6 elementi.
    - la prima   componente della tupla e' il numero di possibili vittorie di Alice
    - la seconda componente della tupla e' il numero di possibili vittorie di Bob
    - la terza   componente della tupla e' il numero di nodi-configurazioni presenti 
      nell'albero di gioco.
    - la quarta  componente della tupla e' il nome del vincitore della partita più corta
    - la quinta  componente della tupla e' il nome del vincitore della partita più lunga
    - la sesta   componente e' una lista con tutte le DIVERSE configurazioni di gioco presenti
    nell'albero di gioco. Ciascuna configurazione deve apparire nella lista
    come tupla di interi e le tuple devono comparire nella lista ordinate per lunghezza 
    crescente e, a parita' di lunghezza, in ordine crescente.
    
    Ad esempio es('19, -3, 2, -10, -20') deve restituire la sestupla 
    (3, 6, 25, 'Bob', 'Alice', 
        [(10,), (30,), (50,), 
        (10, -20), (20, 10), (22, 32), (30, -20), 
        (19, -3, 32), (20, -10, -20), (22, 2, 10), (22, 12, -20), 
        (19, -3, 2, 10), (19, -3, 12, -20), (22, 2, -10, -20), 
        (19, -3, 2, -10, -20)])

ATTENZIONE: non sono permesse altre librerie altre a quelle già importate.

TIMEOUT: il timeout per ciascun test è di 1 secondo.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

'''

class Nodo:
    def __init__(self, sequenza, player):
        self.sequenza = sequenza
        self.player   = player
        self.figli    = []
        for i in range(len(sequenza)-1):
            a, b = sequenza[i:i+2]
            if a > b:
                nuova = sequenza.copy()
                nuova[i:i+2] = [a-b]
                #print(f"{sequenza} -> {nuova}")
                self.figli.append(Nodo(nuova, not player))

    def conta(self, player):
        if not self.figli and self.player == player:
            return 1
        else:
            return sum(son.conta(player) for son in self.figli)

    def conta_nodi(self):
        return sum(son.conta_nodi() for son in self.figli) + 1

    def configurazioni(self):
        conf = { tuple(self.sequenza) }
        for son in self.figli:
            conf |= son.configurazioni()
        return conf

    def foglie(self):
        if not self.figli:
            return { tuple(self.sequenza) }
        risultato = set()
        for son in self.figli:
            risultato |= son.foglie()
        return risultato

    def __repr__(self, livello=0):
        ris = f"{'|   ' * livello}{self.sequenza}\n"
        for son in self.figli:
            ris += son.__repr__(livello+1)
        return ris

    def deepest_winner(self, level=0):
        winners = [ (level, not self.player, self.sequenza) ] + [ son.deepest_winner(level+1) for son in self.figli ]
        return max(winners, key=lambda pair: pair[0])

    def shallowest_winner(self, level=0):
        if not self.figli:
            return level, not self.player, self.sequenza
        winners = [ son.shallowest_winner(level+1) for son in self.figli ]
        return min(winners, key=lambda pair: pair[0])


def es1(s):
    #inserisci qui il tuo codice
    sequenza = list(map(int, s.split()))
    root = Nodo(sequenza, 0)
    print(root)
    vinteA       = root.conta(1)
    vinteB       = root.conta(0)
    numnodi      = root.conta_nodi()
    deepest      = root.deepest_winner()
    print(deepest)
    deepest      = ['Alice', 'Bob'][deepest[1]]
    shallowest   = root.shallowest_winner()
    print(shallowest)
    shallowest   = ['Alice', 'Bob'][shallowest[1]]
    conf         = root.configurazioni()
    conf         = sorted( conf, key=lambda t: (len(t), t) )
    return vinteA, vinteB, numnodi, deepest, shallowest, conf
