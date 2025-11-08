"""Docstring for the module"""
from dataclasses import dataclass, field

@dataclass
class Tool:
    """Docstring for Tool"""
    name: str
    state: str = "new"

@dataclass
class People:
    """Docstring for People"""
    tools: list[Tool] = field(default_factory=list[Tool])

# Criando objetos
people = People()
hammer = Tool("Hammer")
people.tools.append(hammer)

# Exibindo a lista de ferramentas
print(people.tools)       # [Tool(name='Hammer')]
print(people.tools[0])    # Tool(name='Hammer')




people = People()
hammer = Tool("Hammer")
people.tools.append(hammer)
print(people.tools)
print(hammer)
