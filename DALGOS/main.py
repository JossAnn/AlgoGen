#Aquí se ejecutará el flujo principal del algoritmo genético.
import json
from params import ventanaParametral
from initpopu import initPopu
from pairs import pairing
from evaluation import evaluateFitness
from cruza import crossOver
from mutation import  mutations
from podar import poda
from render import activate

def main():
    ventanaParametral()
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    generationNumber = params["generationNumber"]
    
    population = initPopu()
    
    evaluateFitness(population)
    """
    i=1
    while i <= generationNumber:
        
        population = mutations(crossOver(pairing(population)))
        print(len(population))
        evaluateFitness(population)
        population = poda(population)
        i += 1
    """
    activate()



if __name__ == "__main__":
    main()
    
