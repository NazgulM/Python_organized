from abc import ABC, abstractmethod

"""
1. Создайте абстрактный класс Bank с абстрактным методом getBalance. 
100, 150 и 200 долларов ложатся в банках A, B и C соответственно. «BankA», 
«BankB» и «BankC» являются подклассами класса «Bank», каждый из которых имеет 
метод с именем «getBalance». 
Вызовите этот метод, создав объект каждого из трех классов.
"""


class Bank(ABC):
    def __init__(self, name, amount):
        self.user_name = name
        self.amount = amount

    @abstractmethod
    def getBalance(self):
        pass


class BankA(Bank):
    def __init__(self, name, amount, bankName):
        super().__init__(name, amount)
        self.bankName = bankName

    def getBalance(self):
        print(f'{self.user_name} has {self.amount} in {self.bankName}')


class BankB(Bank):
    def __init__(self, name, amount, bankName):
        super().__init__(name, amount)
        self.bankName = bankName

    def getBalance(self):
        print(f'{self.user_name} has {self.amount} in {self.bankName}')


class BankC(Bank):
    def __init__(self, name, amount, bankName):
        super().__init__(name, amount)
        self.bankName = bankName

    def getBalance(self):
        print(f'{self.user_name} has {self.amount} in {self.bankName}')


"""
2. Есть некий Абстрактный класс Car у которого есть приватные поля:
• model;
• color;
• maxSpeed;
и также есть абстрактный методы brake(), gas(), которых требуется 
переопределить в классах наследниках.
Реализуйте и переопределите вышеописанные методы в классах наследниках 
Sedan, SportCar, FamilyCar.
"""


class Car(ABC):
    def __init__(self, model, color, maxSpeed):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def gas(self):
        pass


class Sedan(Car):
    def __init__(self, model, color, maxSpeed, brake, fuel):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed
        self.__brake = brake
        self.__fuel = fuel

    def brake(self):
        print(f'Model of Sedan car: {self.__model}'
              f'\nColor of the car: {self.__color}'
              f'\nMaxSpeed: {self.__maxSpeed}'
              f'\nType of brake: {self.__brake}')

    def gas(self):
        print(f'Type of fuel for {self.__model}: {self.__fuel}')


class SportCar(Car):
    def __init__(self, model, color, maxSpeed, brake, fuel):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed
        self.__brake = brake
        self.__fuel = fuel

    def brake(self):
        print(f'Model of SportCar: {self.__model}'
              f'\nColor of the car: {self.__color}'
              f'\nMaxSpeed: {self.__maxSpeed}'
              f'\nType of brake: {self.__brake}')

    def gas(self):
        print(f'Type of fuel for {self.__model}:  {self.__fuel}')


class FamilyCar(Car):
    def __init__(self, model, color, maxSpeed, brake, fuel):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed
        self.__brake = brake
        self.__fuel = fuel

    def brake(self):
        print(f'Model of FamilyCar: {self.__model}'
              f'\nColor of the car: {self.__color}'
              f'\nMaxSpeed: {self.__maxSpeed}'
              f'\nType of brake: {self.__brake}')

    def gas(self):
        print(f'Type of fuel for {self.__model}: {self.__fuel}')


def main():
    firstClient = BankA('Will Smith', 100, 'KBC Bank')
    firstClient.getBalance()
    print('******************************************')

    secondClient = BankB('Christina Agillera', 150, 'Bank of America')
    secondClient.getBalance()
    print('******************************************')

    thirdClient = BankC('Beyonce', 200, 'ING Bank')
    thirdClient.getBalance()
    print('******************************************')

    sedan = Sedan('Ford Focus', 'red', '186km/h', 'Motor craft Brake Pads', '87 octane-rated fuel.')
    sedan.brake()
    sedan.gas()
    print('*****************************************')

    sportCar = SportCar('Mazda MX-5', 'yellow', '233km/h', 'Disc brakes', '91 to 95 RON')
    sportCar.brake()
    sportCar.gas()
    print('*****************************************')

    familyCar = FamilyCar('Toyota Ipsum', 'white', '224km/h', 'Akebono brake', 'Petrol (Gasoline) A-95')
    familyCar.brake()
    familyCar.gas()


if __name__ == '__main__':
    main()
