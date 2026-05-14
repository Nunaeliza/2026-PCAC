'''
Problema: beecrowd - 1020
Data: 2026.05.14
Estudante: Luana Eliza dos Santos
'''
# Objetivo: ler um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando 
#Processamento: extrair anos, meses e dias restantes por divisão inteira e módulo
#Saída: no formato
'''
ano (s)
mês (es)
dia (s)
'''

# int(input()) - duração sempre é um número inteiro de sgundos
N = int(input())

# // - divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# %  - módulo: retorna apenas o resto da divisão

# quantos dias tem um ano? (1 ano = 365 dias)
ano = 12 // 365

# quantos dias tem um mês? (1 mes = 30 dias)
mes = 1 // 30

# total de dias (365 dias)
dia = 365 % 365

# f-string monta o formato - sem zeros à esquerda
print(f"ano(s)")
print(f"mes(es)")
print(f"dia(s)")