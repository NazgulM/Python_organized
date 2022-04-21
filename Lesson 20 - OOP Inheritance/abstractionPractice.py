from abc import ABC, abstractmethod

"""
Практика - Абстракция:
————————————-
Есть абстрактный класс Person, в нем содержится абстрактный метод
calculateMyExpenses(), whereToEat(), earnMoney()
В классах наследниках Student, BankWorker, Doctor необходимо переопределить
вышеописанные методы для каждого класса по своему.
"""


class Person(ABC):
    def __init__(self, name, age, expenses):
        self.name = name
        self.age = age
        self.expenses = expenses

    @abstractmethod
    def calculateMyExpenses(self):
        pass

    @abstractmethod
    def whereToEat(self):
        pass

    @abstractmethod
    def earnMoney(self):
        pass


class Student(Person):
    def __init__(self, name, age, scholarship, expenses, place='restaurant'):
        super().__init__(name, age, expenses)
        self.placeToWork = None
        self.scholarship = scholarship
        self.placeToEat = place

    def calculateMyExpenses(self):
        endMonth = self.scholarship - self.expenses
        return endMonth

    def whereToEat(self):
        nameFood = input('Please enter the name of food: ')
        if nameFood == 'spaghetti':
            self.placeToEat = 'at relatives home'
        else:
            pass

        print(f'The place to eat of student: {self.placeToEat}')

    def earnMoney(self):
        if self.expenses >= 4500:
            self.placeToWork = 'cafe'
        else:
            pass

        print(f'The place to work of student: {self.placeToWork}')


class BankWorker(Person):
    def __init__(self, name, age, expenses, salary, place='cafe of the Bank'):
        super().__init__(name, age, expenses)
        self.methodEarnMoney = None
        self.salary = salary
        self.placeToEat = place

    def calculateMyExpenses(self):
        endMonth = self.salary - self.expenses
        return endMonth

    def whereToEat(self):
        nameFood = input('Please enter the name of food: ')
        if nameFood == 'shorpo':
            self.placeToEat = 'at home'
        else:
            pass

        print(f'The place to eat of BankWorker: {self.placeToEat}')

    def earnMoney(self):
        if self.expenses >= 15000:
            self.methodEarnMoney = 'work at night and holidays'
        else:
            pass

        print(f'The other method of earn money of BankWorker: {self.methodEarnMoney}')


class Doctor(Person):
    def __init__(self, name, age, expenses, salary, place='cafe of the Hospital'):
        super().__init__(name, age, expenses)
        self.methodEarnMoney = None
        self.salary = salary
        self.placeToEat = place

    def calculateMyExpenses(self):
        endMonth = self.salary - self.expenses
        return endMonth

    def whereToEat(self):
        nameFood = input('Please enter the name of food: ')
        if nameFood == 'kotlety':
            self.placeToEat = 'at home'
        else:
            pass

        print(f'The place to eat of Doctor: {self.placeToEat}')

    def earnMoney(self):
        if self.expenses >= 12000:
            self.methodEarnMoney = 'work at private hospitals'
        else:
            pass

        print(f'The other method of earn money of Doctor: {self.methodEarnMoney}')


def main():
    student = Student('Bolot', 21, 5000, 4850)
    result = student.calculateMyExpenses()
    print(f'Current balance of student is: {result}')
    student.whereToEat()
    student.earnMoney()
    print('*******************************')

    bankWorker = BankWorker('Klara', 45, 22000, 25000)
    remain = bankWorker.calculateMyExpenses()
    print(f'Current balance of BankWorker is: {remain}')
    bankWorker.whereToEat()
    bankWorker.earnMoney()
    print('**********************************')

    doctor = Doctor('Samat', 42, 15000, 20000)
    sum = doctor.calculateMyExpenses()
    print(f'Current balance of Doctor is: {sum}')
    doctor.whereToEat()
    doctor.earnMoney()


if __name__ == '__main__':
    main()
