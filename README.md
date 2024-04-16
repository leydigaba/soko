# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimiento a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

- Documentar el código generado.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. Cada nivel tiene distinto número de cajas y metas.
6. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
mapa = [
            [3,3,3,3,3,3,3],
            [3,4,4,4,4,4,3],
            [3,4,0,4,1,2,3],
            [3,4,4,4,4,4,3],
            [3,3,3,3,3,3,3]
        ]
````

### 3.2 Lista de elementos

Para esta versión del sokoban se utilizarán numeros para representar cada uno de los elementos del juego.

| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Cajas |
| 2 | Metas |
| 3 | Paredes |
| 4 | Piso |
| 5 | Pesonaje_meta |
| 6 | Caja_meta |

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

| Letra | Dirección del movimiento |
| -- | -- |
| a | Izquierda |
| d | Derecha |
| w | Arriba |
| s | Abajo |

## 5. Modo de juego

El juego consiste mostrar el mapa y solicitar al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se presiona enter, se evalua el moviento, si es un movimiento valido se realiza el cambio en el array, es decir se actualiza el mapa, y se repite este proceso forma infinita, hasta que se hayan terminado de acomodar todas las cajas sobre las metas.


## 6. Funciones a implementar

Después de realizar un análisis del juego sokoban se identifican funciones necesarias para completarlo, a continuación se crea una tabla con la lista de estas funciones para tener un mejor control sobre el avance del desarrollo del juego.

Para llevar un mejor control del avance del desarrollo se utiliza la metodología Kanban, indicando en que estatus de desarrollo se encuentra cada función del juego

| Valor | Interpretación |
| -- | -- |
| ToDo | Por hacer |
| Doing | Programando y validando |
| Done | Programada y validada con éxito |

### Ejemplo de seguimiento:

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | ToDo | - |

**Nota:** En este sentido para un mejor control se podrían agregar las columnas asignación (en caso de que sea un trabajo en equipo) y fecha de inicio, para conocer los tiempos que estan llevando realizar cada una de las funciones.


### Ejemplo de Kanban trabajo en equipo

| No. | Función | Asignación | ToDo | Doing | Done | Fecha inicio | Fecha terminación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Salvador | - | - | X | 18/Mar/2024 | 19/Mar/2024 |
| 1. | Repetir el juego hasta terminar el nivel. | Salvador | - |X | - | 19/Mar/2024 | - |

### 6.1 Funciones generales
| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | TERMINADO | 13/04/24 |
| 1. | Repetir el juego hasta terminar el nivel. | TERMINADO |13/04/24  |
| 2. | Imprimir mapa.| TERMINADO | 10/03/24 |
| 3. | Leer el movimiento. | TERMINADO | 10/04/24 |
| 4. | Evaluar el movimiento del usuario. | TERMINADO | 10/0424 |

### 6.2 Derecha


## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Terminado | [0,4] | [4,0] | 16/03/24 |
| 6. | Personaje, meta  | Terminado | [0,2] | [4,5] |16/03/24 |
| 7. | Personaje, caja, pasillo | Terminado | [0,1,4] | [4,0,1] | 16/03/24 |
| 8. | Personaje, caja,  meta | Terminado | [0,1,2] | [4,0,6] | 16/03/24|
| 9. | Personaje, caja_meta, pasillo | Terminado | [0,6,4] | [4,5,1 ] | 16/03/24 |
| 10. |Personaje, caja_meta, meta | Terminado | [0,6,2] | [4,5,6] | 16/03/24 |
| 11. | Personaje_meta, pasillo | Terminado | [5,4] | [2,0] | 16/03/24 |
| 12. | Personaje_meta, meta | Terminado | [5,2] | [2,5] | 16/03/24 |
| 13. | Personaje_meta, caja, pasillo |Terminado | [5,1,4] | [2,0,1] | 16/03/24|
| 14. | Personaje_meta, caja, meta |Terminado | [5,1,2] | [2,0,6] | 16/03/24 |
| 15. | Personaje_meta, caja_meta, pasillo |Terminado | [5,6,4] | [2,5,1] | 16/03/24 |
| 16. | Personaje_meta, caja_meta, meta | Terminado | [5,6,2] | [2,5,6] | 16/03/24 |

### 6.3 Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Terminado | [0,4] | [4,0] | 16/03/24 |
| 6. | Personaje, meta  | Terminado | [0,2] | [4,5] |16/03/24 |
| 7. | Personaje, caja, pasillo | Terminado | [0,1,4] | [4,0,1] | 16/03/24 |
| 8. | Personaje, caja,  meta | Terminado | [0,1,2] | [4,0,6] | 16/03/24|
| 9. | Personaje, caja_meta, pasillo | Terminado | [0,6,4] | [4,5,1 ] | 16/03/24 |
| 10. |Personaje, caja_meta, meta | Terminado | [0,6,2] | [4,5,6] | 16/03/24 |
| 11. | Personaje_meta, pasillo | Terminado | [5,4] | [2,0] | 16/03/24 |
| 12. | Personaje_meta, meta | Terminado | [5,2] | [2,5] | 16/03/24 |
| 13. | Personaje_meta, caja, pasillo |Terminado | [5,1,4] | [2,0,1] | 16/03/24|
| 14. | Personaje_meta, caja, meta |Terminado | [5,1,2] | [2,0,6] | 16/03/24 |
| 15. | Personaje_meta, caja_meta, pasillo |Terminado | [5,6,4] | [2,5,1] | 16/03/24 |
| 16. | Personaje_meta, caja_meta, meta | Terminado | [5,6,2] | [2,5,6] | 16/03/24 |


### 6.4 Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Terminado | [0,4] | [4,0] | 16/03/24 |
| 6. | Personaje, meta  | Terminado | [0,2] | [4,5] |16/03/24 |
| 7. | Personaje, caja, pasillo | Terminado | [0,1,4] | [4,0,1] | 16/03/24 |
| 8. | Personaje, caja,  meta | Terminado | [0,1,2] | [4,0,6] | 16/03/24|
| 9. | Personaje, caja_meta, pasillo | Terminado | [0,6,4] | [4,5,1 ] | 16/03/24 |
| 10. |Personaje, caja_meta, meta | Terminado | [0,6,2] | [4,5,6] | 16/03/24 |
| 11. | Personaje_meta, pasillo | Terminado | [5,4] | [2,0] | 16/03/24 |
| 12. | Personaje_meta, meta | Terminado | [5,2] | [2,5] | 16/03/24 |
| 13. | Personaje_meta, caja, pasillo |Terminado | [5,1,4] | [2,0,1] | 16/03/24|
| 14. | Personaje_meta, caja, meta |Terminado | [5,1,2] | [2,0,6] | 16/03/24 |
| 15. | Personaje_meta, caja_meta, pasillo |Terminado | [5,6,4] | [2,5,1] | 16/03/24 |
| 16. | Personaje_meta, caja_meta, meta | Terminado | [5,6,2] | [2,5,6] | 16/03/24 |

### 6.5 Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Terminado | [0,4] | [4,0] | 16/03/24 |
| 6. | Personaje, meta  | Terminado | [0,2] | [4,5] |16/03/24 |
| 7. | Personaje, caja, pasillo | Terminado | [0,1,4] | [4,0,1] | 16/03/24 |
| 8. | Personaje, caja,  meta | Terminado | [0,1,2] | [4,0,6] | 16/03/24|
| 9. | Personaje, caja_meta, pasillo | Terminado | [0,6,4] | [4,5,1 ] | 16/03/24 |
| 10. |Personaje, caja_meta, meta | Terminado | [0,6,2] | [4,5,6] | 16/03/24 |
| 11. | Personaje_meta, pasillo | Terminado | [5,4] | [2,0] | 16/03/24 |
| 12. | Personaje_meta, meta | Terminado | [5,2] | [2,5] | 16/03/24 |
| 13. | Personaje_meta, caja, pasillo |Terminado | [5,1,4] | [2,0,1] | 16/03/24|
| 14. | Personaje_meta, caja, meta |Terminado | [5,1,2] | [2,0,6] | 16/03/24 |
| 15. | Personaje_meta, caja_meta, pasillo |Terminado | [5,6,4] | [2,5,1] | 16/03/24 |
| 16. | Personaje_meta, caja_meta, meta | Terminado | [5,6,2] | [2,5,6] | 16/03/24 |

### 6.6 Determina si se completo el nivel

Está función determina si todas las cajas estan en una meta, cuando esto sucede se debe cargar el siguiente nivel de juego.

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | -TERMINADO |13/04/24  |
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | TERMINADO | 13/04/24 |

### 6.7 Función extra

Como parte del reto de programar un Sokoban, hay que agregar alguna función especial al juego, como por ejemplo bajo ciertas condiciones empujar 2 cajas, colocar un temporizador por nivel, etc.

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | - | - |
