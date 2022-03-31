#! /usr/bin/env python3 -B

from testlib import check, runtests, check_text_file, check_img_file, check_json_file
import isrecursive

import albero

import program1

###############################################################################
def test_nome_cognome_matricola():
    assert program1.nome        != 'NOME',      "ATTENZIONE, NON HAI INSERITO IL TUO NOME NEL FILE program.py !!!"
    assert program1.cognome     != 'COGNOME',   "ATTENZIONE, NON HAI INSERITO IL TUO COGNOME NEL FILE program.py !!!"
    assert program1.matricola   != 'MATRICOLA', "ATTENZIONE, NON HAI INSERITO LA TUA MATRICOLA NEL FILE program.py !!!"
    return 0

###############################################################################

def test_es10a(R, lista1, expected):
    lista1bis = lista1.copy()
    ris = program1.es10(R,lista1)
    check(lista1,lista1bis,None,"la funzione NON deve modificare la lista")
    check(type(ris),set,None," bisogna restituire un insieme")
    check(ris, expected, None, " la risposta non e' corretta")
    return 1

def test_es10a_1():
    ''' \nPrimo test della funzione es1 con R= (2,4,6,2) e lista1=[(3,6,5,1),(6,6,7,5),(1,8,8,1)]'''
    R= (2,4,6,2)
    lista1=[(3,6,5,1),(6,6,7,5),(1,8,8,1)]
    expected = {0,2}
    return test_es10a(R, lista1, expected)

def test_es10a_2():
    ''' \nSecondo test della funzione es1 con R= (2,4,5,1) e lista2=[(3,3,4,2),(4,5,6,3),(6,7,8,5),(0,8,9,0)]'''
    R= (2,4,5,1)
    lista2=[(3,3,4,2),(4,5,6,3),(6,7,8,5),(0,8,9,0)]
    expected = {0, 1, 3}
    return test_es10a(R, lista2, expected)
    
def test_es10a_3():
    ''' \nTerzo test della funzione es1 con R= (3,7,7,3) e 
    lista3=[(4,6,5,5),(6,4,7,3),(8,2,9,1),(7,7,9,5),(1,3,3,3)]'''
    R= (3,7,7,3)
    lista3=[(4,6,5,5),(6,4,7,3),(8,2,9,1),(7,7,9,5),(1,3,3,3)]
    expected = {0, 1, 3, 4}
    return test_es10a(R, lista3, expected)

##########################################################################################

def test_es1a( lis1, ris1 ):
    '''\nPrimo test della funzione es1 con lis=[7,4,3,25,5,2,12,24,13,14]'''
    lis1bis = lis1.copy()
    ris= program1.es1(lis1)
    check(lis1,lis1bis,None,"la funzione NON deve modificare la lista")
    check(type(ris),list,None,"la funzione deve restituire una lista")
    check(ris,ris1,None,"la lista restituita non e' corretta")
    return 1

def test_es1a_1():
    '''\nPrimo test della funzione es1 con lis=[7,4,3,25,5,2,12,24,13,14]'''
    lis1=[7,4,3,25,5,2,12,24,13,14]
    ris1=[(3, 4, 5), (5, 12, 13), (7, 24, 25)]
    return test_es1a(lis1, ris1)

def test_es1a_2():
    '''\nSecondo test della funzione es1 con lis=[60,11,61,28,45,53,3,4,5,12,13,90]'''
    lis2=[60,11,61,28,45,53,3,4,5,12,13,90]
    ris2=[(3, 4, 5), (5, 12, 13), (11, 60, 61), (28, 45, 53)]
    return test_es1a(lis2, ris2)

def test_es1a_3():
    '''\nTerzo test della funzione es1 con lis=[70,71, ...,150]'''
    lis3=[x for x in range(70,151)]
    ris3=[(72, 96, 120), (75, 100, 125), (78, 104, 130), (80, 84, 116), 
          (81, 108, 135),(84, 112, 140), (87, 116, 145), (88, 105, 137), 
          (90, 120, 150), (96, 110, 146), (100, 105, 145)]
    return test_es1a(lis3, ris3)
    
################################################################################

def test_es4a_1():
    '''\nPrimo test della funzione es4 sul file f4a.txt'''
    ris1=3
    ris= program1.es4('f4a.txt')
    check(ris,ris1,None,"la risposta  non e' corretta")
    return 2
    
def test_es4a_2():
    '''\nSecondo test della funzione es4 sul file f4b.txt'''
    ris2=8
    ris= program1.es4('f4b.txt')
    check(ris,ris2,None,"la risposta  non e' corretta")
    return 2
    
def test_es4a_3():
    '''\nTerzo test della funzione es4 sul file f4c.txt'''
    ris3=0
    ris= program1.es4('f4c.txt')
    check(ris,ris3,None,"la risposta  non e' corretta")
    return 2
    
################################################################################


def test_es5a_1():
    '''\nPrimo test della funzione es1 con f5a.png '''
    ris1=(20,10)
    ris= program1.es5('f5a.png')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris1,None,"la tupla restituita non e' corretta")
    return 2

def test_es5a_2():
    '''\nSecondo test della funzione es1 con f5b.png'''
    ris2=(20,0)
    ris= program1.es5('f5b.png')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris2,None,"la tupla restituita non e' corretta")
    return 2

def test_es5a_3():
    '''\nTerzo test della funzione es1 con f5c.png'''
    ris3=(20,5)
    ris= program1.es5('f5c.png')
    check(type(ris),tuple,None,"la funzione deve restituire una tupla")
    check(ris,ris3,None,"la tupla restituita non e' corretta")
    return 2
    
################################################################################

def test_es100a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program1)
        program1.es100(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program1)
    
    tree1   = albero.fromLista(lista1)
    ris= program1.es100(tree1)
    check(type(ris),list,None,"bisogna restituire una lista")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 2


def test_es100a_1():
    '''\nPrimo test della funzione es1 con  albero:
    
               5
      ________|_____________
     |          |           |
     20         4           6
     |     _____|______  
     11   |   |  |  |  |
          10  2  9  8  7
            __|__   
           |     |
           3     1 

    '''
    listaA1= [5, [[20, [[11, []]]], [4, [[10, []], [2, [[3, []], [1, []]]], [9, []], 
    [8, []],[7, []]]],[6, []]]]
    lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20] 
    return test_es100a(listaA1,lista1)

def test_es100a_2():
    '''\nSecondo test della funzione es1 con  albero:
    
                    7               
             _______|______         
            |              |        
            5              9        
         ___|___        ___|__      
        |       |      |      |     
        10      8      3      1     
       _|_     _|_    _|_    _|_    
      |   |   |   |  |   |  |   |   
      1   2   12  13 15  6  4   0   
                                     
 
    '''
    listaA2=[7,[[5,[[10,[[1,[]],[2,[]]]],[8,[[12,[]],[13,[]]]]]],[9,[[3,[[15,[]],[6,[]]]],
    [1,[[4,[]],[0,[]]]]]]]]
    lista2=[0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15] 
    return test_es100a(listaA2,lista2)

def test_es100a_3():
    '''\nTerzo test della funzione es1 con  albero:
    
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |      |        |       
   15             80           71     39        100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
5     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______     |      |   
  |       |  |      |       |     |     |    |      |   
  181     28 94     29      70    83    8   81     44   
                                        |               
                                       30               
                                       _|_              
                                      |   |             
                                     46  21             

    '''
    listaA3= [76, [[12, [[15, [[5, []], [19, [[181, []], [28, []]]]]], 
    [80, [[47, [[94, []], [29, []]]],[96, []]]]]], [37, [[71, [[92, []], 
    [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
    [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
    lista3=[5, 8, 12, 15, 19, 21, 23, 28, 29, 30, 37, 39, 44, 46, 47, 67, 70, 71, 76, 
            80, 81, 83, 92, 94, 96, 100, 121, 181]
    return test_es100a(listaA3,lista3)

################################################################################

def test_es2a(lista1, expected):
    tree1   = albero.fromLista(lista1)
    try:
        isrecursive.decorate_module(program1)
        program1.es101(tree1)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program1)
    
    tree1   = albero.fromLista(lista1)
    ris= program1.es101(tree1)
    check(type(ris),list,None,"bisogna restituire una lista")
    check(type(ris[0]),tuple,None,"la lista deve contenere tuple")
    check(ris,expected,None,"la lista  restituita non e' corretta")
    return 1

def test_es101a_1():
    '''\nPrimo test della funzione es101 con tree uguale all'albero in basso a sinistra
                                  
               5                  
      ________|_____________      
     |          |           |     
     20         4           6     
     |     _____|______           
     |    |   |  |  |  |          
     12   10  2  9  8  7          
            __|__                 
           |     |                
           30   22               

    '''
    listaA1= [5, [[20, [[12, []]]], [4, [[10, []], [2, [[30, []], [22, []]]], 
    [9, []], [8, []],[7, []]]],[6, []]]]
    lista1=[(5,), (22, 30), (4, 6, 20), (2, 7, 8, 9, 10, 12)] 
    return test_es2a(listaA1,lista1)

def test_es101a_2():
    '''\nSecondo test della funzione es101 con tree uguale all'albero in basso a sinistra
    
                    10                 
             _______|______            
            |              |           
            3              7           
         ___|___        ___|__         
        |       |      |      |        
        1       2      3      4        
                                       
    '''
    listaA2=[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]]
    lista2=[(10,), (3, 7), (1, 2, 3, 4)] 
    return test_es2a(listaA2,lista2)


def test_es101a_3():
    '''\nTerzo test della funzione es10 con tree uguale all'albero in basso a sinistra
    
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |      |        |       
   15             80           71     39        100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
50     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______     |      |   
  |       |  |      |       |     |     |    |      |   
  181     28 94     5      70     83    8   81     44   
                                        |               
                                       30               
                                       _|_              
                                      |   |             
                                     46  21             
    '''
    listaA3= [76, [[12, [[15, [[50, []], [19, [[181, []], [28, []]]]]],
    [80, [[47, [[94, []], [5, []]]],[96, []]]]]], [37, [[71, [[92, []], 
    [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
    [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
    lista3=[(30,), (76,), 
            (12, 37), (21, 46),
            (15, 39, 71, 80, 100), 
            (19, 23, 47, 50, 67, 92, 96, 121), 
            (5, 8, 28, 44, 70, 81, 83, 94, 181)
            ] 
    return test_es2a(listaA3,lista3)

###############################################################################

def test_es200(dirpath, testo, expected, soglia):
    try:
        isrecursive.decorate_module(program1)
        program1.es200(dirpath, testo, soglia)
    except isrecursive.RecursionDetectedError:
        pass
    else:
        raise Exception("Recursion not present")
    finally:
        isrecursive.undecorate_module(program1)
    result = program1.es200(dirpath, testo, soglia)
    check(type(result),dict,None,"bisogna restituire un dizionario")
    for k, v in result.items():
        check(type(k),str,None,"le chiavi del dizionario devono essere stringhe (nomi di file)")
        check(type(v),int,None,"i valori del dizionario devono essere interi")
    check(result,expected,None,"il dizionario è sbagliato")
    return 2

def test_es200_1():
    dirpath = 'dirs/Disney'
    testo   = 'Topolino'
    soglia  = 1
    expected= {'Topolinia.txt': 2, 'Paperopoli.txt': 1} 
    return test_es200(dirpath, testo, expected, soglia)


def test_es200_2():
    dirpath = 'dirs/E3'
    testo   = 'doccia'
    soglia  = 2
    expected= {'spopolate.txt': 2, 'spiazzamento.pdf': 2, 'refrattari.pdf': 2, 'pria.jpg': 2, 
            'esaustivo.txt': 2, 'agonizzerebbe.odt': 2, 'stanzierebbero.odt': 2, 'immaginassi.doc': 3}
    return test_es200(dirpath, testo, expected, soglia)

def test_es200_3():
    dirpath = 'dirs/E5'
    testo   = 'trachea'
    soglia  = 3
    expected= {'notevoli.doc': 5, 'ventimiglia.ods': 4, 'serrerò.doc': 4, 'ricovereranno.doc': 4, 
            'proiettavi.png': 4, 'gridavate.odt': 4, 'condotto.docx': 4, 'suggestioni.ods': 3, 
            'stritolavo.doc': 3, 'selezionammo.odt': 3, 'ossidiana.odt': 3, 'ingrassi.doc': 3, 
            'dedicasti.pdf': 3, 'congedavate.docx': 3, 'cambieresti.doc': 3, 'assesterò.pdf': 3, 
            'accrescevano.txt': 3, 'accasavo.txt': 3, 'narrandosi.pdf': 4, 'ungendo.doc': 3, 
            'scambiavate.ods': 3, 'guardalo.png': 3, 'frugando.docx': 3, 'festeggiante.odt': 3, 
            'allagaste.odt': 3, "dell'iniziale.png": 4, 'sbattiate.docx': 3, 'ingelosire.doc': 3, 
            'santificherete.ods': 4, 'imprecassi.txt': 4, 'tetano.jpg': 3}
    return test_es200(dirpath, testo, expected, soglia)

###############################################################################


tests = [
    test_nome_cognome_matricola,
    test_es10a_1, test_es10a_2, test_es10a_3,
    test_es1a_1, test_es1a_2, test_es1a_3,
    test_es4a_1, test_es4a_2, test_es4a_3,
    test_es5a_1, test_es5a_2, test_es5a_3,
    test_es100a_1, test_es100a_2, test_es100a_3,
    test_es101a_1, test_es101a_2, test_es101a_3,
    test_es200_1, test_es200_2, test_es200_3, 
]

if __name__ == '__main__':
    # runtests(tests)
    runtests(tests, logfile='grade.csv')

################################################################################

