str1 = "Я учу программирование"

for i in str1:
    print(i)
print('*' * 20)

iterList = iter(str1)
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))

print('*' * 20)


def gen_function():
    for i in str1:
        yield i


for item in gen_function():
    print(item)
print('*' * 20)

with open('mytext.txt', 'r') as file1:
    line = file1.readlines()


def iter_function():
    for i in line:
        yield i


for item in iter_function():
    print(item)
