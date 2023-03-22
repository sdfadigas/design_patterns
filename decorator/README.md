# DESIGN PATTERNS

## Decorator

### O _Decorator_ é um padrão de projeto estrutural que permite que você acople novos comportamentos para objetos ao colocá-los dentro de invólucros de objetos que contém os comportamentos.

## Exercícios:
### **Shape**: 
- Você recebe dois tipos, Circle e Square, e um decorador chamado ColoredShape.
- O decorador adiciona a cor à saída da string para uma determinada forma, assim como fizemos no classic decorator. 
- Há um truque: o decorador agora tem um método resize() que deve redimensionar a forma subjacente.
- No entanto, apenas o Circle possui um método resize(); o Square não - não o adicione!
Dica:
        r = getattr(self.shape, 'resize', None)
        if callable(r):
....
- Você é solicitado a concluir a implementação de ColoredShape.



- O resultado deve ser:
A circle of radius 5 has the color red  
A circle of radius 10 has the color red  
A square with side 2 has the color blue  
A square with side 2 has the color blue
