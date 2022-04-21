from abc import ABC, abstractmethod
from math import pi,pow

class Figure(ABC):
    def __init__(self, nameFigure, color):
        self.name = nameFigure
        self.colorFigure = color

    @abstractmethod
    def find_square(self):
        pass


class Square(Figure):
    def __init__(self, nameFigure, color, height, width):
        Figure.__init__(self,nameFigure, color)
        self.heighSquare = height
        self.widthSquare = width

    def find_square(self):
        square = self.heighSquare * self.widthSquare
        return square

class Circle(Figure):
    def __init__(self, nameFigure, color, radius):
        super().__init__(nameFigure,color)
        self.radius = radius

    def find_square(self):
        result = pi * pow(self.radius, 2)

        return result

class Triangle(Figure):
    def __init__(self, nameFigure, color, a, h):
        super().__init__(nameFigure,color)
        self.heigh = h
        self.a = a

    def find_square(self):
        result = 0.5 * self.a * self.heigh
        return result

def main():
    #Квадрат
    fig1 = Square('Квадрат','Черный квадрат', 4, 5)
    squareofFig1 = fig1.find_square()

    #Круг
    fig2 = Circle('Круг', 'Красный', 12)
    squareofFig2 = fig2.find_square()
    #452.3893421169302

    #Треугольник
    fig3 = Triangle('Треугольник', 'Синий', 5, 7)
    squareofFig3 = fig3.find_square()

    print(f'Square of Fig1: {squareofFig1}')
    print(f'Square of Fig2: {squareofFig2:.2f}')
    print(f'Square of Fig3: {squareofFig3:.2f}')

if __name__=='__main__':
    main()
