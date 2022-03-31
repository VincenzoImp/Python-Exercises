import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, n, c, k,expected):
        '''Implementazione del test
            - n:    interi presenti nella sequenza circolare
            - c:    intero con il numero di passi da fare per selezionare l'intero da cancellare
            - k:    interi che devono restare nella sequenza
            - expected: la lista attesa
        '''
        self.maxDiff = None
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(1):
            result   = program.es1(n,c,k)
        self.assertEqual(type(result),  list,     "il risultato prodotto non e' una lista")
        self.assertEqual(result,        expected, "la lista  restituita non e' corretta")

    def test_1_n9_c5_k2(self):
        '''Per n=9,c=5 e k=2 la funzione deve restituire la lista [7,8]'''
        return self.do_test(9, 5, 2,[7,8])

    def test_2_n6_c6_k3(self):
        '''Per n=6, c=6 e k=3 la funzione deve restituire la lista [2,4,5]'''
        return self.do_test(6, 6, 3,[2,4,5])

    def test_3_n5_c12_k2(self):
        '''Per n=5, c=12 e k=2 la funzione deve restituire la lista [1,2]'''
        return self.do_test(5, 12, 2,[1,2])
    
    def test_4_n1000_c0_k5(self):
        return self.do_test(1000, 1, 5,[209, 465, 721, 849, 977])

    def test_5_n1000_c999_k5(self):
        return self.do_test(1000, 999, 5, [488, 498, 579, 609, 850])

    def test_6_n7523_c8599_k10(self):
        return self.do_test(7523, 8599, 10,[41, 954, 1140, 1277, 2459, 2817, 3872, 4644, 5937, 6782])

    def test_7_n38239_c719_k6(self):
        return self.do_test(38239, 719, 6,[4037, 9026, 17615, 36375, 36635, 37588])

    def test_8_n50000_c877_k5(self):
        return self.do_test(50000, 877, 5,[10170, 18402, 19913, 35689, 45094])

    def test_9_n100000_c200000_k5(self):
        return self.do_test(100000, 200000, 5,[10153, 38628, 65057, 66893, 89103])

if __name__ == '__main__':
    Test.main()

