                                                                                                                                """ Binary search """

""" En una lista (arreglo), los elementos deben encontrarse ordenados de forma ascendente o descendente

    En el siguiente problema se tienen una baraja de cartas enumeradas y boca abajo de manera que 
    no puede verse el numero. Se pide que se programe un algoritmo que permita encontrar la carta 
    con el numero 7, con el menor numero de de destape de cartas

Se  pueden escribir test cases antes de empezar a programar
    test={
    input:{
        cards:[22,18,15,7,4,3,2,1],
        query:7
    },
    output:3
}


def locate_card(cards, query):
    pass
locate_card(**test['input']) == test['output']


Deben de considerarse todos los posibles escenraios por ejemplo que la carta con el 7 este en el primer
elemento del arreglo o en el ultimo o bien que no se encuentre en absoluto o qu este repetido

tests= []
tests.append(test)
tests.append(
    {
        'input':{
            cards:[22,18,15,7,4,3,2,1]
            'query':1
             },
        'output':6
    }
)

test.append(
    'inout:{
        cards:[22,18,15,7,4,3,2,1]
        query:22
    },
    'output:1
     }
     )

"""


