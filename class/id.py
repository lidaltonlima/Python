"""Docstring for the Entity class"""
class Entity:
    """Doc"""
    __counter = 0  # atributo de classe para contar instâncias

    def __init__(self):
        self.id = Entity.__counter  # atribui o valor atual ao id da instância
        Entity.__counter += 1       # incrementa o contador para o próximo objeto


one = Entity()
two = Entity()
print(one.id)  # Saída: 0
print(two.id)  # Saída: 1
