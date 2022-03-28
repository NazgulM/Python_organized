def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


x = 3
print(f'The factorial of {x} is {factorial(x)}')

print()


def double(n):
    return n * 2


print(double(10))

print()

double1 = lambda n: n * 2
print(double1(10))
print()

larger = lambda a,b: a if a > b else b
print(larger(157, 47))

print()

names = ['Alan', 'Gregory', 'Zlatan', 'Jonas', 'Tom', 'Augustine']
names.sort(key = lambda x: len(x))
print(names)