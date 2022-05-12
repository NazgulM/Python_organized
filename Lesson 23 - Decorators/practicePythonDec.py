def decoratorShowAvg(funct):
    def wrapper(someList):
        print('***************')
        funct(someList)
        print('***************')
        print(f'Average of list is: {sum(someList) / len(someList)}')

    return wrapper


def decoratorSum(funct):
    def wrapper(someList):
        funct(someList)
        print(f'Sum of the list: {sum(someList)}')

    return wrapper


@decoratorShowAvg
@decoratorSum
def show_list(someList):
    print('All the elements in the list: ')
    for i in someList:
        print(i)


def main():
    show_list([32432, 54, 46, 546, 65])


if __name__ == '__main__':
    main()
