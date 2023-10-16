# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
# Solicitar ao usuário que escolha uma operação
operacao = input("Selecione uma operação matemática\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n")

# Solicitar ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar a operação com base na escolha do usuário
if operacao == '1':
    print("Resultado:", num1 + num2)
elif operacao == '2':
    print("Resultado:", num1 - num2)
elif operacao == '3':
    print("Resultado:", num1 * num2)
elif operacao == '4':
    print("Resultado:", num1 / num2)
else:
    print("Opção inválida")