def calculadora():
    print("Bienvenido a la calculadora. Escribe 'salir' para terminar.")
    while True:
        operacion = input("Introduce la operación (suma, resta, multiplicacion, division): ").strip().lower()
        if operacion == 'salir':
            print("Saliendo de la calculadora.")
            break

        if operacion not in ['suma', 'resta', 'multiplicacion', 'division']:
            print("Operación no válida. Inténtalo de nuevo.")
            continue

        try:
            num1 = input("Introduce el primer número: ")
            if num1.lower() == 'salir':
                print("Saliendo de la calculadora.")
                break
            num1 = float(num1)

            num2 = input("Introduce el segundo número: ")
            if num2.lower() == 'salir':
                print("Saliendo de la calculadora.")
                break
            num2 = float(num2)
        except ValueError:
            print("Entrada no válida. Asegúrate de introducir números.")
            continue

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                continue
            resultado = num1 / num2
        else:
            print("Operación desconocida.")
            continue

        print(f"El resultado de la {operacion} es: {resultado}")

if __name__ == "__main__":
    calculadora()

