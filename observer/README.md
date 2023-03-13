- Imagine um jogo onde um ou mais ratos podem atacar um jogador.
- Cada rato individual tem um valor inicial de 'ataque' de 1.
- No entanto, os ratos atacam como um enxame, então o valor de 'ataque' de cada rato é realmente igual ao número total de ratos em jogo.
  - Exemplo:
    - 1 rato = ataque 1
    - 2 ratos = ataque 2
    - (...)
- Dado que um rato entra no jogo pelo construtor.

Não precisa criar nada!!!! Como classe ou lista, já temos tudo que precisamos, é só abstrair as responsabilidades, o exemplo do rato é uma implementação real, diferente da conceitual.


Dica4: 
Olhem as imagens... repare que nosso Event(list) é a mesma coisa que se tivessemos implementando o código conceitual, a diferença é que o nosso é mais dinâmico, o Event() assume a responsabilidade de interar os métodos e não a classe.


NÃO GASTEM ENERGIA MENTAL TENTANDO LER O CÓDIGO, FAÇAM O DEBUG!!!

GameOfRatsSENAI.7z
- Imagine um jogo onde um ou mais ratos podem atacar um jogador.
- Cada rato individual tem um valor inicial de 'ataque' de 1.
- No entanto, os ratos atacam como um enxame, então o valor de 'ataque' de cada rato é realmente igual ao número total de ratos em jogo.
  - Exemplo:
    - 1 rato = ataque 1
    - 2 ratos = ataque 2 (rato1 + rato2)
    - 3 ratos = ataque 3 (rato1 + rato2 + rator3)
    - (...)
      - Analisar o main.py
- Um rato entra no jogo pelo construtor da classe Rat.