import tensorflow as tf
import numpy as np

def main():
    print("=== Operaciones de Matrices con TensorFlow ===")
    filas_a = int(input("Ingrese el número de filas para la matriz A: "))
    columnas_a = int(input("Ingrese el número de columnas para la matriz A: "))
    filas_b = int(input("Ingrese el número de filas para la matriz B: "))
    columnas_b = int(input("Ingrese el número de columnas para la matriz B: "))
    matriz_a = tf.random.uniform(shape=[filas_a, columnas_a], minval=1, maxval=21, dtype=tf.int32)
    matriz_b = tf.random.uniform(shape=[filas_b, columnas_b], minval=1, maxval=21, dtype=tf.int32)
    print("\nMatriz A:")
    print(matriz_a.numpy())
    print("\nMatriz B:")
    print(matriz_b.numpy())
    if filas_a == filas_b and columnas_a == columnas_b:
        resultado_suma = tf.add(matriz_a, matriz_b)
        
        print("\nResultado de la suma A + B:")
        print(resultado_suma.numpy())
    else:
        print("\nNo se puede realizar la suma: las dimensiones no coinciden")
    if columnas_a == filas_b:
        resultado_multiplicacion = tf.matmul(matriz_a, matriz_b)
    
        print("\nResultado de la multiplicación A * B:")
        print(resultado_multiplicacion.numpy())
    else:
        print("\nNo se puede realizar la multiplicación: las dimensiones no son compatibles")
        print(f"Para multiplicar matrices, el número de columnas de A ({columnas_a}) debe ser igual al número de filas de B ({filas_b})")

if __name__ == "__main__":
    print("TensorFlow version:", tf.__version__)
    main()