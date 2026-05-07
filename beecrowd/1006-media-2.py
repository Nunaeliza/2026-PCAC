'''
Problema: beecrowd - 1006
Data: 2026.05.07
Estudante: Luana Eliza dos Santos
'''
# Objetivo: Ler 3 valores, no caso A, B e C, que que são as notas dos alunos. Em seguida, calcular a media do aluno. A tem peso 2, B tem peso 3 e C tem peso 5. Cada nota pode ir de 0 até 10.0, sempre com uma casa decimal

# --- ANÁLISE (LIAC) ---
# Entrada: o arquivo de entrada contém 3 valores com uma casa decimal
# Processamento: média ponderada = (A * 2 + B * 3 + C * 5) / 10
# Saída: exibir no formato exato "MEDIA = valor" com 1 casa decimal

# float(input()) - notas podem ter casas decimais (ex: 5.0, 6.0, 7.0)
A = float(input())
B = float(input())
C = float(input())
media = (A * 2 + B * 3 + C * 5) / 10

# nota A tem peso 2, nota B tem peso 3 e a nota C tem peso 5
# a soma dos pesos é 10 - divide-se por 10 para obter a média ponderada = (A * 2 + B * 3 + C * 5) / 10

# :.1f dentro da f-string - formata o número com exatamente 1 casa decimal
# o enunciado exige espaço antes e depois do = - seguir à risca
print(f"MEDIA = {media:.1f}")