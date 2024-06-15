"""import json
import random
import math
    

def mutations(newPopulation):
    #newPopulation Recibe: [[7, '0000111', 27.0, -7.887747835813577], [51, '0110011', 71.0, -21.94061369979102], [14, '0001110', 34.0, -28.851389342676576], ...]
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    indi = params["mutationIndiProba"]#Es la probabilidad que tiene cada individuo del parametro newPopulation de mutar
    gen = params["mutationGenProba"]#Es pa probabilidad de mutar que tiene cada gen del individuo cambiante
    
    ""
    Instrucciones:
    extraer cada inividuo de la newPopulation recibida
    evaluar si el individuo es mutable de acuerdo al valor de indi ( indi = al porcentaje que tiene el individuo de mutar)
    Si el individuo es mutable, extrae la cadena de bits del individuo
    Cada bit o gen del individuo se evalua para saber si es mutable de acuerdo al valor de gen ( gen = al porcentaje que tiene cad bit de mutar)
    Si el bit de la cadena resulta ser mutable se cabia el valor de ese bit ( si era 1 pasa a ser 0 y viceverza, es decir, se niega)
    
    para los individuos cuyos genes han mutado y ahora tienen una nueva cadena de bits:
        Rellenar los nuevos individuos
        indexS = [calcular el binario mutado a entero] 
        binIndexS = [es el binario mutado]
        xS = [valueA + index * deltaX for index in indexS]
        fxS = [x * math.cos(x) for x in xS]
        individuos = [[index, binIndex, x, fx] for index, binIndex, x, fx in zip(indexS, binIndexS, xS, fxS)]
        
    finalmente todos los individuos repetidos deben ser eliminados antes de meterlos al arreglo cursedDepuredPopulation, que es el que se retorna
        
    Nota: en otras partes del codigo, longitud necesaria de la cadena de bits se calcula así (por si te sirve como refetencia)
    noPts = int(((valueB - valueA) / deltaX) + 1)
    bitsNum = math.ceil(math.log2(noPts))    
    ""
    return cursedDepuredPopulation """



import json
import random
import math

def mutations(newPopulation):
    # newPopulation Recibe: [[7, '0000111', 27.0, -7.887747835813577], [51, '0110011', 71.0, -21.94061369979102], [14, '0001110', 34.0, -28.851389342676576], ...]
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    indi = params["mutationIndiProba"]  # Probabilidad que tiene cada individuo de mutar
    gen = params["mutationGenProba"]  # Probabilidad de mutar que tiene cada gen del individuo que se decidió que si mutará

    # Calcular la longitud necesaria de la cadena de bits
    noPts = int(((valueB - valueA) / deltaX) + 1)
    bitsNum = math.ceil(math.log2(noPts))

    # Para almacenar la población depurada con mutaciones
    cursedPopulation = []

    # Evaluar cada individuo de la nueva población
    for individual in newPopulation:
        index, binIndex, x, fx = individual

        # Evaluar si el individuo es mutable
        if random.randint(0,100) < indi:
            # Convertir la cadena de bits en una lista para facilitar la mutación
            bits = list(binIndex)
            
            # Evaluar cada bit/gen para saber si es mutable
            for i in range(bitsNum):
                if random.randint(0, 100) < gen:
                    # Negar el valor del bit (si es 1 pasa a 0 y viceversa)
                    bits[i] = '0' if bits[i] == '1' else '1'

            # Crear la nueva cadena de bits mutada
            mutated_binIndex = ''.join(bits)

            # Rellenar los nuevos individuos con la cadena mutada
            mutated_index = int(mutated_binIndex, 2)
            xS = valueA + mutated_index * deltaX
            fxS = xS * math.cos(xS)

            # Añadir el nuevo individuo mutado a la población
            new_individual = [mutated_index, mutated_binIndex, xS, fxS]
            cursedPopulation.append(new_individual)
        else:
            # Añadir el individuo original si no ha mutado
            cursedPopulation.append(individual)
    
    # Eliminar individuos duplicados
    #cursedPopulation = [list(t) for t in {tuple(ind) for ind in cursedPopulation}]
    #evaluateFitness(cursedPopulation)
    print(len(cursedPopulation))
    
    return cursedPopulation
