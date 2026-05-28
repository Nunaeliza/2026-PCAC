# ========================================================
# Disciplina : Pensamento Computacinal, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : adivinhe.py
# Autor      : Luana Eliza dos Santos
# Data       : 2026.05.28
# ========================================================

import random

# 1) Sorteamos o número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)

# 2) Pedimos um palpite (input devolve TEXTO; convertemos para inteiro)
palpite = int(input("Digite um número de 1 a 10: "))

# 3) Mostramos o resultado deste primeiro teste
print()