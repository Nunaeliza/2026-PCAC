'''
Problema: beecrowd - 1014
Data: 2026.05.17
Estudante: Luana Eleza dos Santos
'''
# Objetivo: calcular o cnsumo de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada:
# Processamento:
# Saída: 

# lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# calcula o consumo médio: quilômetros dividido por litros
consumo = X / Y

# exibe o resultadocom 3 casas decimais e a unidade em km/l
print(f"{consumo = X / Y 3:.f} km/1")