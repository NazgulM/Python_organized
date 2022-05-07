from copy import copy


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def display(self):
        print(f'Name:{self.name}'
              f'\nAge: {self.age}')

    def addAge(self, newSum):

        self.age = self.age + newSum

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        elif isinstance(other, (int, float)):
            return other + self.age

        # return other + self.age

    def __iadd__(self, other):
        self.age = self + other
        return self.age

    def __isub__(self, other):
        self.age = self - other
        return self.age

    def __imul__(self, other):
        self.age = self.age * other

        return self.age

    def __sub__(self, other):

        return self.age - other

    def __mul__(self, other):
        return self.age * other

    # Магические методы сравнения
    def __gt__(self, other):
        if self.age > other.age:
            # return True
            return f'Возраст первого объекта больше чем возраст второго объекта'
        else:
            # return False
            return f'Возраст второго объекта больше чем возраст первого объекта'

    def __lt__(self, other):
        if self.age < other.age:
            return True

        else:
            return False

    def __ge__(self, other):
        if self.age >= other.age:
            return f'Первый объект больше либо равно чем второй объект'
        else:
            return f'Первый объект меньше второго'

    def __le__(self, other):
        if self.age <= other.age:
            return f'Первый объект меньше либо равно чем второй объект'
        else:
            return f'Первый объект больше второго'

    def __eq__(self, other):
        if self.age == other.age:
            return f'Они равны'
        else:
            return f'Не равны'

    def __len__(self):
        return len(self.name)

    # def __div__(self, other):
    #     return self.age/other

    # def __contains__(self, item):
    #     if self.name.contains(item):
    #         return True

    def __radd__(self, other):
        return self.age + other

    def __rsub__(self, other):
        return self.age - other

    def __truediv__(self, other):
        if isinstance(other, Person):
            return self.age / other.age
        return self.age / other

    def __rtruediv__(self, other):
        return self.age / other

    # magic method part 2

    def __mod__(self, other):
        if isinstance(other, Person):
            return self.age % other.age
        else:
            return self.age % other

    def __rmod__(self, other):
        if isinstance(other, Person):
            return self.age % other.age
        else:
            return self.age % other

    def __imod__(self, other):
        self.age = self.age % other

        return self.age

    def __call__(self, a, b):
        print(self.age + (a * b))

    def __pow__(self, power, modulo=None):
        return self.age ** power

    def __contains__(self, item):
        if item in self.name:
            return True

        return False

    def __and__(self, other):
        if self.name > other:
            return self.name
        else:
            return other

    def __or__(self, other):
        if self.name < other:
            return self.name
        else:
            return other

    def __getitem__(self, item):
        return self.name[item]

    # def __delete__(self, instance):
    #     print(f'{self.name} deleted from Computer')

    def __del__(self):
        print(f'{self.name} deleted from Computer')

    def __copy__(self):
        print('Processing copy....')
        my_copy = type(self)
        my_copy.__dict__.update(self.__dict__)


def main():
    person1 = Person('Adilet', 25)
    person2 = Person('Aisuluu', 15)

    print(person1 % 5)
    print(person1 % 3)
    print(person1 % person2)
    print(45 % person1)

    person1.age %= 15
    print(person1.age)

    person1(3, 50)
    print(person1)

    print(person1 ** 2)
    print(person2 ** 2)

    print('et' in person1)
    print('lu' in person2)

    print(person1 and person2)
    print(person1 or person2)

    print(type(person1))
    print(person1[::-1])
    print(person2[2:4])

    person4 = person1
    print(person4.name)


if __name__ == '__main__':
    main()
