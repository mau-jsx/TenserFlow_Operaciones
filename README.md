# Operaciones de Matrices con TensorFlow

Este proyecto implementa operaciones básicas de matrices (suma y multiplicación) utilizando la biblioteca TensorFlow. El sistema permite al usuario definir las dimensiones de las matrices y genera automáticamente los valores aleatorios entre 1 y 20 para cada matriz.

## Descripción

El programa realiza las siguientes operaciones:

- Solicita al usuario las dimensiones para dos matrices (A y B)
- Genera valores aleatorios entre 1 y 20 para cada matriz utilizando TensorFlow
- Realiza la suma de matrices (A + B) utilizando la función nativa de TensorFlow
- Realiza la multiplicación de matrices (A \* B) utilizando la función nativa de TensorFlow
- Verifica que las dimensiones sean compatibles para cada operación

## Requisitos

- Python 3.9, 3.10 o 3.11 (recomendado)
- TensorFlow 2.19 o superior

## Instalación

1. Asegúrate de tener instalada una versión compatible de Python
2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Instala TensorFlow:
   ```
   pip install tensorflow
   ```

## Uso

1. Ejecuta el script:
   ```
   python matriz_tensorflow.py
   ```
2. Introduce las dimensiones de las matrices cuando se te solicite
3. El programa generará los valores aleatorios y mostrará:
   - Las matrices generadas
   - El resultado de la suma (si es posible)
   - El resultado de la multiplicación (si es posible)

## Ejemplos

### Ejemplo 1: Matrices compatibles para suma y multiplicación

```
=== Operaciones de Matrices con TensorFlow ===
Ingrese el número de filas para la matriz A: 2
Ingrese el número de columnas para la matriz A: 3
Ingrese el número de filas para la matriz B: 3
Ingrese el número de columnas para la matriz B: 2

Matriz A:
[[15  8 12]
 [ 5  3 19]]

Matriz B:
[[11  7]
 [16  4]
 [ 9 18]]

No se puede realizar la suma: las dimensiones no coinciden

Resultado de la multiplicación A * B:
[[401 410]
 [226 377]]
```

### Ejemplo 2: Matrices compatibles solo para suma

```
=== Operaciones de Matrices con TensorFlow ===
Ingrese el número de filas para la matriz A: 2
Ingrese el número de columnas para la matriz A: 2
Ingrese el número de filas para la matriz B: 2
Ingrese el número de columnas para la matriz B: 2

Matriz A:
[[10  5]
 [ 7 12]]

Matriz B:
[[ 8  3]
 [15  6]]

Resultado de la suma A + B:
[[18  8]
 [22 18]]

Resultado de la multiplicación A * B:
[[155  45]
 [236  87]]
```

## Notas importantes

- Para realizar la suma de matrices, ambas matrices deben tener exactamente las mismas dimensiones.
- Para realizar la multiplicación de matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.
- Los valores se generan aleatoriamente utilizando TensorFlow, por lo que serán diferentes en cada ejecución.

## Estructura del proyecto

- `matriz_tensorflow.py`: Contiene el código principal para la manipulación de matrices con TensorFlow
- `README.md`: Este archivo con la documentación del proyecto
