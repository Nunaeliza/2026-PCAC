'''
Problema: beecrowd - 1052
Data: 2026.05.14
Estudante: Luana Eliza dos Santos
'''
# Objetivo: ler um valor inteiro de 1 e 12 e como resposta o mês do ano por extenso, em inglês

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representando os anos
# Processamento: comparar o ano lido com cada código da tabela usando if/elif/else
# Saída: mês do ano correspondente em inglês

# int(input()) - DDD é sempre um número inteiro
ano = int(input())

# Estrutura if/elif/else: testa cada condição em sêquencia
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if ano == 1:
    print("January")
elif ano == 2:
    print("February")
elif ano == 3:
    print("March")
elif ano == 4:
    print("April")
elif ano == 5:
    print("May")
elif ano == 6:
    print("June")
elif ano == 7:
    print("July")
elif ano == 8:
    print("August")
elif ano == 9:
    print("September")
elif ano == 10:
    print("October")
elif ano == 11:
    print("November")
elif ano == 12:
    print("December")
else:
    # Nenhuma condição acima foi verdadeira - ano não está na tabela
    print("ano nao encontrado")