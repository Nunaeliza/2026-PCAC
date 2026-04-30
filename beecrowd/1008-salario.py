'''
Problema: beecrowd - 1008
Data: 2026.04.30
Estudante: Luana Eliza dos Santos
'''
# Objetivo: escrever um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcular o salário desse funcionário. Em seguida mostrar o número e o salário do funcionário, com duas casas decimais

# --- ANÁLISE (LIAC) ---
# Entrada: contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada
# Processamento: multiplicar as horas trabalhadas e o valor que ele recebe por hora
# Saída: imprima o número e o salário do funcionário, com um espaço em branco antes e depois da igualdade. No caso do salario também deve haver um espaço em branco após o $

# Leitura das entradas - observe o enunciado: quantas variáveis e de qual tipo?
N = int(input())
H = int(input())
V = float(input())

# Calcule o salário - use o 1009 como referência de estrutura
SAL = H * V

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")