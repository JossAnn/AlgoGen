import random

def pairing(population):
    pairedPopulation = []
    
    numParejas = int(len(population) * 0.2)#Es el porcentaje entre 0 y 1 con el que se decide si un individuo se empareja con otro
    #Tiene que ser igual o mayor a 0.17 o la formacion de parejas tiende a 0
    #0.14 minimo pero no concluyente. (Se puede seguir bajando pero para la salida valida deben ser menos generaciones)
    
    # Seleccionar aleatoriamente el 0.17(porcentaje de arriba) de la población para formar parejas
    pairedIndies = random.sample(population, numParejas * 2)  # Se multiplican pa dar tamaño
    # Formar parejas con los individuos seleccionados
    for i in range(0, len(pairedIndies)-1, 2):
        pairedPopulation.append([pairedIndies[i], pairedIndies[i + 1]])
        #al principio llegan aleatorios pero despues de la primer poda llegan ordenados entonces los mas altos son los primeros que pasan a emparejarse
    return pairedPopulation
