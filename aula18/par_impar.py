# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Luana Eliza dos Santos
# Data       : 2026.06.25 

import random

pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")
    numero_maquina = random.randint(0, 5)
    numero_jogador = int(input("Sua jogada (0 a 5): "))
    aposta_bruta = input("Sua aposta (Par ou Ímpar): ")
    aposta = aposta_bruta.lower().strip()
    opcoes = ["par", "impar"]

if aposta_bruta not in opcoes:
    print("Aposta inválida!")
    pontos_jogador = pontos_jogador + 1
else:
    quem = resultado(numero_jogador, numero_maquina)
    if quem == "Empate":
        print("🤝 Empate!")
    elif quem == "jogador":
        print("🎉 Você ganhou!")
    pontos_jogador = pontos_jogador + 1

soma = numero_jogador + numero_maquina
if numero_jogador % 2 == 0:
    print("par")
else:
    print("impar")

    print(f"{numero_maquina}")
    
def quem_venceu(soma, aposta):
    if soma % 2 == 0:
        paridade = "par"
    else:
        paridade = "impar"

    if paridade == aposta:
        return "jogador"
    else:
        return "maquina"

print("Placar -> Você", pontos_jogador, "| Máquina:", pontos_maquina)