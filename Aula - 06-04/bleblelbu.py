gols1= int(input("Digite o número de gols marcados pelo Flamengo: "))
gols2= int(input("Digite o número de gols marcados pelo Vasco: "))

if gols1>gols2:
    print("Flamengo vencedor")
elif gols2>gols1:
    print("Vasco vencedor")
elif gols1==gols2:
    print("EMPATE")
