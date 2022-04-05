# Trabajo Practico Nro 2: Métodos de búsqueda

## Breve introducción ##

## Dependencias 

* Python **>= 3.9 (Importante!)**
* PIP

## Instalación
Una vez que se tenga Python (>=3.9) y PIP instalado, pueden ejecutar el siguiente comando en la carpeta `./TP1` para instalar las dependencias

```shell
pip install -r requirements.txt
```

## Cómo Correr
Utilizando python se debera ejecutar el main.py.
```bash
python3 main.py
```

## Archivo de Configuración:
### Configuraciones Basicas
Para definir las configuraciones basicas deberan agregar los siguientes parámetros:

**Nota: Borrar los comentarios (//), ya que no son parte de json.**

**Nota: (opción_a | opción_b | opción_c) representa un parámetro que puede tomar únicamente esas opciones**
```json5
"selection": ("0" | "1" | "2" | "3" | "4" | "5"),  // ["Elite", "Truncate", "Roulette Wheel", "Rank", "Tournament", "Boltzmann"]
"crossbreed": ("0" | "1" | "2"), // ["Simple", "Multiple", "Uniform"]
"size": "50",               //  Cantidad de individuos por poblacion
"generations": "500",       //  Cantidad de generaciones
"mutation_bound": "1",      //  Cambio en cada mutación
"mutation_rate": "0.1",     //  Probabilidad de mutación
"t0": "1",                  //  Temperatura Inicial para Boltzmann
"tc": "1",                  //  Factor de cambio de Boltzmann
"k": "10"                   //  Constante de Boltzmann

```