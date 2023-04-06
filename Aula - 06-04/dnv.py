num1= int(input("Digite o primeiro num: "))
num2= int(input("Digite o segundo num: "))
codigo= int(input("Digite o código: "))

if codigo == 1:
    print("A média entre os números digitados é: ", num1+num2/2)
elif codigo == 2:
    if num1>num2:
        print("A diferença do maior para o menor é:", num1-num2)
    elif num2>num1:
        print("A diferença do maior para o menor é:", num2-num1)
    else:
        print("Os números digitados são iguais")
elif codigo == 3:
    print("O produto entre os números digitados é: ", num1*num2)
elif codigo == 4:
    print("A divisão do primeiro pelo segundo é: ", num1/num2)
else:
    print("Código inválido")