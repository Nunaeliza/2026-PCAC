print("=== ADIVINHE O NUMERO ===")
segredo = 7
palpite = int(input("Digite um numero de 1 a 10: "))
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)

# O que estava errado nesse código era que estava faltando int() antes do input().