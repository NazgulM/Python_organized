# def functionWithFunction(funct):
#     def test():
#         print('Тестируем ф-ии внутри ф-ии')
#
#     print('This is text in functionWithFunction')
#     # test()
#     hello()
#     print('End of display of function')

def bread(funct):
    def wrapper():
        print('~~~~~~')
        funct()
        print('~~~~~~')
    return wrapper

def tomatos(funct):
    def wrapper():
        print('~@~@~')
        funct()
        print('~@~@~')
    return wrapper

def cucumber(funct):
    def wrapper():
       print('&&&&&')
       funct()
       print('&&&&&')
    return wrapper


@tomatos
@cucumber
@bread
def meat():
    print('=Meat=')


@bread
@cucumber
def fish():
    print('=Fish=')

@tomatos
def chicken():
    print('=Chicken=')

@cucumber
def fish2():
    print('=Fish=')

"""
~~~~~~
~~~~~~
=Meat=
"""

def main():
    meat()
    print('-'*20)
    fish()
    print('-' * 20)
    chicken()

    print('-' * 20)
    fish2()

if __name__ == '__main__':
    main()


