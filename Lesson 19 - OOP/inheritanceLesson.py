class Animal:
    def __init__(self, typeanimal, typefood, livingarea):
        self.animalType = typeanimal
        self.foodType = typefood
        self.areliving = livingarea

    def sleep(self):
        print(f'{self.animalType} спит в {self.areliving}')

    def eat(self):
        print(f'{self.animalType} кушает свою еду: {self.foodType}')

    def display(self):
        print(f'Еда: {self.foodType}'
              f'\nСреда обитания: {self.areliving}'
              f'\nТип животного: {self.animalType}')

class Mind:
    def __init__(self, typeWord):
        self.wordType = typeWord

    def canSpeak(self):
        print(f'Умеет говорить и читать'
              f'  Говорит слова: {self.wordType}')

class Tiger(Animal):
    def __init__(self, typeanimal, typefood, livingarea, lengh_tail):
        Animal.__init__(self,typeanimal, typefood, livingarea)
        self.tail_l = lengh_tail

    def display(self):
        print(f'Еда: {self.foodType}'
              f'\nСреда обитания: {self.areliving}'
              f'\nТип животного: {self.animalType}'
              f'\nДлина хвоста тигра: {self.tail_l}')

    def canHunting(self):
        print('Тигр умеет охотиться и самое жестокое животное и он хищник')

class Monkey(Animal):
    def __init__(self, typeanimal, typefood, livingarea, len_hand, quant_teeth):
        Animal.__init__(self,typeanimal, typefood, livingarea)
        self.len_hand = len_hand
        self.teethQuant = quant_teeth

    def canClimbTree(self):
        print('Обезьяна умеет лазить по деревьям и он травоядное животное')

    def display(self):
        print(f'Еда: {self.foodType}'
              f'\nСреда обитания: {self.areliving}'
              f'\nТип животного: {self.animalType}'
              f'\nДлина руки: {self.len_hand}'
              f'\nКоличество зубов: {self.teethQuant}')

#Множественное наследование
class Parrot(Animal, Mind):
    def __init__(self,typeanimal, typefood, livingarea, typeWord, color):
        Animal.__init__(self, typeanimal, typefood, livingarea)
        Mind.__init__(self, typeWord)
        self.coloranimal = color

    def canFly(self):
        print(f'Это попугай и он умеет летать!'
              f'\n и его цвет {self.coloranimal}')

def main():
    tiger1 = Tiger('Бельгийский тигр','мясо', 'савана', 12)
    monkey1 = Monkey('Шимпанзе', 'банан', 'джунгли', 32, 28)

    tiger1.sleep()
    monkey1.sleep()

    tiger1.eat()
    monkey1.eat()

    tiger1.canHunting()
    monkey1.canClimbTree()
    print(tiger1.tail_l)
    #tiger1.canClimbTree()

    parrot1 = Parrot('Попугай АРА', 'зерно', 'лес', 'Вовка дурак', 'Белый')
    parrot1.canFly()
    parrot1.sleep()
    parrot1.canSpeak()
    parrot1.display()

    print('*'*10)
    monkey1.display()
    print('*' * 10)
    tiger1.display()
    print('*' * 10)
    parrot1.display()

if __name__=='__main__':
    main()

    """
    1) Создать классы Vip_Account, PremiumAccount, кот-ые наследуются от класса Account
    2) Добавить к аккаунту Vip_Account - метод vipserving(): "Обслуживание в 1-ую очередь и отдельно"
    3) Добавить к аккаунту Premium_Account - метод privalages(): "Скидка по карте 25%, резервирование 
    премиальных услуг скидка в 10%"
    """