salario= float(input("Digite o seu salário: "))

if salario<300:
    print("Seu percentual de aumento foi de 45%, seu salário reajustado é: ", salario*1.45)
elif salario>=300 and salario<600:
    print("Seu percentual de aumento foi de 25%, seu salário reajustado é:", salario*1.25)
elif salario>600:
    print("Seu percentual de aumento foi de 15%, seu salário reajustado é: ", salario*1.15)
else:
    print("Usuário perturbado")