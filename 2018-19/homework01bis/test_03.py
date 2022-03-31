import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, parole, testo, expected):
        '''Implementazione del test
            - parole:    la lista di parole
            - testo:     il testo da anagrammare
            - expected:  la terna di parole trovata
        '''
        parole_bis = parole.copy()
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(2):  # timeout di 2 secondi
            result   = program.es3(parole_bis,testo)
        self.assertTrue(type(result) in [tuple, type(None)],    "il risultato deve essere una tupla oppure None")
        self.assertEqual(result, expected,                      f"il risultato deve essere {expected} invece di {result}")
        self.assertEqual(parole_bis, parole,                    "la lista di parole originale NON deve essere modificata")

    @data( 
                    ['1000_parole_italiane_comuni.txt',             'questa frase e troppo lunga',  None ],
                    ['1000_parole_italiane_comuni.txt',             'Origamisti Romani',            ('ministro', 'magari', 'io')       ],
                    ['60000_parole_italiane.txt',                   'Angelo Monti',                 ('tono', 'negli', 'ma')            ],
                    ['60000_parole_italiane.txt',                   'Angelo Spognardi',             ('sragion', 'pend', 'lago')        ],
                    ['60000_parole_italiane.txt',                   'Andrea Sterbini',              ('treni', 'sia', 'brande')         ],
                    ['95000_parole_italiane_con_nomi_propri.txt',   'Ascanio Celestini',            ('tossina', 'nicea', 'cile')       ],
                    ['95000_parole_italiane_con_nomi_propri.txt',   'La Settimana Enigmistica',     ('tsantsa', 'immagine', 'etilica') ],
                    ['110000_parole_italiane_con_nomi_propri.txt',  'Marilyn Monroe',               None                               ],
                    ['110000_parole_italiane_con_nomi_propri.txt',  'Zero Calcare',                 ('zero', 're', 'lacca')            ],
                    ['110000_parole_italiane_con_nomi_propri.txt',  'Pink Floyd',                   None                               ],
                    ['60000_parole_italiane.txt',                   'Douglad Noel Adams',           ('usando', 'dogma', 'della')       ],
        )
    @unpack
    def test_parole(self, file_parole, testo, expected):
        with open(file_parole, encoding='utf8') as f:
            parole=f.read().split()
        self.do_test(parole, testo, expected)

if __name__ == '__main__':
    Test.main()

