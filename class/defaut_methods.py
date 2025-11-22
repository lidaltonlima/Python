"""Doc"""
class Person:
    """Docstring for Person"""
    def __init__(self, name: str, age: int, city: str, state: str, profession: str):
        self.name = name
        self.age = age
        self.city = city
        self.state = state
        self.profession = profession

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r})'

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Person) and
            self.name == other.name and
            self.age == other.age and
            self.city == other.city and
            self.state == other.state and
            self.profession == other.profession
        )


if __name__ == "__main__":
    person1 = Person("João", 29, "Salvador", "Bahia", "Engenheiro")
    person2 = Person("João", 29, "Salvador", "Bahia", "Engenheiro")
    # print(person1)
    print(person1 == person2)  # True
