# DESIGN PATTERNS

## Factory Method

### O **Factory Method** é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

## Exercícios:
### ** MonthlyStatement** : 
1 - Refatorar a classe MonthlyStatement (Factory Method)
     1 - Remover a regra de negócio de dentro dos ifs.
     2 - Remover os atributos para uma classe separada:

        self.call_cost: float
        self.sms_cost: float
        self.total_cost: float
     3 - A função generate vai retornar o objeto Customer com base no tipo CustomerType passado como parâmetro
2 - Criar as respectivas classes com base na classe Customer segregando as respectivas regras encontradas na monthly_statement

### 
