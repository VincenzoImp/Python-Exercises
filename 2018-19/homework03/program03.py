# -*- coding: utf-8 -*-
"""
NOTA: La descrizione è lunga ma il compito non è difficile, è solo lungo da spiegare con precisione.


Bisogna definire tre Classi (Attore, Film e Regista) con i relativi attributi e
metodi per realizzare una videoteca di film, i cui dati sono memorizzati in file
di tipo json che hanno la struttura come nei file di esempio "actors.json" e
"films.json". Le specifiche delle tre classi sono illustrate più avanti.
Bisogna implementare inoltre due funzioni che leggono i file json ed istanziano gli Attori, Film e Registi.

FUNZIONI DA IMPLEMENTARE

Per costruire l'elenco delle istanza di Attore, Film e Regista a partire dai due file
"actors.json" e "films.json" dovete realizzare le seguente due funzioni.
Le classi da realizzare sono descritte dopo.

- leggi_archivio_attori(file_json)
    che legge l'archivio json fornito in input che descrive tutti gli attori
    (con lo stesso formato del file di esempio actors.json)
    e torna un dizionario catalogo_attori { nome -> oggetto di tipo Attore } in cui:
    - le chiavi sono i nomi degli attori
        (prese dal campo "NAME" del dizionario presente per ogni attore nel file json)
    - i valori sono le corrispondenti istanze di tipo Attore create col costruttore passando
        come argomento il dizionario (letto dal file json) che contiene le informazioni dell'attore.

- leggi_archivio_film(file_json, catalogo_attori)
    - che legge dal file json fornito in input che descrive tutti i film
    (con lo stesso formato del file di esempio films.json)
    - ed inoltre riceve il dizionario catalogo_attori { nome->Attore } prodotto con la funzione precedente
    e torna come risultato una coppia di dizionari ( catalogo_film, catalogo_registi )
    Il catalogo_film deve essere un dizionario { titolo -> oggetto di tipo Film } in cui:
        - le chiavi sono i titoli dei film
            (preso dal campo "TITLE" del dizionario presente per ogni film nel file json)
        - i valori sono le corrispondenti istanze di tipo Film create col costruttore passando
            come argomento il dizionario (letto dal file json) che contiene le informazioni del Film.
    Il catalogo_registi deve essere un dizionario { nome -> oggetto di tipo Regista } in cui:
        - le chiavi sono i nomi dei registi
            ( presi dal campo "DIRECTORS" dei dizionari json che descrivono i film presi dal file json)
        - i valori sono istanze del tipo Regista (di cui vedete la definizione più sotto)

    La funzione leggi_archivio_film deve fare in modo che:
    - all'interno di ciascun oggetto Film siano inseriti gli oggetti Attore in modo che:
        - ogni Film contenga gli Attori che ci hanno lavorato
        - ogni Attore contenga i Film in cui è comparso
    - all'interno di ciascun oggetto Film siano contenuti gli oggetti di tipo Regista in modo che:
        - ogni Film contenga i Registi che l'hanno diretto
        - ogni Regista contenga i Film che ha diretto

    NOTA: le istanze che rappresentano ciascun Attore, Film e Regista devono essere uniche.
        (a tal proposito sfruttate i dizionari catalogo_attori, catalogo_film e catalogo_registi
        che avete costruito / state costruendo)

CLASSI DA IMPLEMENTARE

La classe Attore rappresenta la scheda di un attore.
Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
per realizzare i metodi seguenti a partire dalle informazioni json ottenute dal file actors.json
allegato (o da file json simile).

    Implementate i metodi di istanza:

    - Il costruttore della classe riceve un dizionario ottenuto dal file json actors.json (o file simile).
        Il dizionario passato come argomento contiene le informazioni relative ad un solo attore.
        Il costruttore assegna agli attributi tutti i valori necessari a partire dal dizionario json passato.
    - nome(self)        che ne torna il nome
    - vero_nome(self)   che ne torna il vero nome
    - films(self)       che torna l'insieme di oggetti Film in cui l'attore ha partecipato
    - registi(self)     che torna un set contenente le istanze di oggetti di tipo
      Regista, con cui l'attore ha girato almeno un film.
    - regista_preferito(self), che restituisce un'istanza di un oggetto Regista,
      che rappresenta il regista con cui l'attore self ha girato più film.
      In caso di pareggio, viene preso il regista il cui nome viene prima in ordine alfabetico.
    - coprotagonisti(self), che restituisce un set contenente le istanze di oggetti
      di tipo Attore, che rappresentano tutti gli attori con cui l'attore self ha girato
      almeno un film.
    - in_coppia(self, partner=None), che restituisce:
      Se il parametro partner (stringa) NON viene specificato:
        - un set di tuple: ogni tupla è del tipo (a_m, a_f, n_f),
        dove a_f e a_m sono due istanze di oggetto di tipo Attore
        (di cui una rappresenta l'attore self), di genere diverso (campo "GENDER" dei dati json)
        (a_f è femmina e a_m è maschio) ed n_f è il numero di film in cui self e il suo partner
        hanno fatto coppia (ovvero hanno girato PIU' DI UN film assieme).
      Se il parametro partner VIENE specificato (di tipo stringa), viene restituito invece
        - il set di tutti i Film (che può essere vuoto) in cui l'attore self e l'attore partner che ha quel nome
        hanno fatto coppia (ovvero hanno girato ALMENO quel film assieme).
    - luogo_preferito(self), che restituisce la stringa con il paese in cui l'attore
      self ha girato più film.
      In caso di pareggio, viene restituito il luogo che viene prima in ordine alfabetico.
      Se non esiste si torna None
    - film_durata(self, inf=0, sup=None), che restituiscela lista delle istanze
      degli oggetti di tipo Film, dei film in cui l'attore self ha recitato e che
      durano almeno inf minuti e, se sup è specificato, massimo sup minuti. La
      lista deve essere ordinata per durata dei film in ordine crescente.
      In caso di parità per titolo crescente in ordine alfabetico.
      Se nel file json sono specificate più durate per lo stesso film, usate la durata minore.
      Se nei dati json la durata non è indicata ignorate quel film.
      NOTA: per estrarre la durata dalla proprieta' "RUNTIME" dei dati json che descrivono un film
            avete il permesso di usare la libreria re per le espressioni regolari.
    - eta(self), che restituisce un intero che indica l'età dell'attore:
        - se l'anno di nascita NON è presente tornate None (e ignorate questo attore nel metodo Regista.attore_preferito)
        - se l'anno di morte NON è presente usate il 2018 come anno di riferimento
        - altrimenti tornate il numero di anni vissuti
            Es. nato: 1950 oggi: 2018 -> 69
      NOTA: per estrarre l'anno dalle proprieta' "BIRTH" e "DIED" dei dati json che descrivono un attore
            avete il permesso di usare la libreria re per le espressioni regolari.

    - tutti gli altri metodi che ritenete utili

La classe Film rappresenta la scheda di un film, costruita a partire dalle informazioni json.
Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
all'implementazione dei metodi descritti.

    Implementate i metodi di istanza:
    - Il costruttore riceve come argomento un dizionario ricavato dal file films.json (o file json simile)
        che rappresenta un solo film
        ed assegna tutti i valori possibili agli attributi di istanza a partire dal dizionario json passato.
    - titolo(self)  torna il titolo del film
    - attori(self)  torna l'insieme di istanze di tipo Attore che hanno lavorato al film
    - registi(self) torna l'insieme di istanze di tipo Regista che hanno diretto il film
    - luoghi(self)  torna l'insieme di luoghi in cui è stato fatto il film (campo "COUNTRY" dei dati json)
    - durata(self)  torna la durata minima in minuti (intero) del film (campo "RUNTIME" dei dati json)
    - anno(self)    torna l'anno di produzione del film (dal campo "TITLE" dei dati json)

    - tutti gli altri metodi che ritenete utili

La classe Regista rappresenta la scheda di un regista.
Gli attributi di istanza della classe Regista sono quelli necessari ad implementare i seguenti metodi.

    Implementate i metodi di istanza:
    - Il costruttore della classe assegna il nome.
    - nome(self)    che torna il nome del regista
    - films(self)   che torna l'insieme delle istanze dei Film in cui il regista ha lavorato
    - attore_preferito(self)    che torna l'istanza di tipo Attore che ha lavorato più volte col regista
        In caso di parità si torni l'attore più giovane (vedi metodo Attore.eta())
        In caso di parità si torni l'attore di genere femminile
        In caso di parità quello col vero nome (campo "REALNAME") che viene prima in ordine alfabetico.
        Se il campo REALNAME nel dizionario json non è presente o non contiene un valore usate il campo NAME.
    - anni_di_lavoro(self)    che torna per quanti anni ha lavorato il regista
        a partire dal primo film prodotto all'ultimo compresi (vedi Film.anno())

    - tutti gli altri metodi che ritenete utili

GESTIONE DEGLI ERRORI
I test NON proporranno dati errati per cui ci aspettiamo che NON vengano mai generate eccezioni
e quindi non è necessario che controlliate la validità delle informazioni fornite ai metodi.

"""

##################################################################################################

import re
durata_re = re.compile('([0-9]+) min')
year_re   = re.compile('([0-9]{4})')

##################################################################################################
import json

def leggi_archivio_attori(archivio_attori_json):
    '''legge l'archivio json fornito in input che descrive tutti gli attori
    (con lo stesso formato del file di esempio actors.json)
    e torna un dizionario catalogo_attori { nome -> oggetto di tipo Attore } in cui:
    - le chiavi sono i nomi degli attori
        (prese dal campo "NAME" del dizionario presente per ogni attore nel file json)
    - i valori sono le corrispondenti istanze di tipo Attore create col costruttore passando
        come argomento il dizionario (letto dal file json) che contiene le informazioni dell'attore.
        '''
    with open(archivio_attori_json, encoding='utf8') as f:
        raw_data = json.load(f)
    attori = {}
    for nome, data in raw_data.items():
        attori[nome] = Attore(data)
    return attori

def leggi_archivio_film(archivio_film_json, catalogo_attori):
    '''- leggi_archivio_film(file_json, catalogo_attori)
    - che legge dal file json fornito in input che descrive tutti i film
    (con lo stesso formato del file di esempio films.json)
    - ed inoltre riceve il dizionario catalogo_attori { nome->Attore } prodotto con la funzione precedente
    e torna come risultato una coppia di dizionari ( catalogo_film, catalogo_registi )
    Il catalogo_film deve essere un dizionario { titolo -> oggetto di tipo Film } in cui:
        - le chiavi sono i titoli dei film
            (preso dal campo "TITLE" del dizionario presente per ogni film nel file json)
        - i valori sono le corrispondenti istanze di tipo Film create col costruttore passando
            come argomento il dizionario (letto dal file json) che contiene le informazioni del Film.
    Il catalogo_registi deve essere un dizionario { nome -> oggetto di tipo Regista } in cui:
        - le chiavi sono i nomi dei registi
            ( presi dal campo "DIRECTORS" dei dizionari json che descrivono i film presi dal file json)
        - i valori sono istanze del tipo Regista (di cui vedete la definizione più sotto)

    La funzione leggi_archivio_film deve fare in modo che:
    - all'interno di ciascun oggetto Film siano inseriti gli oggetti Attore in modo che:
        - ogni Attore contenga i Film in cui è comparso
        - ogni Film contenga gli Attori che ci hanno lavorato
    - all'interno di ciascun oggetto Film siano contenuti gli oggetti di tipo Regista in modo che:
        - ogni Film contenga i Registi che l'hanno diretto
        - ogni Regista contenga i Film che ha diretto
    '''
    with open(archivio_film_json, encoding='utf8') as f:
        raw_data = json.load(f)
    films = {}
    registi = {}
    for data in raw_data.values():
        film = Film(data)
        films[film._titolo] = film
        for nome in data['DIRECTORS']:
            if nome not in registi:
                registi[nome] = Regista(nome)
            film._registi.add(registi[nome])
            registi[nome]._films.add(film)
        for nome in data['ACTORS']:
            film._attori.add(catalogo_attori[nome])
            catalogo_attori[nome]._films.add(film)
    return films, registi

##################################################################################################

class Attore():
    '''
    La classe Attore rappresenta la scheda di un attore.
    Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
    per realizzare i metodi seguenti a partire dalle informazioni json ottenute dal file actors.json
    allegato (o da file json simile).
    '''

    # Esempio di blocco dati json
    # "'Baby' Paul Cullen": {
    #     "NAME": [
    #         "'Baby' Paul Cullen"
    #     ],
    #     "LASTFIRST": [
    #         "Cullen, 'Baby' Paul"
    #     ],
    #     "REALNAME": [
    #         "Paul Michael Cullen"
    #     ],
    #     "NICKNAMES": [],
    #     "GENDER": [
    #         "M"
    #     ],
    #     "BIRTH": [
    #         "1962, Ireland"
    #     ],
    #     "DIED": [
    #         "21 July 2009, Los Angeles, California, USA"
    #     ]
    # },

    def __init__(self, data):
        '''riceve un dizionario ottenuto dal file json actors.json (o file simile).
        Il dizionario passato come argomento contiene le informazioni relative ad un solo attore.
        Il costruttore assegna agli attributi tutti i valori possibili a partire dal dizionario json passato.
        '''
        self._nome       = data['NAME'][0]
        self._vero_nome  = self._nome
        if 'REALNAME' in data and data['REALNAME']:
            self._vero_nome = data['REALNAME'][0]
        self._genere      = data['GENDER'][0] if 'GENDER' in data and data['GENDER'] else '' # ???
        self._soprannomi = data['NICKNAMES']
        self._nascita    = None
        self._morte      = None
        self._films      = set()  # da riempire quando si caricano i film
        if 'BIRTH' in data and data['BIRTH'] :
            testo = ' '.join(data['BIRTH'])
            match = year_re.search(testo)
            if match:
                self._nascita = int(match.group())
        if 'DIED' in data and data['DIED'] :
            testo = ' '.join(data['DIED'])
            match = year_re.search(testo)
            if match:
                self._morte = int(match.group())

    def __repr__(self):
        return f"""{self._nome}\t({self._genere})\tn:{self._nascita}\tm:{self._morte}\teta:{self.eta()}"""

    def __str__(self):
        films = '\n\t'.join(repr(f) for f in self._films)
        return f"""{self!r}
        {films}"""

    def nome(self):
        '''restituisce il nome'''
        return self._nome

    def genere(self):
        '''restituisce il genere'''
        return self._genere

    def vero_nome(self):
        '''restituisce il vero nome'''
        return self._vero_nome

    def eta(self):
        '''restituisce un intero che indica l'età dell'attore in anni:
        - se l'anno di nascita NON è presente tornate None (e ignorate questo attore nel metodo Regista.attore_preferito)
        - se l'anno di morte NON è presente usate il 2018 come anno di riferimento
        - altrimenti tornate il numero di anni vissuti
            Es. nato: 1950 oggi: 2018 -> 69
        NOTA: per estrarre l'anno dalle proprieta' "BIRTH" e "DIED" dei dati json che descrivono un attore
              avete il permesso di usare la libreria re per le espressioni regolari.
        '''
        fine = self._morte if self._morte else 2018
        if self._nascita:
            return fine - self._nascita + 1

    def films(self):
        '''restituisce il set di film in cui ha lavorato'''
        return self._films

    def registi(self):
        '''restituisce un set contenente le istanze di oggetti di tipo Regista,
        con cui l'attore ha girato almeno un film.'''
        return {regista
                for film in self._films
                for regista in film._registi}

    def regista_preferito(self):
        '''restituisce un'istanza di un oggetto Regista, che rappresenta il regista con cui l'attore
        ha girato più film.
        In caso di pareggio, viene preso il regista il cui nome viene prima in ordine alfabetico.
        '''
        conta   = {}
        for film in self._films:
            for regista in film._registi:
                conta[regista] = conta.get(regista, 0) + 1
        return min(conta, key=lambda r: (-conta[r], r.nome()))

    def coprotagonisti(self):
        '''
        restituisce un set contenente le istanze di oggetti di tipo Attore,
        che rappresentano tutti gli attori con cui l'attore self ha girato almeno un film.
        '''
        return { attore for film in self._films
                        for attore in film._attori
                        if attore != self
                 }

    def in_coppia(self, partner=None):
        '''restituisce:
          Se il parametro partner (stringa) NON viene specificato:
            - un set di tuple: ogni tupla è del tipo (a_f, a_m, n_f),
            dove a_f e a_m sono due istanze di oggetto di tipo Attore
            (di cui una rappresenta l'attore self), di genere diverso (campo "GENDER" dei dati json)
            (a_f è femmina e a_m è maschio) ed n_f è il numero di film in cui self e il suo partner
            hanno fatto coppia (ovvero hanno girato PIU' DI UN film assieme).
          Se il parametro partner VIENE specificato (di tipo stringa), viene restituito invece
            - il set di tutti i Film (che può essere vuoto) in cui l'attore self e l'attore partner che ha quel nome
            hanno fatto coppia (ovvero hanno girato ALMENO quel film assieme).
        '''
        if partner:
            return {
                    film    for film in self._films
                            for attore in film._attori
                            if  attore._nome == partner
                    }
        else:
            conteggio = {}
            altrosesso = 'M' if self._genere == 'F' else 'F'  # what if GENDER non specificato?
            for film in self._films:
                for attore in film._attori:
                    if attore._genere == altrosesso:
                        conteggio[attore] = conteggio.get(attore, 0) + 1
            if altrosesso == 'M':
                return {(a, self, conteggio[a]) for a in conteggio if conteggio[a] > 1 }
            else:
                return {(self, a, conteggio[a]) for a in conteggio if conteggio[a] > 1 }

    def luogo_preferito(self):
        '''restituisce la stringa con il paese in cui l'attore self ha girato più film.
        In caso di pareggio, viene restituito il luogo che viene prima in ordine alfabetico.
        Se non esiste si torna None
        '''
        conta = {}
        for film in self._films:
            for luogo in film._luoghi:
                conta[luogo] = conta.get(luogo, 0) + 1
        return min(conta, key=lambda l: (-conta[l], l), default=None)

    def film_durata(self, inf=0, sup=None):
        '''restituisce la lista delle istanze degli oggetti di tipo Film,
        dei film in cui l'attore self ha recitato e che durano almeno inf minuti e,
        se sup è specificato, massimo sup minuti.
        La lista deve essere ordinata per durata dei film in ordine crescente.
        In caso di parità per titolo crescente in ordine alfabetico.
        Se nel file json sono specificate più durate per lo stesso film, usate la durata minore.
        Se nei dati json la durata non è indicata ignorate quel film.
          NOTA: per estrarre la durata dalla proprieta' "RUNTIME" dei dati json che descrivono un film
                avete il permesso di usare la libreria re per le espressioni regolari.
        '''
        if sup:
            lista = [film for film in self._films if film.durata() and inf <= int(film.durata()) <= sup]
        else:
            lista = [film for film in self._films if film.durata() and inf <= int(film.durata())]
        # print(f"\n\n{self._nome}: {lista}")
        return sorted(lista, key=lambda film: (film.durata(), film._titolo))



##################################################################################################
# Esempio di voce json che descrive un film estratta dal file films.json
##################################################################################################
# "10 Things I Hate About You;1999": {
#     "TITLE": [
#         "10 Things I Hate About You",
#         "1999"
#     ],
#     "ACTORS": [
#         "Heath Ledger",
#         "Julia Stiles",
#         "Joseph Gordon-Levitt",
#         "Larisa Oleynik",
#         "David Krumholtz",
#         "Andrew Keegan",
#         "Susan May Pratt",
#         "Gabrielle Union",
#         "Larry Miller",
#         "Daryl Mitchell",
#         "Allison Janney",
#         "David Leisure",
#         "Greg Jackson",
#         "Kyle Cease",
#         "Terence Heuston"
#     ],
#     "DIRECTORS": [
#         "Gil Junger"
#     ],
#     "WRITERS": [
#         "Karen McCullah Lutz",
#         "Kirsten Smith",
#         "and 1 more credit"
#     ],
#     "GENRES": [
#         "Comedy",
#         "Romance"
#     ],
#     "COUNTRY": ["USA"],
#     "LANGUAGE": [
#         "English",
#         "French"
#     ],
#     "RUNTIME": ["97 min"],
#     "IMDB_URL": ["http://www.imdb.com/title/tt0147800/"],
#     "POSTER": [ "http://ia.media-imdb.com/images/M/MV5BMTI4MzU5OTc2MF5BMl5BanBnXkFtZTYwNzQxMjc5._V1._SY317_CR4,0,214,317_.jpg"]
# },

class Film():
    '''
    La classe Film rappresenta la scheda di un film, costruita a partire dalle informazioni json.
    Al suo interno devono essere definiti tutti gli attributi di istanza che ritenete necessari
    all'implementazione dei metodi descritti.
    '''
    def __init__(self, data):
        '''riceve come argomento un dizionario ricavato dal file films.json (o file json simile)
            che rappresenta un solo film
            ed assegna tutti i valori possibili agli attributi di istanza a partire dal dizionario json passato.
        '''
        self._titolo, self._year= data['TITLE']
        self._year = int(self._year)
        self._durata            = None
        self._lingue            = data['LANGUAGE']
        self._luoghi            = set(data['COUNTRY'])
        self._generi            = set(data['GENRES'])
        self._autori            = set(data['WRITERS'])
        self._url               = data['IMDB_URL']
        self._poster            = data['POSTER']
        self._attori            = set()
        self._registi           = set()
        if data['RUNTIME']:
            durate = durata_re.findall("".join(data['RUNTIME']))
            self._durata = min(map(int, durate), default=None)

    def __repr__(self):
        return f"{self._titolo} ({self._year} - {self._durata} min)"

    def attori(self):
        '''torna l'insieme di istanze di tipo Attore che hanno lavorato al film'''
        return self._attori

    def registi(self):
        '''torna l'insieme di istanze di tipo Regista che hanno diretto il film'''
        return self._registi

    def luoghi(self):
        '''torna l'insieme di luoghi in cui è stato fatto il film (campo "COUNTRY" dei dati json)'''
        return self._luoghi

    def durata(self):
        '''torna la durata minima in minuti (intero) del film (campo "RUNTIME" dei dati json)'''
        return self._durata

    def titolo(self):
        return self._titolo

    def anno(self):
        '''torna l'anno di produzione del film (dal campo "TITLE" dei dati json)'''
        return self._year

##################################################################################################

class Regista:
    '''
    La classe Regista rappresenta la scheda di un regista.
    Gli attributi di istanza della classe Regista sono quelli necessari ad implementare i seguenti metodi.
    '''
    def __init__(self, nome):
        '''Il costruttore assegna il nome.'''
        self._nome  = nome
        self._films = set()

    def __repr__(self):
        return self._nome

    def films(self):
        '''torna l'insieme delle istanze dei Film in cui il regista ha lavorato'''
        return self._films

    def nome(self):
        '''torna il nome del regista'''
        return self._nome

    def attori(self):
        return { attore for film   in self._films
                        for attore in film._attori }

    def attore_preferito(self):
        '''torna l'istanza di tipo Attore che ha lavorato più volte col regista
            In caso di parità si torni l'attore più giovane (vedi metodo Attore.eta())
            In caso di parità si torni l'attore di genere femminile
            In caso di parità quello col vero nome (campo "REALNAME") che viene prima in ordine alfabetico.
            Se il campo REALNAME nel dizionario json non è presente o non contiene un valore usate il campo NAME.
        '''
        conta = {}
        for film in self._films:
            for attore in film._attori:
                if attore.eta() and attore.genere():
                    conta[attore] = conta.get(attore, 0) + 1
        return min(conta, key=lambda a: (-conta[a], a.eta(), a.genere(), a.vero_nome()), default=None)

    def anni_di_lavoro(self):
        '''torna per quanti anni ha lavorato il regista a partire dal primo film prodotto all'ultimo
        compresi (vedi Film.anno())
        '''
        anni = [ f.anno() for f in self._films]
        if anni:
            inizio = min(anni)
            fine   = max(anni)
            return fine - inizio + 1



if __name__ == '__main__':
    attori          = leggi_archivio_attori('actors.json')
    films, registi  = leggi_archivio_film('films.json', attori)
    a = attori['Monica Vitti']
    f = list(a.films())
    print(a,
          'regista preferito', a.regista_preferito(),
          'colleghi', [x.nome() for x in sorted(a.coprotagonisti(), key=lambda attore: attore.nome())],
          sep='\n')
    r = list(a.registi())[0]
    r = registi['Michelangelo Antonioni']
    print(r,
          'attore preferito', r.attore_preferito(),
          sep='\n')
    for film in f:
        print(film, film.durata())
    for m, f, n in a.in_coppia():
        print(f"{m.nome()} - {f.nome()} \t {n}")


    def conta(insieme, chiave, messaggio):
        count = 0
        for a in insieme:
            if not chiave(a):
                count += 1
        #print(messaggio, count)

    #conta(films.values(),   lambda f: f.registi(),          "FILMS WITHOUT DIRECTOR")
    #conta(films.values(),   lambda f: f.luoghi(),           "FILMS WITHOUT PLACES")
    #conta(attori.values(),  lambda a: a.genere(),           "ACTORS WITHOUT GENDER")
    #conta(attori.values(),  lambda a: a.eta(),              "ACTORS WITHOUT AGE")
    #conta(attori.values(),  lambda a: a._morte,             "ACTORS WITHOUT DIED")
    #conta(attori.values(),  lambda a: a.coprotagonisti(),   "ACTORS WITHOUT COWORKERS")
    #conta(attori.values(),  lambda a: a.registi(),          "ACTORS WITHOUT DIRECTORS")
    #conta(attori.values(),  lambda a: a.films(),            "ACTORS WITHOUT MOVIES")
    #conta(registi.values(), lambda r: r.attore_preferito(), "DIRECTORS WITHOUT PREFERRED ACTOR")

    #for f in films.values():
    #    if len(f._luoghi) > 1:
    #        print(f, f._luoghi)
