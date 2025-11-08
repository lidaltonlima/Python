"""
Associação: 
    - Uma classe usa outra classe
    - Sem dependência
    - As outras classes podem existir independentemente
Agregação:
    - Uma classe contém outra classe
    - Dependência fraca
    - As outras classes podem existir independentemente
Composição:
    - Uma classe é composta por outras classes
    - Dependência forte
    - É dona das outras classes
Herança:
    - Uma classe herda de outra classe
    - Reutilização de código
"""


class MyClass:
    """Docstring for MyClass"""
    def __init__(self, name: str = "Default Name"):
        """Docstring for __init__"""
        self.name = name # If no underscore, setter is called
        self.__private: dict[str, str] = {}

    def default_method(self):
        """Docstring for default_method"""

    @staticmethod
    def static_method():
        """Docstring for static_method"""

    @classmethod
    def class_method(cls):
        """Docstring for class_method"""

    @property
    def name(self) -> str:
        """Docstring for name property"""
        print("Accessing the name property")
        return self._name

    @name.setter
    def name(self, value: str):
        """Docstring for name setter"""
        print("Setting the name property")
        self._name = value.upper()

    @property
    def private(self) -> dict[str, str]:
        """Docstring for private property"""
        return self.__private


one = MyClass()
print(one.private)  # Accessing the private attribute using the public property
