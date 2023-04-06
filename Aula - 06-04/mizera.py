num1= int(input("Digite um número: "))
num2= int(input("Digite outro número: "))
codigo= int(input("Digite o código: "))

if codigo == 1 or 2:
    if num1>num2:
        print(num1, "É o maior número")
    elif num2>num1:
        print(num2, "É o maior número")
    else:
        print("Os números são iguais")
elif codigo == 3 or 4:
    if num1>num2:
        print(num2, "é o menor número")
    elif num2>num1:
        print(num1, "é o menor número")
    else:
        print("Os números são iguais")
else:
    print("Erro de código")