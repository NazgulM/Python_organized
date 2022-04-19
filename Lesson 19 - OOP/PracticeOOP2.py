class Car:
    def __init__(self, modelName, year, nameBrand, typeFuel):
        self.__nameModel = modelName
        self.__yearCreate = year
        self.__brandName = nameBrand
        self.__fuelType = typeFuel
        self.__status = None

    def get_status(self):
        return self.__status

    def get_year(self):
        return self.__yearCreate

    def setYear(self, newYear):
        self.__yearCreate = int(newYear)
        if self.__yearCreate > 2010:
            self.__status = 'New Car'
        else:
            self.__status = 'Old Car'

    # @property
    # def year(self):
    #     return self.__yearCreate
    #
    # @year.setter
    # def year(self, newYear):
    #     self.__yearCreate = int(newYear)
    #     if self.__yearCreate > 2010:
    #         self.__status = 'New Car'
    #     else:
    #         self.__status = 'Old Car'

    # def getYear(self):
    #     return self.

    # def get_name(self):
    #     return self.__yearCreate
    #
    # def set_name(self, newName):
    #     self.__nameModel = newName.upper()

    @property
    def name(self):
        return self.__nameModel

    @name.setter
    def name(self, newName):
        self.__nameModel = newName.upper()


    def displayInfo(self):
        print(f'Information. \n'
              f'Model of the car: {self.__nameModel}'
              f'\nYear of manufacture: {self.__yearCreate}'
              f'\nBrand: {self.__brandName}'
              f'\nType of fuel: {self.__fuelType}')


def main():
    car1 = Car('Model S', '2020', 'Tesla', 'eco')
    car1.setYear('1999')
    print(car1.get_status())

    car1.setYear('2021')
    print(car1.get_status())

    car1.name = 'Model Y'
    print(car1.name)

    car1.displayInfo()

if __name__ == '__main__':
    main()