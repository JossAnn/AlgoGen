import json
import random

def poda(cursedPopulation):
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
        maxiPopu = params["maxiPopu"]
    floatSection = maxiPopu / 6
    #ordenar de menor a mayor y eliminar repetidos
    orderedPopulation = sorted(set(map(tuple, cursedPopulation)), key=lambda x: x[-1])
    
    #crear las clases y asignarles partes diferentes de la poblacion ordenada
    third_len = len(orderedPopulation) // 3
    #poorClass = orderedPopulation[:third_len]
    mediClass = orderedPopulation[third_len:2 * third_len]
    richClass = orderedPopulation[2 * third_len:]

    #No todas las clases tienen la misma longitud
    #print(f"Poor class : {len(poorClass)}")
    #print(f"Medi class : {len(mediClass)}")
    #print(f"Rich class : {len(richClass)}")

    section = int(floatSection)
    #se jalan individuos de cada clase a una poblacion selecta
    richSection = section * 3
    selectedPopulation = random.sample(richClass, min(richSection, len(richClass)))
    mediSection = section * 2
    selectedPopulation += random.sample(mediClass, min(mediSection, len(mediClass)))
    #poorSection = section
    #selectedPopulation += random.sample(poorClass, min(poorSection, len(poorClass)))

    #Comparacion delongitud, entre el arreglo selcto y la maxima de individuos permitidos
    if len(selectedPopulation) < maxiPopu:
        #si faltan individuos para alcanzar la maxima, los rellena con los que vienen de la curseada
        diferencia = maxiPopu - len(selectedPopulation) #con regularidad será uno nada mas
        faltan = min(diferencia, len(cursedPopulation))
        indiesFaltantes = random.sample(cursedPopulation, faltan)
        selectedPopulation += indiesFaltantes
    elif len(selectedPopulation) > maxiPopu:
        #Si sobran inividuos (normalmente no va a pasar, pero por si las moscas) los borra para mantener la poblacion segun el numero en maxiPopu
        while len(selectedPopulation) > maxiPopu:
            selectedPopulation.pop(random.randint(0, len(selectedPopulation) - 1))

    #Por cuallquier cosa
    limitedPopulation = selectedPopulation#aqui quiero que la lista se ordene de mayor a meno
    #Se ordena en reversa para que los primeros que lleguen sean los mas altos y asi seran los primeros en formar parejas (les da prioridad de cruce a los mas altos)
    #limitedPopulation = sorted(selectedPopulation, key=lambda x: x[-1], reverse=True)

    return limitedPopulation
