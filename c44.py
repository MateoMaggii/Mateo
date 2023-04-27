# Función para determinar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Ingreso de los números y detección de los números primos
suma_primos = 0
numeros = input("Ingrese una serie de números separados por comas: ")
numeros = numeros.split(",")
for num in numeros:
    num = int(num)
    if es_primo(num):
        print(num, "es primo")
        suma_primos += num

# Impresión de la suma total de los números primos
print("La suma total de los números primos ingresados es:", suma_primos)





