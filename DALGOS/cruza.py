import json

def crossOver(population):
    # Lee los parámetros del archivo JSON
    jsonParamsPath = "jsons\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    initialPopu = params["initialPopu"]
    maxiPopu = params["maxiPopu"]
    mutationIndiProba = params["mutationIndiProba"]
    mutationGenProba = params["mutationGenProba"]
    generationNumber = params["generationNumber"]
    
    
    #print(params)
    #print(population)

    return