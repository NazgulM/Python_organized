"""
1) Создать класс Автомобиль - Car. С приватными полями год выпуска, бренд, модель, тип топлива, состояние
• Создать конструктор для принятия значений
• Создать get и set методы для доступа к этим значениям
• Если год выпуска автомобиля старее 2000 года, установить значение
состояние как ‘’old’’ иначе ‘’new’’
• Создать метод для отображения
• В главном методе создать 3 объекта с разными значениями и вызвать
метод для отображения всех объектов
"""


class Car:
    def __init__(self, modelName, year, nameBrand, typeFuel):
        self.nameModel = modelName
        self.yearCreate = year
        self.brandName = nameBrand
        self.fuelType = typeFuel

    def displayInfo(self):
        print(f'Information. \n'
              f'Model of the car: {self.nameModel}'
              f'\nYear of manufacture: {self.yearCreate}'
              f'\nBrand: {self.brandName}'
              f'\nType of fuel: {self.fuelType}')


def main():
    car1 = Car('Model S', '2020', 'Tesla', 'eco')
    car1.displayInfo()


if __name__ == '__main__':
    main()
