# ============================================================
# Arquivo:       main.py
# Disciplina:    2026-PCAP
# Aula:          20
# Autor:         Luana Eliza dos Santos
# Data:          2026.08.04
# Conceitos: 
# ===========================================================

# Importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores

NOMES_DOS_JOGOS = ["Adivinhe o Número", "Pedra-Papel-Tesoura", 
                   "Par ou Impar"]
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

def mostrar_placar():
    titulo("PLACAR")
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "X")

NOME_DO_DONO = "LUANA"
OPCOES = ["0", "1", "2", "3", "4"]

def mostrar_menu():
    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("[1] Adivinhe o Numero")
    print("[2] Pedra-Papel-Tesoura")
    print("[3] Par ou Impar")
    print("[4] Jogadores")
    print("[0] Sair")
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo("Ate a Proxima!")
        break

    if opcao == "4":
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

    if opcao == "1":
        jogar_adivinhe()
    elif opcao == "2":
        jogar_ppt()
    else:
        jogar_parimpar()

    input("Pressione Enter para voltar ao menu...")