"""
Напишите программу с классом Student, в котором есть три атрибута:
name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge,
setGroupNumber.
Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента,
метод setGroupNumber нужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы.
"""


class Student:
    def __init__(self, name, groupNumber='10A', age=18):
        self.studentName = name
        self.groupNumber = groupNumber
        self.studentAge = age

    def getName(self):
        print(f'The name of student: {self.studentName}')

    def getAge(self):
        print(f'The age of student: {self.studentAge}')

    def getGroupNumber(self):
        print(f'The number of student group: {self.groupNumber}')

    def setNameAge(self, name, age):
        self.studentName = 'Boris'
        self.studentAge = 21
        print(f'We added correct name of student: {self.studentName}'
              f' and age: {self.studentAge}')

    def setGroupNumber(self, groupNumber):
        self.groupNumber = '8B'
        print(f'The student correct group number is: {self.groupNumber}')


"""
2. Напишите программу с классом Math. 
Создайте два атрибута — a и b. Напишите методы addition — сложение, 
multiplication — умножение, division — деление, subtraction — вычитание. 
При передаче в методы параметров a и b с ними нужно производить соответствующие 
действия и печатать ответ.
"""


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        add = self.a + self.b
        print(f'The result of addition: {add}')

    def multiplication(self):
        mult = self.a * self.b
        print(f'The result of multiplication: {mult}')

    def division(self):
        div = self.a / self.b
        print(f'The result of division: {div}')

    def subtraction(self):
        sub = self.b - self.a
        print(f'The result of subtraction b-a: {sub}')


"""
3. Напишите программу с классом Car. Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
Третий — присвоение автомобилю года выпуска. 
Четвертый метод — присвоение автомобилю типа. 
Пятый — присвоение автомобилю цвета.
"""


class Car:
    def __init__(self, color, type, year):
        self.colorCar = color
        self.typeCar = type
        self.yearCar = year

    def startCar(self):
        print(f'The {self.typeCar} with {self.colorCar} color and from {self.yearCar} '
              f'year is started a car')

    def turnOffCar(self):
        print(f'The {self.typeCar} with {self.colorCar} color and from {self.yearCar} '
              f'year is turned off')

    def yearOfCar(self):
        print(f'The car manufacturing year is {self.yearCar}')

    def typeOfCar(self):
        print(f'The car type is {self.typeCar}')

    def colorOfCar(self):
        print(f'The color of the car is {self.colorCar}')


"""
4. Создайте класс Soda (для определения типа газированной воды), принимающий 
1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), 
выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, 
а иначе отобразится следующая фраза: «Обычная газировка».
"""


class Soda:
    def __init__(self, topping=None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping == 'raspberry':
            print(f'Soda and {self.topping}')
        else:
            print('Normal soda')


"""
Для этого он решил создать класс TriangleChecker, принимающий только 
положительные числа.
С помощью метода is_triangle() возвращаются следующие значения 
(в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!; – Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""


class TriangleChecker():
    def __init__(self, num=[]):
        self.num = num

    def is_triangle(self):
        for n in self.num:
            if n >= 0:
                print('Woohoo, we can create a triangle')
                break
            elif n < 0:
                print('Nothing will work with negative numbers!')
                break
        # elif type(self.num) == str:
        #     print('You only need to enter numbers!')
        # else:
        #     print('Unfortunately, but you cannot make a triangle out of this')


def main():
    student1 = Student('Chyngyz')
    student1.getName()
    student1.getAge()
    student1.getGroupNumber()
    student1.setNameAge(name='Boris', age=21)
    print('************************')

    student2 = Student('Nazgul')
    student2.getName()
    student2.getAge()
    student2.getGroupNumber()
    print('***************************')

    student3 = Student('Nursultan')
    student3.getName()
    student3.getAge()
    student3.getGroupNumber()
    print('***************************')

    student4 = Student('Bakai')
    student4.getName()
    student4.getAge()
    student4.getGroupNumber()
    print('***************************')

    student5 = Student('Aruuke')
    student5.getName()
    student5.getAge()
    student5.getGroupNumber()
    student5.setGroupNumber(groupNumber='8B')
    print('*****************************')

    add = Math(21, 15)
    add.addition()

    mult = Math(12, 10)
    mult.multiplication()

    div = Math(456, 12)
    div.division()

    sub = Math(89, 789)
    sub.subtraction()
    print('**********************************')

    start = Car('white', 'Crossover', 2020)
    start.startCar()

    off = Car('red', 'Sedan', 2019)
    off.turnOffCar()

    y = Car('purple', 'Mercedes', 2021)
    y.yearOfCar()

    type1 = Car('silver', 'Sports Car', 2022)
    type1.typeOfCar()

    color = Car('golden', 'Sedan', 2020)
    color.colorOfCar()
    print('**********************************')

    drink1 = Soda()
    drink2 = Soda('raspberry')
    drink3 = Soda(5)

    drink1.show_my_drink()
    drink2.show_my_drink()
    drink3.show_my_drink()
    print('**********************************')

    triangle1 = TriangleChecker([2,3,4])
    triangle1.is_triangle()
    # triangle2 = TriangleChecker([77, 3, 4])
    # triangle2.is_triangle()
    # triangle3 = TriangleChecker([77, 3, 'Side 3'])
    # triangle3.is_triangle()
    triangle4 = TriangleChecker([77, -3, 4])
    triangle4.is_triangle()


if __name__ == '__main__':
    main()
