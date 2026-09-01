# ============================================================
# Arquivo:       parimpar.py
# Disciplina:    2026-PCAP
# Aula:          20
# Autor:         Luana Eliza dos Santos
# Data:          2026.09.01
# Conceitos: 
# ==========================================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao

JOGADA = ["Par", "Impar"]

def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    elif jogador == (computador + 0) % 2:
        return "jogador"
    elif jogador == (computador + 1) % 2:
        return "computador"


def mostrar_jogadas():
    print("[0] Par")
    print("[1] Impar")
    linha()

def jogar_parimpar():
    titulo("PAR OU IMPAR")

pontos_jogador = 0
pontos_computador = 0

while pontos_jogador < 2 and pontos_computador < 2:
    mostrar_jogadas()

    jogador = int(ler_opcao("Sua jogada", ["0", "1"]))
    computador = randint(0, 1)

    print("Você jogou " + JOGADA[jogador] + ".")
    print("Computador jogou " + JOGADA[computador] + ".")

    resultado = quem_vence(jogador, computador)

    if resultado == "empate":
        print("Empate! Ninguem venceu!")
    elif resultado == "jogador":
        pontos_jogador += 1
        print("Você venceu essa rodada!")
    elif resultado == "computador":
        pontos_computador += 1
        print("Computador venceu essa rodada!")

    linha()
    print(f"Placar: Jogador {pontos_jogador} X {pontos_computador} Computador")
    linha()

if pontos_jogador > pontos_computador:
    titulo("YOU WIN")
else:
    titulo("YOU LOSE")