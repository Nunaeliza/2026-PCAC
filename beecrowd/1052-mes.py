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
mes = int(input())

# Estrutura if/elif/else: testa cada condição em sêquencia
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if mes == 1:
    print("January")
elif mes == 2:
    print("February")
elif mes == 3:
    print("March")
elif mes == 4:
    print("April")
elif mes == 5:
    print("May")
elif mes == 6:
    print("June")
elif mes == 7:
    print("July")
elif mes == 8:
    print("August")
elif mes == 9:
    print("September")
elif mes == 10:
    print("October")
elif mes == 11:
    print("November")
elif mes == 12:
    print("December")
else:
    # Nenhuma condição acima foi verdadeira - ano não está na tabela
    print("mes nao encontrado")