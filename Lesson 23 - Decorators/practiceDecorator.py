def bold(text):
    def screen():
        print('<b>')
        text()
        print('</b>')

    return screen


def italic(text):
    def screen():
        print('<i>')
        text()
        print('</i>')

    return screen


def underline(text):
    def screen():
        print('<u>')
        text()
        print('</u>')

    return screen


@bold
@italic
@underline
def display():
    print('text')

def main():
    display()

if __name__ == '__main__':
    main()
