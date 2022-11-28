def ordenar(lista: list): 
    lista_ordenada = [i for i in range(len(lista))]
    for i in range(len(lista)-1): 
        for j in range(len(lista)-1):
            if lista[lista_ordenada[j]] < lista[lista_ordenada[j+1]]:
                temp = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j+1] = temp
    return lista_ordenada

def imprimir_tabla(costos: list, d: list, x: list): 
    for i in range(len(costos)): 
        print("P"+str(i+1) + " " + str(costos[i]) + " " + str(x[i]))
    print("D " + str(d))

def evaluar(x: list, b: list): 
    z = 0
    for i in range(len(x)): 
        z += x[i]*b[i]
    return z

if __name__=="__main__":
    n = int(input("Ingrese la cantidad de productos que se pueden producir: "))
    m = int(input("Ingrese la cantidad de materias primas disponibles: "))
    costos = [[0 for j in range(m)] for i in range(n)]
    beneficios = [0 for i in range(n)]
    disponibilidad = [0 for j in range(m)]
    for i in range(n):
        for j in range(m): 
            costos[i][j] = float(input(f"Costo de m.p. {j+1} para producir el producto {i+1}, c{i+1}{j+1} = "))
        beneficios[i] = float(input("Beneficio b"+str(i+1)+" = "))
    for j in range(m): 
        disponibilidad[j] = int(input("Disponibilidad d"+str(j+1)+" = "))
    

    '''
    n = 2 #Cantidad de productos
    m = 3 #Cantidad de materias primas
    costos = [[0.1, 0.3, 0.2], [0.3, 0.2, 0.2]]
    beneficios = [4, 3]
    disponibilidad = [210, 240, 200]
    '''
    x = [0 for i in range(n)]

    lista = ordenar(beneficios)
    print("L = "+str(lista))
    print("-"*20)
    imprimir_tabla(costos, disponibilidad, x)

    for i in lista: 
        print("-"*20)
        print("Iteración #"+str(i+1))
        #Se elige al primer cociente como valor inicial de la variable menor
        menor = int(disponibilidad[0]/costos[i][0])

        for j in range(len(disponibilidad)): 
            if int(disponibilidad[j]/costos[i][j]) < menor: 
                #Actualizar el valor del menor cociente entero
                menor = int(disponibilidad[j]/costos[i][j])

        print("Menor cociente: "+str(menor))
        #Actualizar el valor de x_i en la solución
        x[i] = menor
        #ACtualizar la disponibilidad de cada materia prima
        for j in range(len(disponibilidad)): 
            disponibilidad[j] -= x[i] * costos[i][j]
            
        imprimir_tabla(costos, disponibilidad, x)
    print("-"*20)
    print("Solución: x = "+str(x))
    print("Valor Z(x) = "+str(evaluar(x, beneficios)))
        
