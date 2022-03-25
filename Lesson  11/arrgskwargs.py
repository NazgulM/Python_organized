# args - Передача неопределенных параметров
def functionarg(*args):
    print(type(args))
    listNums = list(args)
    for i in args:
        print(i, end=' ')


def kwargsFunction(**kwargs):
    print(type(kwargs))

    for k, v in kwargs.items():
        print(f'{k}:{v}')


def both(*args, **kwargs):
    print(args)
    print('=========')


def main():
    functionarg(23, 43, 54, 65, 76)

    someDict = {
        'name': 'Askar',
        'age': 25,
        'address': 'Mira 7'
    }
    kwargsFunction(name='Askar', age=25, address='Mira 7')
    kwargsFunction(**someDict)

    both(23, 43, 54, 65, 76, name='Askar', age=25, address='Mira 7')



if __name__ == '__main__':
    main()
