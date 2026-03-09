def calculadora():
    print("=== Calculadora em Python ===")

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2

            print(f"Resultado: {resultado}")
        except ValueError:
            print("Entrada inválida! Digite números.")

        continuar = input("Deseja fazer outra conta? (s/n): ").lower()
        if continuar != "s":
            print("Calculadora encerrada.")
            break


calculadora()