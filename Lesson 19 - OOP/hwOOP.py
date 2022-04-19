"""
1. Создать класс BankAccount с параметрами:
• Id - String-овый параметр
• balance - Int значение

Дополнительно реализовать следующие методы:
• Deposit - Через этот метод человек восполняет баланс и баланс увеличивается.
После депозита средств на счет должно выводится следующее сообщение:
«Вы пополнили счет 123231434000034 на сумму: 25000 сом
Баланс после пополнения счета: 60000 сом»
• Withdraw - Снятие денег, через этот метод происходит снятие денег и
после снятия происходит снижение текущего баланса, в случае если денег на балансе нету то,
выводится сообщение:
«У вас закончились деньги на балансе» Иначе
«Вы сняли со счета 123231434000034: 15000 сом Баланс после пополнения счета: 35000 сом
Текущий баланс:35000 сом»
Пример результата выполнения программы:
Текущий баланс: 50000 сом
Вы сняли со счета 123231434000034: 15000 сом Баланс после пополнения счета: 35000 сом
Текущий баланс:35000 сом
Вы пополнили счет 123231434000034 на сумму: 25000 сом Баланс после пополнения счета:
60000 сом
"""


class BankAccount:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def deposit(self):
        print(f'Current balance: {self.balance}')
        amount = float(input('\nPlease enter the amount to be Deposited: '))
        self.balance += amount
        print(f'You filled {self.id} account by the amount:  {amount}'
              f'\nYour balance after deposit: {self.balance}')

    def withdraw(self):
        print(f'\nCurrent balance: {self.balance}')
        amount = float(input('\nPlease enter the amount to de Withdraw: '))
        self.balance -= amount
        if self.balance <= 0:
            print('Insufficient balance')
        else:
            print(f'You withdrew from account {self.id} : {amount}'
                  f'\nYour balance after withdraw: {self.balance}')


def main():
    s = BankAccount('1232314340000034', 35000)
    s.deposit()
    s.withdraw()


if __name__ == '__main__':
    main()
