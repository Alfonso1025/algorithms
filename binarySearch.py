                                                                                                                                """ Binary search """

""" 
En una lista (arreglo), los elementos deben encontrarse ordenados de forma ascendente o descendente

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

Despues de cubrir los test cases mas importantes, expresa una solucion al problema no en codigo sino en ingles o español.
En este caso se podria usar la Lineal Search(fuerza bruta). Es decir, buscar carta por carta, una por una, en el arreglo hasta 
encontrar la que tenga el query. Esto se podria expresar
en codigo de la siguiente manera:
1 iterar sobre el arrglo
2 revisar si elemento con index[i] es igual al 
query.
3. De ser asi retornar el elemento
4. De lo contrario incrementar position +1 y repetir
paso 2

query=x
for element in cards
    if(element==query)
        return element

La busqueda lineal no es la forma mas optima de resolver
el problema

            Algorithms Complexity  
En este caso en una baraja de N cartas, se tendria
que voltear una N cantidad de cartas para encontrar
el query. Lo cual no es muy eficiente.

Complexity:
    Medida de la cantidad de tiempo y/o espacio req-
    erido por un algoritmo para procesar un input
    Siempre se busca el peor escenario es decir en el
    ejemplo anterior, cuanto tiempo tomaria encontrar
    la carta con el query si el query se encuentra en la
    ultima carta.

    cN= constant time
    c'= space complexity

    Big O Notation
        la complejidad de un algoritmo se reprenta con la
        big o notation. 
        ej. si la complejidad del algoritmo fuera:
        cN^3+dN^2+eN+f, en bigOnotation se expresaria
        O(N^3) 
        por tanto la complejidad en tiempo de la busqueda lineal
        es O(N) y en espacio es O(1)

Binary Search
   Retomando el ejemplo, se empieza escogiendo una carta de en medio. Recordar 
   las cartas estan ordenadas de mayor a menor ene ste caso. Al escoger una carta
   intermedia por ejmplo si sale 9 y buscamos la carta con el 7, podemos des
   cartar todas las cartas que esten adelante del nueve y enfocarnos solo en las
   que esten despues del nueve ya que 7 es menor que nueve. 
   El proceso se repite una vez mas se toma la carta de en medio y se compara.
   Hata dar con la ultima carta qque debe tener el query. Recuerda que siempre se 
   considera el peor caso.


"""
cards=[23,22,21,19,11,7,4,3,2,1]
def locate_card(cards, query):
    low=0 #primera posicion del arreglo
    hight=len(cards)-1 #ultima posicion del arreglo
    while low <=hight:
        mid=(low+hight)//2
        mid_number=cards[mid]

        print("low is:", low, ",hight:", hight, ",mid:", mid, "mid_number:", mid_number)

        if mid_number==query:
            return mid
        elif mid_number < query:
            hight=mid-1
        elif mid_number > query:
            low=mid+1
    return -1
locate_card(cards,7)

"""
The above algorithm fails in the following situation:
cards=[8,8,6,6,6,6,6,5,3,2,2,2,0,0,0], query=6
lo=0, hi=14, mid=7, mid_number=6
In this case, mid_number equals the query so our algorithm will return
index 7 as result; however, there is a 6 in the index 2. According to our
rules, the function should return the first ocrrance of the query within the list
We need add a new  check in our algorithm that evaluates if the mid_number is
the first or only ocurrance of the query
In this case, we will use a helper function
"""

def test_location(cards, query, mid):
    mid_number=cards[mid]
    print("mid is: ", mid, "mid_number is ", mid_number)
    if mid_number==query:
        #if the index before mid es 0 or bigger than 0
        # and the value in that index equals query
        if mid-1 >=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_cards_2(cards, query):
    lo, hi=0, len(cards)-1

    while lo <= hi:
        print("lo: ",lo,"hi:",hi)
        mid=(lo+hi)//2
        result= test_location(cards, query, mid)

        if result=='found':
            return mid
        elif result=='left':
             hi = mid-1
        elif result=='right':
             lo= mid+1
    return -1
    
    """
    Ahora contemos la cantidad de iteraciones que lleva
    a cabo este algoritmo para conocer su eficiencia

    initial lenght: N
    Iteration 1: N/2
    Iteration 2: N/4 o N/2^2
    iteration 3: N/8 o N/2^3
    Asi que hay un patron

    Iteration k: N/2^K
    En este punto la longitud de la lista es de uno
    N/2^K=1
    Despejando N
    N=2^k

    En terminos del logaritmo:
    K= log N
    
    """
