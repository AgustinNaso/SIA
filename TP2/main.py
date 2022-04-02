import json
import numpy as np
from main_algorithm import main_algorithm

with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

selection = int(jsonObject['selection'])
crossbreed = int(jsonObject['crossbreed'])
population_size = int(jsonObject['size'])
generations = int(jsonObject['generations'])
t0 = int(jsonObject['t0'])
tc = int(jsonObject['tc'])
k = int(jsonObject['k'])
stop_criteria = int(jsonObject['stop_criteria'])


def main():
    print(main_algorithm(selection, crossbreed, population_size, generations, t0, tc, k))
    print(np.random.randn(10))
    print("Hello World!")


if __name__ == "__main__":
    main()
