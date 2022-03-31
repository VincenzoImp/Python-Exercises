import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program02 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, lmosse, k,expected):
        '''Implementazione del test
            - ls:    	 la lista di partenza
            - lmosse:    la lista delle mosse
            - k:    	 il numero di passi di trasformazione
            - expected:  la lista risultante
        '''
        self.maxDiff = None
        ls1=ls.copy()
        lmosse1=lmosse.copy()
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(0.5):    # mezzo secondo di timeout
            result   = program.es2(ls,lmosse,k)
        self.assertEqual(ls1,          ls,       "la lista originale ls non va modificata")
        self.assertEqual(lmosse1,      lmosse,   "la lista originale lmosse non va modificata")
        self.assertEqual(type(result), list,     "il risultato prodotto non e' una lista")
        self.assertEqual(result,       expected, "la lista restituita non e' corretta")

    def test_1_n9_k5(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
                    [1, 0, 5, 2, 8, 4, 3, 7, 6], 
                    5,
                    [2, 1, 6, 3, 9, 5, 4, 8, 7])

    def test_2_n9_k370(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 0, 5, 2, 8, 4, 3, 7, 6],  
                    370,
                    [1, 2, 5, 6, 7, 9, 3, 8, 4])

    def test_3_n9_k81000(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 0],  
                    81000,
                    [1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_4_n9_k81002(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 0],  
                    81002,
                    [8, 9, 1, 2, 3, 4, 5, 6, 7])

    def test_5_n29_k270001(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                    [1, 2, 3, 4, 5, 6, 7, 8, 0,  10, 11, 12, 13, 14, 15, 16, 17, 18, 9,  20, 21, 22, 23, 24, 25, 26, 27, 28, 19], 
                    270001,
                    [9, 1, 2, 3, 4, 5, 6, 7, 8, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 29, 20, 21, 22, 23, 24, 25, 26, 27, 28] 
        )

    def test_6_n26_k320010(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
                    [1, 2, 3, 0, 5, 6, 7, 8, 9,  10, 11,  4, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 12], 
                    320010,
                    [3, 4, 1, 2, 11, 12, 5, 6, 7, 8, 9, 10, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 13, 14, 15, 16, 17, 18]
        )

    def test_7_n59_k270341(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, ], 
                    [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 38, 15, 16, 1, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 57, 0, 
                    31, 32, 33, 34, 35, 36, 5, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 18, 53, 26, 54, 55, 56, 58, ], 
                    270341,
                    [19, 33, 21, 34, 23, 10, 35, 25, 13, 36, 28, 39, 37, 31, 40, 32, 41, 42, 27, 43, 30, 44, 1, 45, 3, 46, 52, 5, 47, 53, 
                    8, 11, 14, 16, 2, 4, 7, 38, 6, 9, 12, 15, 17, 18, 20, 22, 24, 26, 29, 58, 57, 56, 55, 54, 51, 50, 49, 48, 59]
        )

    def test_8_n33_k1000000(self):
        return self.do_test(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, ],
                    [2, 1, 4, 5, 3, 7, 8, 9, 6,  11, 12, 13, 14, 15, 10, 17, 18, 19, 20, 21, 22, 23, 16, 25, 26, 27, 28, 29, 30, 31, 32,  0, 24, ],
                    1000000,
                    [14, 2, 16, 20, 18, 22, 7, 24, 9, 26, 15, 28, 11, 30, 13, 32, 17, 1, 19, 3, 21, 5, 23, 4, 25, 6, 27, 8, 29, 10, 31, 12, 33]
        )

if __name__ == '__main__':
    Test.main()

