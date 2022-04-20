class Animal:
    def eat(self):
        print('I can eat')


class Dog(Animal):
    def bark(self):
        print('I can bark')


class Cat(Animal):
    def get_grumpy(self):
        print('I am getting grumpy')


dog1 = Dog()
dog1.bark()
dog1.eat()

cat1 = Cat()
cat1.eat()
cat1.get_grumpy()

"""
1) Создать классы Vip_Account, PremiumAccount, кот-ые наследуются от класса BankAccount
2) Добавить к аккаунту Vip_Account - метод vipserving(): "Обслуживание в 1-ую очередь и отдельно"
3) Добавить к аккаунту Premium_Account - метод privalages(): "Скидка по карте 25%, резервирование 
премиальных услуг скидка в 10%"

"""


class BankAccount:
    def __init__(self, id):
        self.id = id

    def displayInfo(self):
        print('You have account : ', self.id)


class VipAccount(BankAccount):

    def vipService(self):
        print('Обслуживание в 1-ую очередь и отдельно')


class PremiumAccount(BankAccount):

    def privileges(self):
        print("Скидка по карте 25%, резервирование премиальных услуг скидка в 10%")


client = VipAccount('12300000784596')
client.displayInfo()
client.vipService()

client2 = PremiumAccount('186000089563214')
client2.displayInfo()
client2.privileges()

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        value = 0
        for side in self.sides:
            value += side
        return value


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        value = 0
        for side in self.sides:
            value += side
        return value


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        # Polygon.display_info(self)
        super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

t1.display_info()