'''
Problema: beecrowd - 1014
Data: 2026.05.17
Estudante: Luana Eleza dos Santos
'''
# Objetivo: calcular o cnsumo de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: um valor inteiro X representando a distância total percorrida (em km), e um valor real Y representando o total de combustível gasto
# Processamento: consumo = X / Y
# Saída: consumo com 3 casas decimais seguido de "km/l"

# lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# calcula o consumo médio: quilômetros dividido por litros
consumo = X / Y

# exibe o resultadocom 3 casas decimais e a unidade em km/l
print(f"{X / Y :.3f} km/1")