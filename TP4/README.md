# Trabajo Practico Nro 4: Métodos de Aprendizaje No Supervisados

## Instalación y ejecución

El programa se desarrollo con python 3.10.

## Ejercicio 1

###Kohonen

Ejecutar el archivo main.py dentro de la carpeta kohonen.

```shell
python3 main.py
```

###Oja

Ejecutar el archivo oja.py dentro de la carpeta TP4.

```shell
python3 oja.py
```

## Ejercicio 2

El archivo de configuración se encuentra bajo el nombre config.json dentro de la carpeta hopfield.
Sus parametros:

```json
{
  "letters": ["H", "L", "I", "X"],
  "letter_to_modify": "X",
  "probability": 0.2,
  "iterations": 100,
  "conserve_pattern": "False"
}
```
- La variable letters toma un arreglo de letras que pueden estar en mayúscula y/o minúscula.
- La variable letter_to_modify toma la letra que se quiere alterar.
- La variable probability toma la probabilidad de ruido.
- La variable iterations toma la cantidad de iteraciones a correr.
- La variable conserve_pattern toma 'True' o 'False'.<br>
Luego se ejecuta el archivo main.py dentro de la carpeta hopfield.

```shell
python3 main.py
```
