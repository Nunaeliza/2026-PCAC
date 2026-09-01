# Fliperama da Luana

Um fliperama de terminal com três jogos, placar que não esquece e cadastro de jogadores. Projeto da disciplina PCAP, 1º ano do Técnico em Informática do IFPR.

## O que ele faz

- Três jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura e Par ou Ímpar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alterar e excluir

## Como rodar

```
cd fliperama
python3 main.py
```

## Os arquivos

- `main.py` - o gabinete: menu, placar e chamadas
- `telas.py` - ferramentas visuais
- `modulos.py` - ferramentas de lógica: as três funções que perguntam e conferem
- `palacr.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
- `adivinhe.py`, `ppt.py`, `parimpar.py` - um arquivo por jogo
- `placar.csv` e `jogadores.csv` - os dados, que nascem sozinhos

A função `ler_texto` ficou no `modulos.py` porque o apelido não vai ser a única coisa do programa que vai usar, essa função é uma "resposta" no código.

## Deonde ele veio

- Aula 20: os três jogos viraram um programa só, com módulos e menu
- Aula 21: entrou o Pedra-Papel-Tesoura e o plcar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador
- Espaço no apelido pode dar errado e você vai ter que colocar outro apelido