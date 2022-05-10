class Student:
    def __init__(self, name, payment, marks, subjectslist):
        self.nameStudent = name
        self.pay = payment
        self.marksStudent = marks
        self.subjectlist = subjectslist

    def __contains__(self, item):
        if item in self.subjectlist:
            return True

        return False

    def display(self):
        print(f'Student: {self.nameStudent}'
              f'Payment: {self.pay}')

        print('Оценки по предметам: ')
        # (1,('Math',5))
        for numb, subjectInfo in enumerate(self.marksStudent.items(),1):
            print(f'{numb}. Mark for {subjectInfo[0]}: {subjectInfo[1]}')


        print('Список долгов по предметам: ')
        for numb, subjectName in enumerate(self.subjectlist,1):
            print(f'{numb}. {subjectName}')

    def __call__(self):
        print('Average mark of student1: ',
              sum(self.marksStudent.values()) / len(self.marksStudent.values()))


#Task 4


def my_genFindPower(numb):
    for i in range(1,numb+1):
        yield i**2


def main():
    student1 = Student('Sam Alvey', 25000, {'Math': 5, 'Geography':3, 'Physics':4},
                       ['Algebra', 'Geometry', 'Biology'] )

    print('English' in student1)
    student1.display()

    student1()

    numb = int(input('Numb: '))

    findPower = my_genFindPower(numb)
    sumNumbs = 0
    for i in findPower:
        print(i)
        sumNumbs+=i

    avgNumb = sumNumbs/numb

    print(f'Sum is {sumNumbs}'
          f'\nAvg is {avgNumb}')




if __name__ == '__main__':
    main()
