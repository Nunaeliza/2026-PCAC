# Fliperama em C (MeuApp v3.0)

## O que é
O fliperama em C junta tres jogos (Adivinhe o Numero, Pedra-Papel-Tesoura e Par ou Impar) em um unico arquivo, mas funciona da mesma forma que o fliperama em python. 

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c: o arquivo principal onde fica o codigo do fliperama e os tres jogos.
- jogadores.csv: guarda os apelidos e os pontos dos jogadores.

## Python x C: o que mudou
| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
|guardar um jogador | jogadores.append(novo) (Linha 29) | strcpy(apelidos[qtd], novo) (Linha 69) |
| comparar apelidos | == (Linha 59) | strcmp(...) == 0 (Linha 51) |
| abrir sem arquivo | exists(ARQUIVO) (Linha 119) | fopen == NULL (Linha 128) |

## O que o C me obrigou a decidir

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | fliperama.c |
| 2. Cadastro: menu, funcoes e vetores | B | fliperama.c |
| 3. Jogo e partidas | B | fliperama.c |
| 4. Persistencia | B | fliperama.c |
| 5. Documentacao e comparacao | B | fliperama.c |