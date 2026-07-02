Fundamentos -- Jogo Pedra, Papel e Tesoura

Operadores lógicos:
1: if jogador == "pedra" and maquina == "tesoura":
        return "jogador"

    Esse código funciona quando um jogador joga pedra (nesse caso) e máquina joga tesoura, a máquina perdeu, pois pedra quebra tesoura então o ponto vai para o jogador.

Repetição:
1: for rodada in range(1, 6):

    Esse código é uma repetição, ele vai repetir a rodada 5 vezes, o limite final (6) vai ficar de fora, mas para o jogo funcionar com 5 rodadas precisa por o número 6 no final.

Saída:
1: print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)

    Esse código organiza e marca os pontos do jogador e da máquina e quem ganhou.