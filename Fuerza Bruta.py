from math import inf
from random import randint

#ALGUNOS PROBLEMAS DE EJEMPLO
#El inf nos sirve para indicar soluciones infactibles
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




def calcular_distancia(ruta: list, problema: dict): 
    distancia = 0
    nodo_actual = ruta[0]   #Nodo actual es el primero
    for i in range(len(ruta)-1):
        #print(i+1)
        #Calcula la distancia entre nodos 
        distancia += problema[nodo_actual][ruta[i+1]]
        nodo_actual = ruta[i+1]
        #Retorna la distancia entre nodos
    return distancia

#La funcion recibe un diccionario y una lista de la ruta, y devuelve una lista
def probar_caminos(problema: dict, disp: list, ruta = [])->list:
    
    Si la lista esta vacia devuelve ruta vacia
    if len(disp) == 0: 
        ruta.append(ruta[0])
        return ruta
        
    #Por cada elemento en la lista agrega un nodo a la lista de las rutas
    mejor_ruta = []
    menor_distancia = inf
    for nodo in disp: 
        ruta.append(nodo)
        print(ruta)
        temp_d = disp.copy()
        temp_d.remove(nodo)
        
        #La funcion se hace redundante y manda a esta misma funcion el diccionario junto con la ruta actual
        r = probar_caminos(problema, temp_d, ruta.copy())
        
        #Calcula la distancia de la ruta actual enviando el diccionario
        distancia = calcular_distancia(r, problema)
        if distancia <= menor_distancia: 
            mejor_ruta = r.copy()
            menor_distancia = distancia
            #En caso de ser la menor distancia guarda esa ruta a menos que haya una mejor
        ruta.pop()
        #Devuelve la mejor ruta
    return mejor_ruta


if __name__ == "__main__": 
    from time import time
    print("Fuerza bruta")
    #Asignamos el problema a solucionar
    p = problema_1
    
    #Covertirmos el diccionario en lista
    disponibles = [key for key in p]
    
    #Arrancamos el contador de solucion
    inicio = time()
    
    #Mandamos el diccionario y la lista a la función proba caminos
    ruta = probar_caminos(p, disponibles)
    
    
    print("Tiempo de ejecución: "+str(time()-inicio))
    print("Mejor ruta: "+str(ruta))
    print("Distancia: "+str(calcular_distancia(ruta, p)))