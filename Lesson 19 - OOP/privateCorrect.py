"""
Task 1
"""


class BankAccount:
    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance

    def deposit(self):
        print(f'Current balance: {self.__balance}')
        amount = float(input('\nPlease enter the amount to be Deposited: '))

        if amount <= 0:
            print(f'Сумма добавления к балансу {amount} невозможна')
        else:
            self.__balance += amount

        print(f'You filled {self.__id} account by the amount:  {amount}'
              f'\nYour balance after deposit: {self.__balance}')

    def withdraw(self):
        print(f'\nCurrent balance: {self.__balance}')
        amount = float(input('\nPlease enter the amount to de Withdraw: '))

        if self.__balance <= 0 or self.__balance < amount:
            difference = amount - self.__balance

            print(f'Недостаточно баланса, вы ввели сумму, которая больше '
                  f'актуального баланса на {difference}!'
                  f'\nПожалуйста введите сумму, которая '
                  f'меньше чем ваш баланс: {self.__balance}')
        else:
            self.__balance -= amount
            print(f'You withdrew from account {self.__id} : {amount}'
                  f'\nYour balance after withdraw: {self.__balance}')

    def display(self):
        print(f'Your account: {self.__id}'
              f'\nBalance: {self.__balance}')


"""
Task 2
"""


class Person:
    def __init__(self, name, address, age=18):
        self.__namePerson = name
        self.__agePerson = age
        self.__addressPerson = address
        self.__can_vote = None

        if self.__agePerson >= 18:
            self.__can_vote = True
        else:
            self.__can_vote = False

    # getter method
    def get_age(self):
        return self.__agePerson

        # setter method

    def set_age(self, new_age):
        if new_age < 18:
            print(f'Возраст меньше 18!')
        else:
            print(f'Возраст больше 18, может голосовать')

        self.__agePerson = new_age

    def get_vote(self):
        if self.__can_vote == False:
            return 'Молодой для голосования'
        else:
            return 'Может голосовать'

    def get_can_vote(self):
        return self.__can_vote

    def displayPerson(self):
        print(f'Имя: {self.__namePerson}'
              f'\nВозраст: {self.__agePerson}'
              f'\nАдрес: {self.__addressPerson}'
              f'\nДопуск к голосованию: {self.__can_vote}'
              f'\n*********************************')


def main():
    p1 = Person("Адилет", "Мира 7")
    p2 = Person("Сергей", "Токтогула 8", 15)
    p3 = Person("Айсулуу", "Токтогула 77", 23)

    p1.displayPerson()
    p2.displayPerson()
    p3.displayPerson()

    print(p1.get_vote())
    print(p2.get_vote())

    # Task1

    a1 = BankAccount('12220000002333200', 20000)

    a2 = BankAccount('13000000234300045', 50000)


    a1.deposit()
    a1.withdraw()
    # print(a1.balance)

    # print(a2.balance)
    # print(a2.id)


if __name__ == '__main__':
    main()
