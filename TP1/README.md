# Trabajo Practico Nro 1: Métodos de búsqueda

## Breve introducción ##

En este trabajo se investigaron diferentes técnicas de búsqueda (informadas y no informadas)
para encontrar una solución al juego de 8 number puzzle y se compararon los diferentes resultados
para determinar si había un método optimo.
Para los métodos de búsqueda no informados se utilizaron 3 algoritmos:
* BFS
* DFS
* IDDFS

Para los métodos de búsqueda informados se utilizaron también 3 algoritmos:
* LOCAL SEARCH
* GLOBAL SEARCH
* A STAR

Para estos últimos 3 algoritmos se desarrollaron 3 heurísticas,
dos admisibles y una no admisible.




## Instalación y ejecución

El programa se desarrollo con python 3.10  
Para instalar las dependencias para poder ejecutar el programa correr
```shell
\TP1> pip install requirements.txt
```

Logrado esto, para correr la interfaz grafica del programa, ejecutar 

```shell
\TP1> python game.py 
```
En caso de que se quiera correr el test generador de gráficos para comparar los algoritmos, ejecutar
```shell
\TP1> python matplot.py 
```
## Información adicional
Para configurar que algoritmo y/o heurística se corre, se logra directamente 
utilizando los dropdowns que se disponen en la interfaz.
Además hay 3 botones, uno para resolver el juego (se convierte en un botón de pausa al iniciar la solución), uno para generar
un tablero aleatorio y uno para devolver el tablero a la posición antes de 
resolverlo (en caso de que se quiera partir de un mismo tablero para comparar 
algoritmos).  
Por ultimo, se dispone un archivo de configuración *settings.json* para elegir la
profundidad máxima inicial del algoritmo IDDFS, el atributo informed para elegir 
si se grafican los algoritmos informados o no informados en el test de matplot y
show_steps permite habilitar la impresión de un loggeo de la solución


![interfaz grafica](https://github.com/AgustinNaso/SIA/blob/main/TP1/GUI.png?raw=true)



```json
{
  "max_depth": "10",
  "matplot": {
    "informed": false
  },
  "show_steps": true
}
```
