class Student:
    def __init__(self, name, payment, debts, **marks):
        self.name = name
        self.payment = payment
        self.debts = debts
        self.marks = marks

    def __str__(self):
        return f'Student name is {self.name}, she has to pay {self.payment} USD for education,' \
               f'\nShe has debts on: {self.debts} according scores: {self.marks}'

    def __add__(self, other):
        if isinstance(other, Student):
            return Student(self.payment + other.payment)
        return self.payment + other

    def __radd__(self, other):
        if isinstance(other, Student):
            return Student(self.payment + other.payment)

    def __iadd__(self, other):
        self.payment = self + other
        return self.payment

    def __sub__(self, other):
        return self.payment - other

    def __rsub__(self, other):
        if isinstance(other, Student):
            return Student(self.payment - other.payment)

    def __isub__(self, other):
        self.payment = self - other
        return self.payment

    def __truediv__(self, other):
        if isinstance(other, Student):
            return Student(self.payment / other.payment)
        return self.payment / other

    def __rtruediv__(self, other):
        return self.payment / other

    def __itruediv__(self, other):
        self.payment = self / other
        return self.payment

    def __mul__(self, other):
        if isinstance(other, Student):
            return Student(self.payment * other.payment)
        return self.payment * other

    def __rmul__(self, other):
        return self.payment * other

    def __imul__(self, other):
        self.payment = self / other
        return self.payment

    def __pow__(self, power, modulo=None):
        return self.payment ** power

    def __rpow__(self, other):
        return self.payment ** other

    def __ipow__(self, other):
        self.payment = self ** other
        return self.payment

    def __getitem__(self, item):
        return self.name[item]

    def __lt__(self, other):
        if self.marks < other.marks:
            return True
        return False

    def __gt__(self, other):
        if self.marks > other.marks:
            return True
        return False

    def __le__(self, other):
        return self <= other

    def __eq__(self, other):
        return self == other

    def __ge__(self, other):
        return self >= other

    def __delitem__(self, key):
        del self.marks[key]

    def __del__(self):
        print('Delete student 1')

    def __len__(self):
        return len(self.debts)

    def __call__(self, *args, **kwargs):
        return sum(**args) / len(**args)

    def __contains__(self, item):
        if item in self.debts:
            return 'This subject in the list'
        return 'Cannot find this subject'

    def display(self):
        for counter, subj in enumerate(self.debts):
            print(f'{counter + 1}.{subj}')

    def display_using_generator(self):
        for i in self.debts:
            yield i


def squares_gen(x):
    for i in range(x):
        yield i * i


def main():
    marks = {'math': 75, 'history': 100, 'science': 50, 'bio': 100}
    student1 = Student('Nurilya', 50000, ['science', 'math'], **marks)
    print(student1.__str__())
    print('*' * 30)
    marks = {'english': 65, 'bio': 50, 'math': 100, 'science': 100}
    student2 = Student('Mariya', 65000, ['english', 'bio'], **marks)
    print(student2.__str__())
    print('*' * 30)

    print('Next year payment is: ', student1 + 25000)
    print('Two students total payment is: ', student1.payment + student2.payment)
    print('The second student payment would increase next year to: ', 15000 + student2.payment)
    print('*' * 30)

    print('If student1 will pass all exams, her payment can decrease to: ', student1.payment - 15000)
    print('Student2 education payment more than student1 payment for: ', student2.payment - student1.payment)
    print('Student2 can get 10% discount for excellent study for next year and can pay less: ', student2.payment - 6500)
    print('*' * 30)

    print('Payment for one semester for student1: ', student1.payment / 2)
    print('Student2 payment more than student1 payment for: ', student2.payment / student1.payment, 'times')
    print('Student2 can divide payment for 4  as: ', student2.payment / 4)
    print('Student2 semester payment is: ', student2.payment / 2)
    print('*' * 30)

    print('Student1 has to pay for whole 4 bachelor course: ', student1.payment * 4)
    print('Student2 has to pay for whole 4 bachelor course: ', student2.payment * 4)
    print('If multiply student1 and student2 payment would be: ', student1.payment * student2.payment)
    print('Student1 payment multiply for 10: ', student1.payment * 10)
    print('Three years annually payment for student 2: ', 3 * student2.payment)
    print('*' * 30)

    print(student1.payment ** 2)
    print(student2.payment ** 3)
    print(student1.payment ** 4)
    print('*' * 30)

    print('Nur' in student1.name)
    print('gul' in student2.name)
    print('*' * 30)

    print(list(student1.marks.values()) < list(student2.marks.values()))
    print(list(student1.marks.values()) > list(student2.marks.values()))
    print(list(student1.marks.values()) <= list(student2.marks.values()))
    print(list(student2.marks.values()) == list(student1.marks.values()))
    print(list(student1.marks.values()) >= list(student2.marks.values()))
    print('*' * 30)

    print(student1.marks['math'])
    del student1.marks['math']
    print('After deleting math from subject list: ', student1.marks)
    print('*' * 30)
    print('Student 2 has: ', len(student2.debts), 'debts')
    print('*' * 30)

    print('Average mark of student1: ', sum(student1.marks.values()) / len(student1.marks.values()))
    print('Average mark of student2: ', sum(student2.marks.values()) / len(student2.marks.values()))
    print('*' * 30)

    print('math' in student1.debts)
    print('science' in student2.debts)
    print('*' * 30)

    student1.display()
    print('*' * 30)
    student2.display()
    print('*' * 30)

    student1.display_using_generator()

    for item in student1.debts:
        print(item)
    print('*' * 30)

    student2.display_using_generator()

    for item in student2.debts:
        print(item)
    print('*' * 30)

    square = squares_gen(6)
    c = 0
    aver = 0
    for i in square:
        print(i)
        c+=i
        aver = c/5

    print('The sum of all numbers: ', c)
    print('The average of all numbers: ', aver)





    del student1


if __name__ == '__main__':
    main()
