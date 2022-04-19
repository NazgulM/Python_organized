"""
Создайте класс Person со следующими приватными атрибутами:
• name, age, address, can_vote (Можно будет установить «да», «нет.
По умолчанию для can_vote установлен параметр «Да», а для возраста установлен 18)
• В конструктор нужно передавать все атрибуты, кроме can_vote.
Атрибут can_vote устанавливается в зависимости от возраста человека.
• Создать геттер и геттер для age, can_vote
• В сеттере происходит настройка возраста, затем в зависимости от возраста Can_vote
становится “Да”, если возраст человека выше либо равно 18-ти, иначе атрибут can_vote
принимает в себя «Нет».
• Создайте метод для отображение всех информаций о человеке.
Создайте необходимые экземпляры класса и передайте в конструктор все соответствующие параметры
"""


class Person:
    def __init__(self, name, address, age=18):
        self.__namePerson = name
        self.__agePerson = age
        self.__addressPerson = address
        self.__can_vote = None

        if self.__agePerson >= 18:
            self.__can_vote = 'yes'
        else:
            self.__can_vote = 'no'

    # getter method
    def get_age(self):
        return self.__agePerson

    # setter method
    def set_age(self, newAge):
        if newAge < 18:
            print('Age is less than 18')
            self.__can_vote = 'no'

        else:
            print('Age is up 18, you can vote')
            self.__can_vote = 'yes'
        self.__agePerson = newAge

    def get_vote(self):
        if self.__can_vote == False:
            return 'You are so young to vote'
        else:
            return 'Can Vote'

    # def set_vote(self):
    #     if self.__agePerson > 18:
    #         self.__can_vote = 'yes'
    #     else:
    #         self.__can_vote = 'no'

    def displayPerson(self):
        print(f'Name: {self.__namePerson}'
              f'\nAge: {self.__agePerson}'
              f'\nAddress: {self.__addressPerson}'
              f'\nEligibility to vote: {self.__can_vote}'
              f'\n*************************************')


def main():
    p1 = Person('Adilet', 'Mira 7')
    p2 = Person('Sergey', 'Toktogula 8', 15)
    p3 = Person('Aisuluu', 'Toktogula 77', 23)

    p1.displayPerson()
    p2.displayPerson()
    p3.displayPerson()

    print(p1.get_vote())


if __name__ == '__main__':
    main()
