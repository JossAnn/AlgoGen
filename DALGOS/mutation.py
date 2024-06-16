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
    indi = params["mutationIndiProba"]  #probabilidad que tiene cada individuo de mutar
    gen = params["mutationGenProba"]  #probabilidad de mutar que tiene cada gen del individuo que se decidio que si mutara

    noPts = int(((valueB - valueA) / deltaX) + 1)
    bitsNum = math.ceil(math.log2(noPts))

    cursedPopulation = []

    # micro evaluacion
    for individual in newPopulation:
        index, binIndex, x, fx = individual

        # el individuo es mutable
        if random.randint(0,100) < indi:
            # Convertir cadena de bits en lista pa que mute
            bitsList = list(binIndex)
            
            # Evaluar cada bit/gen para saber si es mutable
            for i in range(bitsNum):
                if random.randint(0, 100) < gen:
                    # Negar el valor del bit (si es 1 pasa a 0 y viceversa)
                    bitsList[i] = '0' if bitsList[i] == '1' else '1'#"asigna 0 si el bit dela posision i es igual a 1, si no, asigna 1"

            # Cadena de bits mutada
            mutBinIndex = ''.join(bitsList)

            # Rellenar los nuevos individuos con la cadena mutada
            mutatedIndex = int(mutBinIndex, 2)
            xS = valueA + mutatedIndex * deltaX
            fxS = xS * math.cos(xS)

            # Añadir el nuevo individuo mutado a la población
            newIndie = [mutatedIndex, mutBinIndex, xS, fxS] #reconstruccion
            cursedPopulation.append(newIndie)
        else:
            #el individuo original si no ha mutado
            cursedPopulation.append(individual)
    
    # Eliminar individuos duplicados (una funcion que limita mucho la evaluacion)
    #cursedPopulation = [list(t) for t in {tuple(ind) for ind in cursedPopulation}]
    #evaluateFitness(cursedPopulation)
    #print(len(cursedPopulation))#Para observar si el algoritmo comienza tirarle al 0 (referencia de pairing en pair y en reverse de la poda en podar)
    
    return cursedPopulation
