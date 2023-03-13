# DESIGN PATTERNS

## Observer

### O **Observer** é um padrão de projeto comportamental que permite que você defina um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

## Exercícios:
### **Game of Rats**: 
- Imagine um jogo onde um ou mais ratos podem atacar um jogador.
- Cada rato individual tem um valor inicial de 'ataque' de 1.
- No entanto, os ratos atacam como um enxame, então o valor de 'ataque' de cada rato é realmente igual ao número total de ratos em jogo.
  - Exemplo:
    - 1 rato = ataque 1
    - 2 ratos = ataque 2
    - (...)
- Dado que um rato entra no jogo pelo construtor.

