from datetime import *

class AirCondtioner:
    def __init__(self, modelName):
        self.nameModel = modelName
        self.temper = None
        self.timeNow = datetime.now().time()

    def displayInfo(self):
        print(f'Информация. \n'
              f'Модель {self.nameModel}'
              f'\nТекущая температура: {self.temper}'
              f'\nВремя: {self.timeNow}'
              f'\n****************')

    def turnedOff(self):
        print(f'Кондиционер ВЫключается...'
              f'\n***********************')
        self.temper = None
        self.timeNow = None

    def turnedOn(self):
        print(f'Кондиционер ВКлючается...'
              f'\n***********************')
        self.temper = 20
        self.timeNow = datetime.now().time()

    def changeTemp(self, temperature):
        self.temper = temperature
        print(f'Новая температура: {self.temper}'
              f'\n***********************')

    def makeHot(self):
        self.temper = 35
        print(f'Новая температура: {self.temper}'
              f'\n Установлен режим Печки'
              f'\n***********************')


class Person:
    def __init__(self, name):
        self.__namePerson = name
        self.__agePerson = 20
        #__namePerson

    def set_age(self, newage):
        if 1< newage < 100:
            self.__agePerson = newage
        else:
            print('Недопустимый возраст')

    def getAge(self):
        return self.__agePerson

    @property
    def name(self):
        return self.__namePerson

    @name.setter
    def name(self, newname):
        self.__namePerson = newname.capitalize()

    def displayInfo(self):
        print("Информация о данном человеке:"
              "\nИмя: {0}"
              "\nВозраст: {1}".format(self.__namePerson, self.__agePerson))

def main():
    airCond_1 = AirCondtioner('Samsung tx54')
    airCond_2 = AirCondtioner('LG re45')
    airCond_3 = AirCondtioner('Beko 342')

    airCond_1.displayInfo()
    airCond_1.turnedOn()

    airCond_1.displayInfo()
    airCond_1.changeTemp(15)

    airCond_1.displayInfo()

    airCond_2.turnedOn()
    airCond_2.makeHot()
    airCond_2.displayInfo()

    airCond_3.turnedOn()
    airCond_3.displayInfo()

    airCond_1.turnedOff()
    airCond_1.displayInfo()

    print(airCond_2.temper)
    airCond_2.temper = 23
    print(airCond_2.temper)

    person1 = Person('Adilet')
    person2 = Person('Samat')

    #person1.__namePerson = 'Askar'
    #print(person1.__namePerson)

    # print(person1.getName())
    # person1.setName('askar')
    #
    # print(person1.getName())
    # print(person1.getAge())

    person1.set_age(-45)
    print(person1.getAge())

    person1.set_age(15)
    print(person1.getAge())

    person1.displayInfo()

    print(person1.name)
    person1.name = 'samat'

    print(person1.name)


if __name__=='__main__':
    main()

"""

"""






