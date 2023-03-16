# DESIGN PATTERNS

## Abstract Factory

### O **Abstract Factory** é um padrão de projeto criacional que permite que você produza famílias de objetos relacionados sem ter que especificar suas classes concretas.

## Exercícios:
### **Person**: 
- Você recebe uma classe chamada `Person`.
- A pessoa tem 3 atributos: `id`, `name` e `age`.
- Implemente uma `PersonFactory` que tenha um método `create_person()` não estático que pegue o nome de uma pessoa e retorne uma pessoa inicializada com este `age`, `name` e um `id`.
- O `id` da pessoa deve ser definido como um índice baseado em 0 do objeto criado.
- Assim, a primeira pessoa que a fábrica fizer deverá ter Id=0, a segunda Id=1 e assim sucessivamente.
   - Pra esse exercício, pesquisem sobre variável de classe e variável da referencia em python pra resolver.

### 
