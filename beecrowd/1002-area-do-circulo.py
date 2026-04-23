'''
Problema: beecrowd - 1002
Data: 2026.04.23
Estudante: Luana Eliza dos Santos
'''
# Objetivo: calcular a área de uma circunferência com a fórmula area = n . raio², considerando que para este problema n = 3.14159. Efetue o calculo da área, elevando o valor de raio ao quadrado e multiplicando por n.

# --- ANÁLISE (LIAC) ---
# Entrada: contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
# Processamento: aplicar a formula da area de uma circunferência 
# Saída: apresentar a mensagem "A=" seguido pelo valor da variável area, com 4 casas após o ponto decimal

# Leitura do raio como número decimal
R = float(input())

# Defina pi conforme o enunciado indica
pi = 3.14159

# Qual é a fórmula da área do circulo?
AREA = pi * R ** 2

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"A={AREA:.4f}")