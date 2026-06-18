# ✊✋✌️ Pedra-Papel-Tesoura
​
Jogo de Pedra-Papel-Tesoura feito em Python na disciplina PCAP (Aula 17).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py
3. A cada rodada, digite pedra, papel ou tesoura.
4. Ao fim das 5 rodadas, o programa mostra o placar final.
​
## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia uma jogada (random.choice) e lê a sua.
O texto digitado é limpo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas.
​
## 🧠 O que eu pratiquei
- Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel ou tesoura
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Sub-rotinas (def/return): isolar a regra do jogo
​
## 🎯 Autoavaliação
Conceito pretendido: [ C ]
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: ppt.py, linhas __ a __: O jogo funciona do jeito normal - você digita se você quer Pedra, Papel ou Tesoura e o computador joga também.
- Trabalho com texto .........: ppt.py, linha __  (.lower().strip(), in, ==): É meio complicado de entender para que serve, mas o (.lower()) serve para deixar tudo minúsculo, e (.strip()) remove oa espaços do começo e do fim.
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: ppt.py, linha __  (o que eu criei — níveis B/A)
​
Autor: Luana Eliza dos Santos