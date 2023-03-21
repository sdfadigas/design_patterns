# DESIGN PATTERNS

## Strategy

### O _Strategy_ é um padrão de projeto comportamental que permite que você defina uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis.


## Exercícios:
### **TextProcessor**: 
- Suponha que queremos fornecer uma API com duas estratégias diferentes para formatar lista:
     - Em `MarkdownListStrategy` quando passado uma lista qualquer de string deve ser formatado da seguinte forma Ex:
        * foo
        * bar
        * baz
     - Em `HtmlListStrategy`, quando passado uma lista qualquer de string deve ser formatado da seguinte forma Ex:
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
- Implemente essas duas estratégias, bem como o próprio TextProcessor para avaliar qual estratégia de formatação usada.

### 
