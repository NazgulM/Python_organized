def my_decorator_hotel(funct):
    def wrapper(arg1, arg2):
        print('*' * 20)
        print(f'Welcome {arg1} to the hotel'
              '\n')

        print('Your room number is 15')
        print('*' * 20)

    return wrapper


def my_decorator_tour(funct):
    def wrapper(arg1, arg2):
        print('*' * 20)
        print('We are going to make a tour'
              '\nPlease introduce yourself')
        funct(arg1, arg2)
        print('{0} I see you paid 1000$ for a tour and I can give you Private package'
              '\nJust because you are from {1} addition discount 10%'.format(arg1, arg2))

    return wrapper


@my_decorator_tour
@my_decorator_hotel
def function_simple(name, city):
    print(f'My name is {name} and I live in {city}')


def calculate_nums(function_some):
    def wrapper(arg1, arg2):
        print(f'Result addition of {function_some(arg1, arg2)[0]} and {function_some(arg1, arg2)[1]} is: {arg1 + arg2}')

    return wrapper

# def multiplyOper(function_some):
#     def wrapper(arg1, arg2):
#         print(arg1*arg2)
#     return wrapper


@calculate_nums
# @multiplyOper
def calculateNum(num1, num2):
    return num1, num2


def main():
    namePerson = input('Name of a person: ')
    city = input('City: ')

    function_simple(namePerson, city)

    calculateNum(12, 33)



if __name__ == '__main__':
    main()
