def hello():
    print('Hello world')

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
        elif isinstance(other, (int,float)):
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

    #Магические методы сравнения
    def __gt__(self, other):
        if self.age > other.age:
            #return True
            return f'Возраст первого объекта больше чем возраст второго объекта'
        else:
            #return False
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
            return self.age/other.age
        return self.age/other

    def __rtruediv__(self, other):
        return self.age/other


def main():
    hello()

    p1 = Person('Samat', 28)
    p2 = Person('Adilet', 21)
    p3 = Person('Timur', 28)

    p1.display()
    #p1.addAge(5)
    p1.display()

    # n1 = 45
    # print(n1 + 10)

    #print(p1 + 10)
    # print(p2 + 20)
    # print(p3 + 30)

    # print(p1 - 2)
    # print(p2 - 10)

    #print(p3 * 2)

    #print(p3/4)
    #print(p1.age + p2.age)

    #resultAgeTwoPerson = p1 + p2
    #print(resultAgeTwoPerson)

    # resultAge2 = p1 + 10
    # print(resultAge2)

    #resultAge3 = 10 + p1

    # p1 += 2
    # p1 +=10
    # print(p1)

    # resultAgeThreePerson = (p1 + p2) + p3
    # print(resultAgeThreePerson)

    print(p1 > p2)
    print(p1 < p2)

    print(p1 >= p3)
    print(p1 <= p3)


    print(p1 == p2)


    print(p1)
    print(p2)
    print(p3)

    print(len(p1))
    print(len(p2))

    resultAge3 = 10+p1
    print(resultAge3)

    print(p1/4)
    print(4/p1)

    #print(p1.contains('a'))






if __name__=='__main__':
    main()
