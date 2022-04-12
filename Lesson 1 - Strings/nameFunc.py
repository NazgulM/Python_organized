print(__name__)


def greet():
    print('Hello World')


if __name__ == '__main__':
    greet()


def is_leap(year):
    leap = False

    # Write your logic here
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input('Please enter the year: '))
print(is_leap(year))


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))

my_function_with_args("Naza", "Have a nice day")
