import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program03 as program

@ddt
class Test(testlib.TestCase):

    # TODO: aggiungere test di ricorsione

    def do_test(self, path, filePNG, expected, expectedPNG):
        '''Implementazione del test
            - path:         directory da esplorare
            - filePNG:      file .PNG in cui registrare la foto prodotta
            - expected:     coppia (larghezza, altezza) attesa
            - expectedPNG:  nome del file PNF di confronto
        '''

        # prima controlliamo che l'implementazione sia ricorsiva
        try:
            isrecursive.decorate_module(program)
            program.es3(path, filePNG)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        # poi controlliamo che faccia quello che deve fare
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'), \
             self.timer(4):
            result   = program.es3(path,filePNG)
        self.assertEqual(type(result),  tuple,      "Il risultato non è una tupla")
        self.assertEqual(len(result),   2,          "Il risultato non è una tupla di 2 elementi")
        self.assertEqual(result,        expected,   f"Il risultato non è la tupla {expected} ma {result}")
        self.check_img_file(filePNG, expectedPNG)

    @data(
            ['dirs/Informatica', 'es3_test1.png', (130,   82), 'es3_risTest1.png'],
            ['dirs/12345678901234567890123456789012345678901234567890',
                                 'es3_test2.png', ( 50,   13), 'es3_risTest2.png'],
            ['dirs/A1',          'es3_test3.png', (130,  379), 'es3_risTest3.png'],
            ['dirs/t1',          'es3_test4.png', ( 90,  430), 'es3_risTest4.png'],
            ['dirs/t4',          'es3_test5.png', ( 90,  439), 'es3_risTest5.png'],
            ['dirs/t2',          'es3_test6.png', (110,  490), 'es3_risTest6.png'],
            ['dirs/t3',          'es3_test7.png', (110,  769), 'es3_risTest7.png'],
            ['dirs',             'es3_test8.png', (150, 2617), 'es3_risTest8.png'],
            ['segreto1',         'es3_test_segreto1.png', (130,  82), 'es3_risTest_segreto1.png'],
            ['segreto2',         'es3_test_segreto2.png', (230, 775), 'es3_risTest_segreto2.png'],
            )
    @unpack
    def test(self, path, filePNG, expected, expectedPNG):
        return self.do_test(path, filePNG, expected, expectedPNG)

if __name__ == '__main__':
    Test.main()

