# Trabajo Practico Nro 1: Metodos de busqueda

## Breve introduccion ##
En este trabajo se investigaron diferentes tecnicas de busqueda (informadas y no informadas)
para encontrar una solucion al juego de 8 number puzzle y se compararon los diferentes resultados
para determinar si habia un metodo optimo.
Para los metodos de busqueda no informados se utilizaron 3 algoritmos:
* BFS
* DFS
* IDDFS

Para los metodos de busqueda informados se utilizaron tambien 3 algoritmos:
* LOCAL SEARCH
* GLOBAL SEARCH
* A STAR

Para estos ultimos 3 algoritmos se desarrollaron 3 heuristicas,
dos admisibles y una no admisible.



## Instalacion y ejecucion

El programa se desarrollo con python 3.10
Para instalar las dependencias para poder ejecutar el programa correr
```shell
pip install requirements.txt
```
en la carpeta del correspondiente programa. 

Logrado esto, para correr la interfaz grafica del programa, ejecutar 

```shell
\TP1> python game.py 
```

## Informacion adicional
Para configurar que algoritmo y/o heuristica se corre, se logra directamente 
utilizando los dropdowns que se disponen en la interfaz.
Ademas hay 3 botones, uno para resolver el juego, uno para generar
un tablero aleatorio y uno para devolver el tablero a la posicion antes de 
resolverlo (en caso de que se quiera partir de un mismo tablero para comparar 
algoritmos).
Por ultimo, se dispone un archivo de configuracion *settings.json* para elegir la
profundidad maxima inicial del algoritmo IDDFS

![interfaz grafica](/GUI.png)



```json
{
  "max_depth": "10000"
}
```
