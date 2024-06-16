import json
from params import ventanaParametral
from initpopu import initPopu
from pairs import pairing
from evaluation import evaluateFitness
from cruza import crossOver
from mutation import  mutations
from podar import poda
from render import activate
from tqdm import tqdm

def main():
    ventanaParametral()
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    generationNumber = params["generationNumber"]
    
    population = initPopu()
    
    evaluateFitness(population)#Esta es la evaluacion para la poblacion inicial por eso sale una mas
    
    i=1
    with tqdm(total=generationNumber, desc="Progreso de generaciones") as pbar:
        while i <= generationNumber:
            
            population = mutations(crossOver(pairing(population)))#emparejamiento, cruza y mutacion
            evaluateFitness(population)#evaluacion comun pero de "cursedPopulation"
            population = poda(population)
            pbar.update(1)
            i += 1
    
    print("\n\nGENERANDO  VIDEO")
    activate()



if __name__ == "__main__":
    main()
    
