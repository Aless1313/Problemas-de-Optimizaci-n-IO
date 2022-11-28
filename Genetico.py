from math import inf
from random import randint

#ALGUNOS PROBLEMAS DE EJEMPLO

problema_1 = {
    0: {0: 0, 1: 10, 2: 15, 3: 20},
    1: {0: 5, 1: 0, 2: 9, 3: 10},
    2: {0: 6, 1: 13, 2: 0, 3: 12},
    3: {0: 8, 1: 8, 2: 9, 3: 0}
}

problema_2 = {
    0: {0: 0, 1: 12, 2: 10, 3: 19, 4: 8}, 
    1: {0: 12, 1: 0, 2: 3, 3: 7, 4: 6},
    2: {0: 10, 1: 3, 2: 0, 3: 2, 4: 20},
    3: {0: 19, 1: 7, 2: 2, 3: 0, 4: 4}, 
    4: {0: 8, 1: 6, 2: 20, 3: 4, 4: 0}
}

problema_3 = {
    0: {0: 0, 1: 12, 2: 10, 3: inf, 4: inf, 5: inf, 6: 12}, 
    1: {0: 12, 1: 0, 2: 8, 3: 12, 4: inf, 5: inf, 6: inf}, 
    2: {0: 10, 1: 8, 2: 0, 3: 11, 4: 3, 5: inf, 6: 9}, 
    3: {0: inf, 1: 12, 2: 11, 3: 0, 4: 11, 5: 10, 6: inf},
    4: {0: inf, 1: inf, 2: 3, 3: 11, 4: 0, 5: 6, 6: 7}, 
    5: {0: inf, 1: inf, 2: inf, 3: 10, 4: 6, 5: 0, 6: 9}, 
    6: {0: 12, 1: inf, 2: 9, 3: inf, 4: 7, 5: 9, 6: 0}, 
}

problema_4 = {
    0: {0: 0, 1: 13, 2: 25, 3: 15, 4: 21, 5: 9, 6: 19, 7: 18, 8: 8, 9: 15}, 
    1: {0: 13, 1: 0, 2: 26, 3: 21, 4: 29, 5: 21, 6: 31, 7: 23, 8: 16, 9: 10}, 
    2: {0: 25, 1: 26, 2: 0, 3: 11, 4: 18, 5: 23, 6: 28, 7: 44, 8: 34, 9: 35}, 
    3: {0: 15, 1: 21, 2: 11, 3: 0, 4: 10, 5: 13, 6: 19, 7: 34, 8: 24, 9: 29}, 
    4: {0: 21, 1: 29, 2: 18, 3: 10, 4: 0, 5: 12, 6: 11, 7: 37, 8: 27, 9: 36}, 
    5: {0: 9, 1: 21, 2: 23, 3: 13, 4: 12, 5: 0, 6: 10, 7: 25, 8: 14, 9: 25}, 
    6: {0: 19, 1: 31, 2: 28, 3: 19, 4: 11, 5: 10, 6: 0, 7: 32, 8: 23, 9: 35}, 
    7: {0: 18, 1: 23, 2: 44, 3: 34, 4: 37, 5: 25, 6: 32, 7: 0, 8: 10, 9: 16}, 
    8: {0: 8, 1: 16, 2: 34, 3: 24, 4: 27, 5: 14, 6: 23, 7: 10, 8: 0, 9: 14},
    9: {0: 15, 1: 10, 2: 35, 3: 29, 4: 36, 5: 25, 6: 35, 7: 16, 8: 14, 9: 0}, 
}

#EJEMPLOS PARA CLASE

ejemplo_placa = {
    "A": {"A": 0, "B": 80, "C": 55, "D": inf, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": 50}, 
    "B": {"A": 80, "B": 0, "C": 60, "D": 80, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "C": {"A": 55, "B": 60, "C": 0, "D": 55, "E": inf, "F": inf, "G": inf, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "D": {"A": inf, "B": 80, "C": 55, "D": 0, "E": 25, "F": 20, "G": 35, "H": inf, "I": inf, "J": inf, "K": inf, "L": 50}, 
    "E": {"A": inf, "B": inf, "C": inf, "D": 25, "E": 0, "F": 20, "G": 20, "H": inf, "I": inf, "J": inf, "K": 20, "L": 35}, 
    "F": {"A": inf, "B": inf, "C": inf, "D": 20, "E": 20, "F": 0, "G": 20, "H": inf, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "G": {"A": inf, "B": inf, "C": inf, "D": 35, "E": 20, "F": 20, "G": 0, "H": 20, "I": inf, "J": inf, "K": inf, "L": inf}, 
    "H": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": 20, "H": 0, "I": 10, "J": 15, "K": inf, "L": inf}, 
    "I": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": inf, "H": 10, "I": 0, "J": 10, "K": inf, "L": inf}, 
    "J": {"A": inf, "B": inf, "C": inf, "D": inf, "E": inf, "F": inf, "G": inf, "H": 15, "I": 10, "J": 0, "K": 10, "L": 30}, 
    "K": {"A": inf, "B": inf, "C": inf, "D": inf, "E": 20, "F": inf, "G": inf, "H": inf, "I": inf, "J": 10, "K": 0, "L": 25}, 
    "L": {"A": 50, "B": inf, "C": inf, "D": 50, "E": 35, "F": inf, "G": inf, "H": inf, "I": inf, "J": 30, "K": 25, "L": 0}
}


#FUNCION PARA EVALUAR UN RUTA EN PARTICULAR

def calcular_distancia(ruta: list, problema: dict): 
    if len(ruta) == 0: 
        return inf
    distancia = 0
    nodo_actual = ruta[0]
    for i in range(len(ruta)-1):
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
    return distancia


#ALGORITMO GENÉTICO

#Recibe como parametro el dicctionario
def generar_solucion(p: dict): 
    #Convierte a lista el diccionario
    disp = [key for key in p]
    ruta = []
    #Por cada elmento de diccionario
    for i in range(len(p)): 
        #Añade un elemento más elemento aleatorio
        ruta.append(disp.pop(randint(0, len(disp)-1)))
        #Añade a la ruta el primer elemento
    ruta.append(ruta[0])
    return ruta

def seleccion(pob: list, problema: dict, n_muestra = 2):
    solucion = ""
    dist = inf
    #iteramos entre el numeor de muestras
    for i in range(n_muestra): 
        #obtenemos un elemento aleatorio del diccionario
        m = pob[randint(0, len(problema)-1)]
        #comprobamos la distancia entre este elemento y el diccionario
        if calcular_distancia(m, problema) <= dist: 
            #buscamos la solucion con mejor distancia
            dist = calcular_distancia(m, problema)
            solucion = m  
            #Retonamos la solucion (padres)
    return solucion

#como parametro la lista y el diccionario
def correccion(sol: list, problema: dict):
    #obtenemos los elemenos faltantes 
    faltan = [key for key in problema]
    sobran = []
    sol.pop()
    
    for s in sol: 
        if s in faltan: 
            #removemos los faltantes
            faltan.remove(s)
        elif s not in faltan and s not in sobran:
            #añadimos los sobrantes
            sobran.append(s)
        #mientras los sobrantes sena mayor a 0
    while len(sobran) > 0: 
        #obtenemos elementos aleatorios
        s = randint(0, len(sobran)-1)
        f = randint(0, len(faltan)-1)
        
        n = sol.index(sobran[s])
        #ontenemos una nueva solucion apartir de estos elementos
        nueva_sol = [sol[i] for i in range(n)]
        nueva_sol.append(faltan[f])
        #iteramos entre los eementos de la solucion
        for i in range(n+1, len(sol)): 
            nueva_sol.append(sol[i])
            #añadimos los elemetos sobrantes y faltantes acorde al numero aleatorio obtenido
        sobran.pop(s)
        faltan.pop(f)
        sol = nueva_sol
        #retornamo la solucion
    return sol

#Para obtener los cruces tomando como parametros la lista y el diccionario y otorando una probabilidad
def cruce(p: list, m: list, problema: dict, probabilidad = 90): 
    #Si el numero aleatorio es menor que la pobabilidad
    if randint(1, 100) <= probabilidad: 
        #tomamos dos pivotes obtenidos del diccionario
        pivot_1 = len(problema)//3
        pivot_2 = len(problema)*2//3

        h1 = list()
        h2 = list()
        
        #iteramos entre el pivote 1
        for i in range(pivot_1): 
            #añadimos a la lista estos elementos de la iteracion
            h1.append(p[i])
            h2.append(m[i])
        #repetimos con el picote 1 y 2
        for i in range(pivot_1, pivot_2): 
            h1.append(m[i])
            h2.append(p[i])
        #repetimos con pivote 2 y la lista
        for i in range(pivot_2, len(p)): 
            h1.append(p[i])
            h2.append(p[i])
        
        #obtenemos las correcioines de la lista
        h1 = correccion(h1, problema)
        h2 = correccion(h2, problema)
        h1.append(h1[0])
        h2.append(h2[0])
        return h1, h2
    return p, m

#obenemos como parametro la solucion obtenida en el cruce, el diccionario y la pobabilidad
def mutacion(solucion: str, problema: dict, probabilidad = 5): 
    #obtenemos pivotes aleatorios
    if randint(1, 100) <= probabilidad: 
        pivote_1 = randint(0, len(problema)-1)
        pivote_2 = pivote_1
        #si ambos pivotes os iguales
        while pivote_2 == pivote_1: 
            #cambiamos un pivote
            pivote_2 = randint(0, len(problema)-1)
            #si el pivote 2 es menor que el 1
        if pivote_2 < pivote_1: 
            #intercambiamos
            temp = pivote_1
            pivote_1 = pivote_2
            pivote_2 = temp
            #genermaos una solucion temporal obtneida del pivote 1
        temp = solucion[pivote_1]
        #obtemos solucion le pivote 2
        solucion[pivote_1] = solucion[pivote_2]
        #le agregamos la solucion temporal a la solucion del pivote 2
        solucion[pivote_2] = temp
        solucion[len(solucion)-1] = solucion[0]
        #retornamos esta solucion
    return solucion

def algoritmo_genetico(problema: dict, n_gen: int, n_pob: int, explicito = False): 
    #Genera la poblacion a traves del diccionario y el numero de poblacion asignado
    poblacion = [generar_solucion(problema) for i in range(n_pob)]
    
    #Si el resultado es  explicito lo muestra directamente
    if explicito: 
        print("Población Inicial\tDistancia")
        for individuo in poblacion: 
            print("\t"+str(individuo)+"\t\t"+str(calcular_distancia(individuo, problema)))
    mejor_solucion = ""
    mejor_valor = inf
    
    #iteramos el numero de generaciones
    for g in range(n_gen): 
        if explicito:
            print("-"*10)
            print("Generación "+str(g+1))
            #En caso de no se explicito buscmaos alos padres
        mejor_solucion_local = ""
        mejor_valor_local = inf
        #Mandamos a llamar a la funcion para buscar padres mandando como parmetro el dicionario y la poblacion y iteramos el numero de poblacion
        padres = [seleccion(poblacion, problema) for i in range(n_pob)]
        hijos = list()
        #Iteramos entre numero de poblacions tomando los padres
        for i in range(0, n_pob, 2): 
            padre, madre = padres[i], padres[i+1]
            #Iteramos entre el numero de cruces obtenido de los padres y el diccionario
            for h in cruce(padre, madre, problema): 
                #obtebemos la mutacion obtenida del cruce
                h = mutacion(h, problema)
                #añadimos los hijos
                hijos.append(h)
                #calclamos la distancia en la solucion obtenida en la mutacion
                d = calcular_distancia(h, problema)
                #print('\t' + h + '\t\t' + str(d))
                #asignamos la mejor solucion local de las iteraciones
                if d <= mejor_valor_local: 
                    mejor_valor_local = d
                    mejor_solucion_local = h
        #igualamos la poblacion a los hijos
        poblacion = hijos
        #si es explicito calculamos directamente las soluciones
        if explicito: 
            print("Mejor solución\tDistancia")
            print(str(mejor_solucion_local)+"\t"+str(mejor_valor_local))
        if mejor_valor_local <= mejor_valor: 
            mejor_solucion = mejor_solucion_local
            mejor_valor = mejor_valor_local
        print("\nGeneración #" + str(g+1))
        print("Solución: "+str(mejor_solucion_local))
        print("Valor: "+str(mejor_valor_local))
    return mejor_solucion

if __name__=="__main__": 
    from time import time
    p = problema_1

   
    
    print("-"*5)
    print("Alforitmo genetico: ")
    t = time()
    ruta = algoritmo_genetico(p, 5, 100)
    print("\nTiempo de ejecución: "+str(time()-t))
    print("Solución: "+str(ruta))
    print("Valor: "+str(calcular_distancia(ruta, p)))