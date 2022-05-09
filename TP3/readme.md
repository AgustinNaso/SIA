# TP3: Perceptron simple y multicapa
## Introduccion
En este proyecto se implementa el perceptron simple, 
tanto como una red multicapa completa. Se facilitan funciones de activacion escalon, lineal y no lineales.


## Instalacion y ejecucion

Para el desarrollo del programa se utilizo la version 3.7 de Python

Las dependencias de los ejecutables se encuentran en el archivo requirements.txt para instalarlos, ejecutar

```shell
pip install -r requirements.txt
```
*Puede que en versiones de python3 sea necesario usar pip3*

Una vez instaladas las dependencias continuamos a ejecutar los ejercicios.

## Ejercicio 1

El archivo de configuración se encuentra bajo el nombre ex1_config.json
sus parametros:

```json
{
  "problem": "xor",
  "learning_rate": 0.01,
  "iterations": 1000
}
```
La variable problem puede variar entre "and" y "xor".<br>
Luego se ejecuta el archivo ex1.py

```shell
python3 ex1.py
```

## Ejercicio 2

El archivo de configuración se encuentra bajo el nombre ex2_config.json
sus parametros:

```json
{
  "perceptron": "linear",
  "learning_rate": 0.01,
  "epochs": 10,
  "test_set_start": 10,
  "test_set_end": 30
}
```
La variable perceptron puede variar entre "linear" y "non linear".<br>
Luego se ejecuta el archivo ex2.py.
```shell
python3 ex2.py
```

## Ejercicio 3

El archivo de configuracion que permite cambiar que inciso se 
resuelve se encuentra bajo el nombre ex3_config.json. <br>
Su configuración:
```json
{
  "exercise": 2,
  "config_file": ["ex3config/ex3_1_config.json", "ex3config/ex3_2_config.json", "ex3config/ex3_3_config.json"]
}
```
donde exercise toma los valores 0, 1 y 2 para resolver los ejercicios 1 2 y 3 respectivamente.

Luego se ejecuta el archivo ex3_runner.py

```shell
python3 ex3_runner.py
```

### Configuracion de incisos

HiddenLayers es un array indicando en cada valor la 
cantidad de neuronas en cada hidden, el hidden layer esta 
representado por cada indice respectivamente.<br>
Adaptive eta y momentum toman valores de 0 y 1 indicando si estos estan activos o no.<br>
Los valores del adaptive eta estan representados por adaptive_k, adaptive_inc y adaptive_dec.<br>
Batch_size: toma valores enteros mayores a 0, si su valor es 1 entonces el perceptron 
funciona como un perceptron incremental.


#### Inciso 1
El archivo de configuración se encuentra bajo el nombre ex3config/ex3_1_config.json
sus parametros:

```json
{
    "learning_rate": 0.1,
    "epochs": 100,
    "hiddenLayers": [4],
    "batch_size": 1,
    "momentum": 0,
    "adaptive_eta": 0,
    "adaptive_k": 2,
    "adaptive_inc": 0.5,
    "adaptive_dec": 0.01
}
```

#### Inciso 2
El archivo de configuración se encuentra bajo el nombre ex3config/ex3_2_config.json
sus parametros:

```json
{
    "learning_rate": 0.1,
    "epochs": 100,
    "hiddenLayers": [9, 6],
    "batch_size": 1,
    "momentum": 0,
    "adaptive_eta": 0,
    "adaptive_k": 2,
    "adaptive_inc": 0.5,
    "adaptive_dec": 0.01
}
```

#### Inciso 3
El archivo de configuración se encuentra bajo el nombre ex3config/ex3_3_config.json
sus parametros:

```json
{
    "learning_rate": 0.01,
    "epochs": 1000,
    "hiddenLayers": [10, 10],
    "batch_size": 1,
    "momentum": 0,
    "adaptive_eta": 0,
    "adaptive_k": 2,
    "adaptive_inc": 0.5,
    "adaptive_dec": 0.01
}
```
