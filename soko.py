# Sokoban

## 0. Objetivo

Programar el juego Sokoban en una versión retro para consola.

## 1. Reglas del juego

El juego sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar totas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando numeros para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

mapa = [
            [3,3,3,3,3],
            [3,4,4,4,3],
            [3,4,0,4,3],
            [3,4,4,4,3],
            [3,3,3,3,3]
        ]

### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje meta
- 6 - Caja meta

## 3. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover.

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo

## 4. Función a implementar

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Por hacer | - | | - |
| 1. | Repetir el juego hasta terminar el nivel. | Por hacer | - | | - |
| 2. | Imprimir mapa.| Por hacer | - |
| 3. | Leer el movimiento. | Por hacer | - |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Terminado | [0,4] | [4,0] | 16/03/24 |
| 6. | Personaje, meta  | Terminado | [0,2] | [4,6] |16/03/24 |
| 7. | Personaje, caja, pasillo | Terminado | [0,1,4] | [4,0,1] | 16/03/24 |
| 8. | Personaje, caja,  meta | Terminado | [0,1,2] | [4,0,6] | 16/03/24 |
| 9. | Personaje, caja_meta, pasillo | Terminado | [0,6,4] | [4,5,1] | 17/03/24 |
| 10. |Personaje, caja_meta, meta | Terminado | [0,6,2] | [4,5,6] | 17/03/24|
| 11. | Personaje_meta, pasillo | Terminado| [5,4] | [2,0] | 17/03/24 |
| 12. | Personaje_meta, meta |Terminado | [5,2] | [2,5] | 17/03/24|
| 13. | Personaje_meta, caja, pasillo | Terminado | [5,1,4] | [2,0,1] | 17/08/2024 |
| 14. | Personaje_meta, caja, meta |Terminado | [5,1,2] | [2,0,6] | 17/08/2024|
| 15. | Personaje_meta, caja_meta, pasillo | Terminado | [5,6,4] | [2,5,1] | 17/08/2024 |
| 16. | Personaje_meta, caja_meta, meta | Terminado [5,6,2] | [2,5,6] | 17/08/2024|

## Izquierda

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 17. | Personaje y espacio | Por hacer | - |
| 18. | Personaje y meta | Por hacer | - |
| 19. | Personaje, caja y espacio | Por hacer | - |
| 20. | Personaje, caja y meta | Por hacer | - |
| 21. | Personaje, caja_meta y espacio | Por hacer | - |
| 22. | Personaje, caja_meta y meta | Por hacer | - |
| 23. | Personaje_meta y espacio | Por hacer | - |
| 24. | Personaje_meta y meta | Por hacer | - |
| 25. | Personaje_meta, caja y espacio | Por hacer | - |
| 26. | Personaje_meta, caja y meta | Por hacer | - |
| 27. | Personaje_meta, caja_meta y espacio | Por hacer | - |
| 28. | Personaje_meta, caja_meta y meta | Por hacer | - |

## Arriba

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 29. | Personaje y espacio | Por hacer | - |
| 30. | Personaje y meta | Por hacer | - |
| 31. | Personaje, caja y espacio | Por hacer | - |
| 32. | Personaje, caja y meta | Por hacer | - |
| 33. | Personaje, caja_meta y espacio | Por hacer | - |
| 34. | Personaje, caja_meta y meta | Por hacer | - |
| 35. | Personaje_meta y espacio | Por hacer | - |
| 36. | Personaje_meta y meta | Por hacer | - |
| 37. | Personaje_meta, caja y espacio | Por hacer | - |
| 38. | Personaje_meta, caja y meta | Por hacer | - |
| 39. | Personaje_meta, caja_meta y espacio | Por hacer | - |
| 40. | Personaje_meta, caja_meta y meta | Por hacer | - |

## Abajo

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 41. | Personaje y espacio | Por hacer | - |
| 42. | Personaje y meta | Por hacer | - |
| 43. | Personaje, caja y espacio | Por hacer | - |
| 44. | Personaje, caja y meta | Por hacer | - |
| 45. | Personaje, caja_meta y espacio | Por hacer | - |
| 46. | Personaje, caja_meta y meta | Por hacer | - |
| 47. | Personaje_meta y espacio | Por hacer | - |
| 48. | Personaje_meta y meta | Por hacer | - |
| 49. | Personaje_meta, caja y espacio | Por hacer | - |
| 50. | Personaje_meta, caja y meta | Por hacer | - |
| 51. | Personaje_meta, caja_meta y espacio | Por hacer | - |
| 52. | Personaje_meta, caja_meta y meta | Por hacer | - |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  | Por hacer | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | Por hacer | - |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | Por hacer | - |
