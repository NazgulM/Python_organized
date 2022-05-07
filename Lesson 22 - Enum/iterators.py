listNumbers = [34, 5, 55, 54, 34, 23, 43, 11]

for i in listNumbers:
    print(i, end='\n')
print('*' * 20)

iterList = iter(listNumbers)
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print('*' * 20)


class StopIterClass:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


myIterObject = StopIterClass(10)  # range(1, 11)
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print(next(myIterObject))
print('*' * 20)

myIterObj2 = StopIterClass(10)

for i in myIterObj2:
    print(i)
print('*' * 20)


# function for creating own generators
def print_num():
    for i in listNumbers:
        yield i

for i in print_num():
    print(i)


def gen_function():
    for i in listNumbers:
        yield i


for item in gen_function():
    print(item)
