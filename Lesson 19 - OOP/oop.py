"""
При ООП разработка начинается с создания класса, данные и переменные
Главное в ООП, это объекты, они становятся автономными.
Мы можем использовать в разных целях, история начинается в начала 1960
Кристен Найберт и Даль
Термин ООП был использован компанией Эксель
Если мы разрабатываем функцию, нам нужно что то изменить, операторы или переменные,
Основным достоинством ООП - гибкость, использование новых программ,
работа между несколькими независимыми программами
"""


class Person:
    def __init__(self, name, age, address, speedRun):
        # print('Создание объекта человека')
        self.name = name
        self.age = age
        self.address = address
        self.speedRun = speedRun

    def sayHello(self, name):
        print(f'Hello there! {name} from {self.name} be my guest at adress {self.address}')

    def runnning(self):
        print(f'{self.name} runs with speed {self.speedRun}')


adilet = Person('Adilet  Eshmamatov', 25, 'Lev Tolstoy123', 50)
adilet.sayHello('Samara')
adilet.runnning()

samat = Person('Samat Dursunov', 32, 'Mira 7', 70)
samat.sayHello('Olga')
samat.runnning()
# samat.sayHello('Tamara')
turat = Person('Turat Bolotov', 26, 'Mira 71', 35)
turat.runnning()

# print(id(adilet))
# print(type(adilet))
# print(id(samat))


"""
Создать класс животные Animal
- возраст
- тип животного (корова, собака)
- звук животного (му-му, гав, гав)
- порода

создать ф-ию внутри класса Animal, которая отображает все эти информации

Создать 5 типов животных (5 объектов живот)
"""


class Animal:
    def __init__(self, age, typeAnimal, voice, breed):
        self.age = age
        self.typeAnimal = typeAnimal
        self.voice = voice
        self.breed = breed

    def animalInfo(self):
        print(f'This {self.typeAnimal} is {self.age} yo and '
              f'it can {self.voice} and its breed {self.breed}')


horse = Animal('Horse', 10, 'neigh-neigh', 'Arabian')
horse.animalInfo()
# duck = Animal()
# cat = Animal()
# dog = Animal()
# cow = Animal()
