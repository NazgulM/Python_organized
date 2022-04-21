"""
1. Создать класс родитель Teacher от, которого наследуются другие классы наследники:
PhysichTeacher, ChemistryTeacher,MathTeacher
Базовый класс принимает параметры как:
• ФИО учителя
• Стаж учителя
• Имя предмета, который ведет учитель
• Количество студентов
Также есть базовый метод displayInfo(), который отображает все эти информации.

В классах наследниках (GeographyTeacher, DrawingTeacher,MathTeacher) помимо принятия
базовых аттрибутов, примите следующие атрибуты:
• Для DrawingTeacher - фигуру (это может быть круг, квадрат, треугольник)
• Для MathTeacher - три числа
• Для GeographyTeacher - название страны
"""


class Teacher:
    def __init__(self, name, experience, subject, numberStud):
        self.fullName = name
        self.workExp = experience
        self.subjectName = subject
        self.numStudents = numberStud

    def displayInfo(self):
        print(f'The name of teacher: {self.fullName}'
              f'\nTotal work experience is: {self.workExp}'
              f'\nSubject name is: {self.subjectName}'
              f'\nNumber of students: {self.numStudents}')


class GeographyTeacher(Teacher):
    def __init__(self, name, experience, subject, numberStud, countryName):
        Teacher.__init__(self, name, experience, subject, numberStud)
        self.nameCountry = countryName

    def findCapitalCity(self):
        if self.nameCountry == 'France':
            print('The capital of France is Paris')
        elif self.nameCountry == 'Kyrgyzstan':
            print('The capital of Kyrgyzstan is Bishkek')
        else:
            print('The capital of Belgium is Brussels')

    def displayInfo(self):
        print(f'The name of teacher: {self.fullName}'
              f'\nTotal work experience is: {self.workExp}'
              f'\nSubject name is: {self.subjectName}'
              f'\nNumber of students: {self.numStudents}')


class DrawingTeacher(Teacher):
    def __init__(self, name, experience, subject, numberStud, figureName):
        Teacher.__init__(self, name, experience, subject, numberStud)
        self.nameFigure = figureName

    def findSimilarObject(self):
        if self.nameFigure == 'circle':
            print('CD, wheels are circular')
        elif self.nameFigure == 'square':
            print('Chess board is square shaped')
        elif self.nameFigure == 'triangle':
            print('A slice of pizza has a triangle shape')

    def displayInfo(self):
        print(f'The name of teacher: {self.fullName}'
              f'\nTotal work experience is: {self.workExp}'
              f'\nSubject name is: {self.subjectName}'
              f'\nNumber of students: {self.numStudents}')


class MathTeacher(Teacher):
    def __init__(self, name, experience, subject, numberStud):
        Teacher.__init__(self, name, experience, subject, numberStud)

    def findAverage(self, number1, number2, number3):
        avg = (number1 + number2 + number3) / 3
        print('The average number is: ', avg)

    def displayInfo(self):
        print(f'The name of teacher: {self.fullName}'
              f'\nTotal work experience is: {self.workExp}'
              f'\nSubject name is: {self.subjectName}'
              f'\nNumber of students: {self.numStudents}')


class MathGeographyTeacher(MathTeacher, GeographyTeacher):
    def __init__(self, name, experience, subject, numberStud):
        Teacher.__init__(self, name, experience, subject, numberStud)

    def introducing(self):
        print(f'My name is {self.fullName} and I teach Mathematics and Geography')

    def displayInfo(self):
        print(f'The name of teacher: {self.fullName}'
              f'\nTotal work experience is: {self.workExp}'
              f'\nSubject name is: {self.subjectName}'
              f'\nNumber of students: {self.numStudents}')


def main():
    geoTeacher = GeographyTeacher('Aliya Sabirova', 15, 'geography', 35, 'France')
    geoTeacher.findCapitalCity()
    geoTeacher.displayInfo()
    print('*****************************')

    drawTeacher = DrawingTeacher('Bekbol Artykov', 5, 'drawing', 25, 'circle')
    drawTeacher.findSimilarObject()
    drawTeacher.displayInfo()
    print('******************************')

    mathTeacher = MathTeacher('Akyl Kanatova', 35, 'mathematics', 80)
    mathTeacher.findAverage(45, 60, 20)
    mathTeacher.displayInfo()
    print('******************************')

    mathgeoTeacher = MathGeographyTeacher('Dinara Oshurahunova', 25, 'math and geography', 45)
    mathgeoTeacher.introducing()
    print('******************************')
    mathgeoTeacher.displayInfo()


if __name__ == '__main__':
    main()
