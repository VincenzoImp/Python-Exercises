import testlib
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, nome, colore, tripla, expected):
        '''Implementazione del test
            - nome         : parte del nome del file di input
            - colore       : nome del colore cercato
            - tripla       : tupla del colore cercato
            - expected     : numero atteso di pixel dell'area massima dei colore
        '''
        fileInPNG   = f"es1_{nome}.png"                 # file PNG che contiene l'immagine di partenza
        fileOutPNG  = f"es1_test_{nome}_{colore}.png"   # file PNG che deve essere creato
        expectedPNG = f"es1_Ris_{nome}_{colore}.png"    # file PNG della immagine attesa

        with self.ignored_function('builtins.print'), \
             self.ignored_function('pprint.pprint'), \
             self.timer(5):
            result = program.es1(fileInPNG, tripla, fileOutPNG)
        self.assertEqual(type(result), int,      "Il risultato dev'essere un intero")
        self.assertEqual(result,       expected, "Il risultato dev'essere {expected} invece che {result}")
        self.check_img_file(fileOutPNG, expectedPNG)

    @data(  
            ("f1", 'rosso',  (255,  0,  0),  400 ),
            ("f1", 'nero',   (  0,  0,  0), 3641 ),
            ("f2", 'nero',   (  0,  0,  0), 1600 ),
            ("f2", 'azzurro',(  0,125,255), 7121 ),
            ("f3", 'nero',   (  0,  0,  0), 5351 ),
            ("f3", 'verde',  (100,250,  0), 3500 ),
            ("f3", 'bianco', (255,255,255),  500 ),
            ("f4", 'verde',  ( 26,188,156), 10000),
            ("f4", 'azzurro',( 52,152,219), 10000),
            ("f5", 'nero',   (  0,  0,  0), 2265 ),
            ("f5", 'platino',(221,221,221), 11582),
            ("f5", 'angolo', (221,221,222), 3114 ),
            ("f6", 'bianco', (255,255,255), 2692 ),
            ("f6", 'blu',    (  5, 61,138), 1943 ),
            ("f6", 'fucsia', (231, 61,138),  210 ),
            )
    @unpack
    def test(self, nome, colore, tripla, expected):
        return self.do_test(nome, colore, tripla, expected)

if __name__ == '__main__':
    Test.main()

