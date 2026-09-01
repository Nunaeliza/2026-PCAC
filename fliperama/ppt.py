#=============================================================================================================
# Arquivo    : ppt.py (pasta fliperama)
# Conceitos  : Jogo com modulo, lista como tabela de nomes, função com retorno, operador % para dar a volta
# Base       : Jogo da aula 17 (atividade 11)
# Autor      : Luana Eliza dos Santos
# Data       : 2026.08.11
# ============================================================================================================

# importa função randint da biblioteca random, que sorteia um número inteiro aleatorio em um intervalo dfinido
from random import randint

# importa as funções titulo e linha do arquivo telas.py
from telas import titulo, linha

# importa a função ler-opcao que valida a entrada do usuario do arquivo modulos.py
from modulos import ler_opcao

JOGADA = ['PEDRA', 'PAPEL', 'TESOURA']

# Define o ganhador
def quem_vence(jogador, computador):
    if jogador == computador:
        return 'empate'
    elif jogador == (computador + 1) % 3:
        return 'jogador'
    return 'computador'


# Mostar jogadas
def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você jogou ' + JOGADA[jogador] + '.')
        print('Computador jogou ' + JOGADA[computador] + '.')

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguem venceu!')
        elif resultado == 'jogador':
            pontos_jogador += 1
            print('Você venceu essa rodada!')
        elif resultado == 'computador':
            pontos_computador += 1
            print('Computador venceu essa rodada!')

        linha()
        print(f'Placar: Jogador {pontos_jogador} X {pontos_computador} Computador')
        linha()

    if pontos_jogador > pontos_computador:
        titulo('YOU WIN!')
    else:
        titulo('YOU LOSE!')

