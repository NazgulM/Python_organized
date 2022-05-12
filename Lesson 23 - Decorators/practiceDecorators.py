def decorator_py(funct):
    def wrapper():
        stringLen = len(funct())
        textFromfunct = funct()

        print("******")
        print(textFromfunct)
        print(stringLen)
        print("******")
    return wrapper

def decorator_py2(funct):
    def wrapper():
        stringLen = len(funct())
        print(stringLen)
    return wrapper

@decorator_py
def my_text():
    return 'sdadsaasd'

def main():
    my_text()

if __name__ == '__main__':
    my_text()

