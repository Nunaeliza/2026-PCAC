# Fliperama em C++ (MeuApp v4.0)

## O que e


## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: o arquivo principal onde fica os codigos principais para o funcionamento do jogo.
- jogadores.csv: cada linha guarda o nome cadastrado e quantos pontos a pessoa fez.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 69) | apelidos.push_back(novo) (l. 91) |
| comparar apelidos | strcmp(...) == 0 (l. ) | == (l. ) |