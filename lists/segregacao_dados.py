"""Doc"""
values: list[str | float] = [
    'João',
    29,
    'Salvador',
    'Bahia',
    'Engenheiro',
]

name, age, *_, profession = values

print(f'O {name} tem {age} anos e trabalha como {profession}.')
