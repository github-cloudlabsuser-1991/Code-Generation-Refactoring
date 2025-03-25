# Calculadora Basica en Python

import math

# Metodo Sumar
def sumar(a, b):
    return a + b

# Metodo Restar
def restar(a, b):
    return a - b

# Metodo Multiplicar
def multiplicar(a, b):
    return a * b

# Metodo Dividir
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Metodo Potencia
def potencia(a, b):
    return a ** b

# Metodo Raiz Cuadrada
def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de un número negativo"
    return math.sqrt(a)

# Metodo Principal
def main():
    print("Calculadora Básica en Python")
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz Cuadrada")

    opcion = int(input("Ingrese su opción (1/2/3/4/5/6): "))

    if opcion in [1, 2, 3, 4, 5]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado:", sumar(num1, num2))
        elif opcion == 2:
            print("Resultado:", restar(num1, num2))
        elif opcion == 3:
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == 4:
            print("Resultado:", dividir(num1, num2))
        elif opcion == 5:
            print("Resultado:", potencia(num1, num2))
    elif opcion == 6:
        num = float(input("Ingrese el número: "))
        print("Resultado:", raiz_cuadrada(num))
    else:
        print("Opción no válida")

def pruebas_unitarias():
    print("\nPruebas Unitarias:")
    print("Sumar 2 + 3:", sumar(2, 3))  # Esperado: 5
    print("Restar 5 - 2:", restar(5, 2))  # Esperado: 3
    print("Multiplicar 3 * 4:", multiplicar(3, 4))  # Esperado: 12
    print("Dividir 10 / 2:", dividir(10, 2))  # Esperado: 5.0
    print("Dividir 10 / 0:", dividir(10, 0))  # Esperado: Error: División por cero
    print("Potencia 2 ** 3:", potencia(2, 3))  # Esperado: 8
    print("Raíz Cuadrada de 16:", raiz_cuadrada(16))  # Esperado: 4.0
    print("Raíz Cuadrada de -4:", raiz_cuadrada(-4))  # Esperado: Error: Raíz cuadrada de un número negativo

# Casos de Prueba
if __name__ == "__main__":
    modo = input("Seleccione el modo (calculadora/pruebas): ").strip().lower()
    if modo == "calculadora":
        main()
    elif modo == "pruebas":
        pruebas_unitarias()
    else:
        print("Modo no válido")