class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def findArea(self):
        return self.height * self.width

    def __lt__(self, other):
        if isinstance(other, Area):
            return self.findArea() < other.findArea()

        return False

    def __gt__(self, other):
        if isinstance(other, Area):
            return self.findArea() > other.findArea()
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Area):
            return self.findArea() == other.findArea()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Area):
            return self.findArea() <= other.findArea()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Area):
            return self.findArea() >= other.findArea()
        else:
            return False

    def __mod__(self, other):
        if isinstance(other, Area):
            return self.findArea() % other.findArea()
        else:
            return self.findArea() % other

    def __rmod__(self, other):
        if isinstance(other, Area):
            return self.findArea() % other.findArea()
        else:
            return self.findArea() % other

    def __call__(self, a, b):
        print(self.findArea() + (a * b))

    def __pow__(self, power, modulo=None):
        return self.findArea() ** power

    def __contains__(self, item):
        listOfSides = [self.width, self.height]
        if item in listOfSides:
            return True

        return False

    def __getitem__(self, item):
        listOfSides = [self.width, self.height]

        return listOfSides[item]



def main():
    area1 = Area(12, 30)  # 360
    area2 = Area(15, 20)  # 300

    print(area1 > area2)
    print(area1 < area2)
    print(area1 == area2)
    print(area1 >= area2)
    print(area1 <= area2)

    print(area1 % area2)
    print(area2 % area1)
    print(area1 % 400)

    area1(2, 25)

    print(area1 ** 2)
    print(area2 ** 3)

    print(30 in area1)
    print(25 in area2)
    print('***************')

    print(area2[0])
    print(area1[1])



    def __copy__(self):
        print('Processing copy....')
        my_copy = type(self)
        my_copy.__dict__.update(self.__dict__)






if __name__ == '__main__':
    main()
