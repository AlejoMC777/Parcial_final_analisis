def calcular_cuadrados(n):
    print("{:<10}{:<10}{:<10}".format("Número", "Cuadrado", "Método"))
    print("-----------------------------------")

    resultado = 0  # Variable para almacenar la suma acumulada

    for i in range(1, n + 1):
        cuadrado = i * i  # Calculamos el cuadrado del número

        metodo = ""  # Variable para almacenar el método actual
        suma = 0  # Variable para almacenar la suma de los números impares

        # Generamos la cadena del método sumando los números impares hasta el cuadrado
        for j in range(1, cuadrado + 1, 2):
            suma += j
            metodo += str(j)

            if suma >= cuadrado:
                break
            else:
                metodo += "+"

        resultado += cuadrado  # Acumulamos el cuadrado en la suma acumulada

        print("{:<10}{:<10}{:<10}".format(i, cuadrado, metodo))

# Solicitamos el valor de "n" al usuario
n = int(input("Ingrese un número entero positivo: "))

# Llamamos a la función para calcular los cuadrados
calcular_cuadrados(n)
