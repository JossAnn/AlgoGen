#Genera la poblacion inicial en base a la variablo de poblacion inicial y luego se manda a evaluar los datos
import math
import random
import subprocess
import json
from evaluation import evaluateFitness

# Jalar JSON de params.py (por que son variables que se usan en todo el codigo y era facil leer el json)
result = subprocess.run(["python", "params.py"], capture_output=True, text=True)
jsonParams = result.stdout.strip()
params = json.loads(jsonParams)

valueA = params["valueA"]
valueB = params["valueB"]
deltaX = params["deltaX"]
initialPopu = params["initialPopu"]

# Funcion para completar los datos del individuo "individuo = [1, '001', 3.0, -2.9699774898013365]"
def initPopu():
    noPts = int(((valueB - valueA) / deltaX) + 1)
    nExpo = math.ceil(math.log2(noPts))
    
    indexS = [random.randint(0, noPts-2) for _ in range(initialPopu)]
    
    binIndexS = [format(index, f'0{nExpo}b') for index in indexS]
    
    xS = [valueA + index * deltaX for index in indexS]
    
    fxS = [x * math.cos(x) for x in xS]
    
    individuos = [[index, binIndex, x, fx] for index, binIndex, x, fx in zip(indexS, binIndexS, xS, fxS)]
    
    return individuos

#population = initPopu()
#evaluateFitness(population)
evaluateFitness(initPopu())