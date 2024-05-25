contador1 = 0
contador2 = 0
for contador in range(0,3,1):
    jogadorN1 = int(input(f" Jogador 1, escolha uma dessas opções: \n"
                         f" 1- Pedra \n"
                         f" 2- Papel \n"
                         f" 3- Tesoura \n"
                         f" --> "))
    jogadorN2 = int(input(f" Jogador 2, escolha uma dessas opções: \n"
                         f" 1- Pedra \n"
                         f" 2- Papel \n"
                         f" 3- Tesoura \n"
                         f" --> "))

    if jogadorN1 == 1 and jogadorN2 == 3 or jogadorN1 == 2 and jogadorN2 == 1 or jogadorN1 == 3 and jogadorN2 == 2:
        print(f" O Jogador 1 venceu!")
        contador1 += 1
    elif jogadorN2 == 1 and jogadorN1 == 3 or jogadorN2 == 2 and jogadorN1 == 1 or jogadorN2 == 3 and jogadorN1 == 2:
        print(f" O Jogador 2 venceu!")
        contador2 += 1
    else:
        print("Empate! Vamos tentar mais uma vez")

    if contador1 == 2 or contador2 == 2:
        print("Não tem chance de virada!")
        break

print(f" \n PLACAR FINAL: \n"
    f"Jogador 1 = {contador1} \n"
    f"Jogador 2 = {contador2} \n")

print("Fim de jogo!")