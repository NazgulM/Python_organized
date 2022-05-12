def dec(someText):
    textFromFunct = someText()
    def wrapper():
        print('**************')
        print(someText())
        print('*************')

    return wrapper


def len_text(someText):
    def wrapper():
        stringLen = len(someText())
        print(stringLen)

    return wrapper


@dec
@len_text
def staticText():
    return 'Good morning'


def main():
    staticText()


if __name__ == '__main__':
    main()
