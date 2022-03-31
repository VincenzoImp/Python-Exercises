import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program01 as program

@ddt
class Test(testlib.TestCase):

    # TODO: aggiungere test di ricorsione

    def do_test(self, fileInJSON, fileOutJSON, expected, expectedJSON):
        '''Implementazione del test
            - fileInJSON    : file JSON che contiene l'elenco degli archi
            - fileOutJSON   : file JSON da creare
            - expected      : numero atteso di alberi nella foresta
            - expectedJSON  : file JSON come deve venire
        '''

        # prima controlliamo che l'implementazione sia ricorsiva
        try:
            isrecursive.decorate_module(program)
            program.es1(fileInJSON, fileOutJSON)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        # poi controlliamo che faccia quello che deve fare
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'), \
             self.timer(2):
            result = program.es1(fileInJSON, fileOutJSON)
        self.assertEqual(type(result),  int,      "Il risultato non è un intero")
        self.assertEqual(result,        expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_json_file(fileOutJSON, expectedJSON)

    @data(  
            ('es1_f1.json',             'es1_test1.json',    3, 'es1_risTest1.json'),
            ('es1_f2.json',             'es1_test2.json',   20, 'es1_risTest2.json'),
            ('es1_100e_100n.json',      'es1_test3.json',    7, 'es1_risTest3.json'),
            ('es1_200e_200n.json',      'es1_test4.json',   31, 'es1_risTest4.json'),
            ('es1_1000e_1000n.json',    'es1_test5.json',  510, 'es1_risTest5.json'),
            ('es1_10000e_10000n.json',  'es1_test6.json', 4911, 'es1_risTest6.json'),
            ('es1_100000e_100010n.json','es1_test7.json',   10, 'es1_risTest7.json'),
            ('es1_segreto_10_liste_da_100.json',  'es1_test_segreto1.json', 10, 'es1_risTest_segreto1.json'),
            ('es1_segreto_10_casuali_1000e.json', 'es1_test_segreto2.json', 10, 'es1_risTest_segreto2.json'),
            )
    @unpack
    def test(self, fileInJSON, fileOutJSON, expected, expectedJSON):
        return self.do_test(fileInJSON, fileOutJSON, expected, expectedJSON)

if __name__ == '__main__':
    Test.main()
