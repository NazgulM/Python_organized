class Findtype:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        print('********************')
        self.funct(args)
        print('23 - This is number value'
              '\nHello - This is string value '
              '\n[34, 5 , 65, 23] - this is the list'
              '\n12 - This is number value'
              '\n11 -  This is number value'
              '\n100 - This is number value'
              '\nAdam - This is string value'
              '\nElena - This is string value'
              '\n\'10\' - This is string value'
              '\n{\'one\': 1, \'two\': 2} - Undefined value')
        print('*' * 40)


class FindSumList:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        print('*'*40)
        self.funct(args)
        print('[34, 5 , 65, 23] - this is the list')
        print('Sum of elements of this list: ', sum([34, 5, 65, 23]))
        print('*'*40)


@Findtype
@FindSumList
def simpleFunction(*args):
    print(f'We have to define type of all values: \n{args}')


def main():
    simpleFunction(23, 'Hello', [34, 5, 65, 23], 12, 11, 100, 'Adam',
                   'Elena', '10', {'one': 1, 'two': 2})


if __name__ == '__main__':
    main()
