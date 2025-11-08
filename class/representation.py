"""Docstring for the module"""
class People:
    """Docstring for People"""
    def __init__(self):
        """Docstring for __init__"""
        self.tools: list[Tool] = []

class Tool:
    """Docstring for Tool"""
    def __init__(self, name: str):
        """Docstring for __init__"""
        self.name = name

    def __repr__(self):
        return f'Tool(name="{self.name}")'

    def __str__(self):
        return self.name


# Criando objetos
people = People()
hammer = Tool("Hammer")
people.tools.append(hammer)

# Exibindo a lista de ferramentas
print(people.tools)       # [Tool(name='Hammer')]
print(people.tools[0])    # Hammer
