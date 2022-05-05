class Car:
    def __init__(self, year, modelName, engineCapacity):
        self.year = year
        self.engineCapacity = engineCapacity
        self.modelName = modelName

    def display(self):
        print(f'Car: {self.modelName}'
              f'\nYear of release: {self.year}'
              f'\nEngine: {self.engineCapacity}')

    def __str__(self):
        return f'Car: {self.modelName}', f'\nYear of release: {self.year}', f'\nEngine: {self.engineCapacity}'

    def __add__(self, other):
        if isinstance(other, Car):
            return self.engineCapacity + other.engineCapacity
        return self.engineCapacity + other

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.engineCapacity - other.engineCapacity
        return self.engineCapacity - other


class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __lt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width < other.height * other.width
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Area):
            return self.height * self.width > other.height * other.width
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Area):
            return self.height * self.width == other.height * other.width
        else:
            return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


def main():
    car1 = Car(2020, 'BMW X5', 4.8)
    car1.display()
    print('******************')

    car2 = Car(2019, 'Range Rover', 4.5)
    car2.display()
    print('******************')

    print(car1 + 1)
    print(car1 + car2)

    print(car1 - car2)

    a1 = Area(5, 8)
    a2 = Area(4, 10)
    a3 = Area(8, 9)
    print(f'A1 less than A2 :  {a1 < a2}')
    print(f'A1 less than A3: {a1 < a3}')
    print(f'A1 greater than A2: {a1 > a2}')
    print(f'A1 greater than A3: {a1 > a3}')
    print(f'A1 is equal to A2: {a1 == a2}')
    print(f'A1 is equal to A3: {a1 == a3}')
    print(f'A1 is equal or less than A2: {a1 <= a2}')
    print(f'A1 is equal or less than A3: {a1 <= a3}')
    print(f'A1 is equal or greater than A2: {a1 >= a2}')
    print(f'A1 is equal or greater than A3: {a1 >= a3}')


if __name__ == '__main__':
    main()
