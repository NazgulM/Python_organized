myWorkerDict = {
    "Сотрудник 1":

        {"ФИО": "Адилет Эшмаматов",
         "Возраст": 28,
         "Род деятельности": "Работник цеха",
         "Заработная плата": 25000,
         "ФИО Супруга/и": "Гульзада Саратова",
         "Дети": {"Ребенок 1": "Мухаммад Эшмаматов",
                  "Ребенок 2": "Элиза Эшмаматова"

                  },
         "Транспорт": "Тойота Камри 35",
         "Адрес проживания": "г. Бишкек, ул. Лев Толстой 77"

         },

    "Сотрудник 2":

        {"ФИО": "Эсен Урматов",
         "Возраст": 30,
         "Род деятельности": "Работник цеха",
         "Заработная плата": 31000,
         "ФИО Супруга/и": "Тамара Тиленова",
         "Дети": {"Ребенок 1": "Усон Урматов", },
         "Транспорт": "Хонда Фит",
         "Адрес проживания": "г. Бишкек, ул. Чуй 123"

         },

    "Сотрудник 3":

        {
            "ФИО": "Аселя Давлетова",
            "Возраст": 30,
            "Род деятельности": "Работник бухгалтерии",
            "Заработная плата": 42000, "ФИО Супруга/и":
            "Сергей Васильев",
            "Дети": {"Ребенок 1": "Елена Васильева",
                     "Ребенок 2": "Степан Васильев",
                     "Ребенок 3": "Марат Васильев", },
            "Транспорт": "БМВ X7",
            "Адрес проживания": "г. Бишкек, ул. Токтогула 76"
        },

    "Сотрудник 4":

        {
            "ФИО": "Мария Степанова",
            "Возраст": 29,
            "Род деятельности": "Работник маркетинга",
            "Заработная плата": 85000,
            "ФИО Супруга/и":
                "Олег Кичин", "Дети": {"Ребенок 1": "Василиса Кичина", },
            "Транспорт": "Тойота Камри 35",
            "Адрес проживания": "г. Бишкек, мкр 7 дом 76, кв: 14"
        },

    "Сотрудник 5":
        {
            "ФИО": "Олег Иванов",
            "Возраст": 45,
            "Род деятельности": "Генеральный Директор",
            "Заработная плата": 70000,
            "ФИО Супруга/и": "Светлана Валерьева",
            "Дети": {"Ребенок 1": "Григорий Иванов",
                     "Ребенок 2": "Наталья Иванова",
                     "Ребенок 3": "Василий Иванов",
                     "Ребенок 4": "Филип Иванов", },
            "Транспорт": "БМВ X5",
            "Адрес проживания": "г. Бишкек, мкр 5 дом 16, кв: 102"
        },
}


def showWorkers():
    if len(myWorkerDict) != 0:
        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================')
            for key, values in workerDict.items():
                if key == "Дети":
                    workerNameList = workerDict["ФИО"].split(" ")
                    print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                          f'\n************************')

                    for child, childInfo in values.items():
                        print(f'{child}: {childInfo}')
                    print('************************')
                if key == "Дети":
                    continue
                print(f'{key}: {values}')
    else:
        print('База сотрудников пуста!')


def searchWorker(nameWorker):
    for worker, workerDict in myWorkerDict.items():
        for key, valueWorker in workerDict.items():
            if valueWorker == nameWorker:
                for key, valueWorker in workerDict.items():
                    print(key, valueWorker)


def showListAwarded():
    listAwardedWorkers = []
    numberAwarded = int(input('Вы выбрали меню №4.\nНапишите кол-во людей для награждения: '))

    for i in range(numberAwarded):
        try:
            nameAwarded = input('Имя чел-ка для награждения: ')
        except:
            print('You entered the wrong, please enter one more time')

        for worker, workerDict in myWorkerDict.items():
            if nameAwarded == workerDict["ФИО"]:
                listAwardedWorkers.append(workerDict["ФИО"])
            else:
                pass

    return listAwardedWorkers


def delWorker(nameWorker):
    valDelete = None
    for worker, workerDict in myWorkerDict.items():
        for k, v in workerDict.items():
            if nameWorker in workerDict.values():
                valDelete = worker

    del myWorkerDict[valDelete]


def findMaxSalary():
    salaryList = []
    for worker, workerDict in myWorkerDict.items():
        salaryList.append(workerDict["Заработная плата"])
    maxSalary = max(salaryList)

    nameWorker_maxSalary = None
    for worker, workerDict in myWorkerDict.items():
        if workerDict["Заработная плата"] == maxSalary:
            nameWorker_maxSalary = workerDict["ФИО"]

    return nameWorker_maxSalary


def findSumSalary():
    salaryList = []
    for worker, workerDict in myWorkerDict.items():
        salaryList.append(workerDict["Заработная плата"])
    sumSalary = sum(salaryList)

    return sumSalary


def addingWorker():
    try:
        nameInput = input('Вы выбрали меню №2.'
                          '\nНапишите ФИО Сотрудника для добавления: ')
    except:
        print('Try again')

    age = int(input('Возраст: '))
    typeWork = input('Род деятельности: ')
    salary = int(input('Напишите зарплату: '))
    fioWifeHusb = input('Напишите имя супруга/и: ')
    quantChild = int(input('Кол-во детей: '))

    child = {}
    # 3 - range(3) - 0,1,2
    for i in range(quantChild):
        childKey = 'Ребенок ' + str(i + 1)
        child[childKey] = input(f'Пожалуйста введите '
                                f'имя для {i + 1} ребенка: ')

    nameOfTransport = input('Название транспорта: ')
    address = input('Адрес проживания: ')

    countWorker = len(myWorkerDict) + 1
    countWorkerKey = 'Сотрудник ' + str(countWorker)
    myWorkerDict[countWorkerKey] = {"ФИО": nameInput,
                                    "Возраст": age,
                                    "Род деятельности": typeWork,
                                    "Заработная плата": salary,
                                    "ФИО Супруга/и": fioWifeHusb,
                                    "Дети": child,
                                    "Транспорт": nameOfTransport,
                                    "Адрес проживания": address
                                    }

    print('Новый словарь работников теперь выглядит так:')


def addingSalary(sumSalaryAdd, nameWorker):
    keyWorker = None
    for worker, workerDict in myWorkerDict.items():
        for k, v in workerDict.items():
            if nameWorker in workerDict.values():
                keyWorker = worker

    # myWorkerDict[keyWorker]["Заработная плата"] =  int(myWorkerDict[keyWorker]["Заработная плата"]) + salaryAdd_value
    myWorkerDict[keyWorker]["Заработная плата"] += sumSalaryAdd

    print(f'Новая ЗП сотрудника {myWorkerDict[keyWorker]["ФИО"]}: '
          f'{myWorkerDict[keyWorker]["Заработная плата"]}')


def avgSalary():
    salaryList = []
    for worker, workerDict in myWorkerDict.items():
        salaryList.append(workerDict["Заработная плата"])
    avgSalaryWorker = sum(salaryList) / len(salaryList)

    return avgSalaryWorker


def showTransport():
    setTransport = set()

    for worker, workerDict in myWorkerDict.items():
        if workerDict["Транспорт"] == 'Пешком':
            continue
        setTransport.add(workerDict["Транспорт"])
    # setTransport.discard('Пешком')
    counter = 1
    for transport in setTransport:
        print(f'Транспорт {counter}: {transport}')
        counter += 1


def showKids():
    listOfKids = []

    for worker, workerDict in myWorkerDict.items():
        for k, v in workerDict["Дети"].items():
            listOfKids.append(v)

    print(f'Кол-во детей сотрудников: {len(listOfKids)}')

    return listOfKids


def showListRest():
    listRestWorkers = []
    numberForRest = int(input('Вы выбрали меню №5.\nНапишите кол-во людей для выхода в отпуск: '))

    for i in range(numberForRest):
        nameRest = input('Имя чел-ка, который собирается в отпуск: ')
        for worker, workerDict in myWorkerDict.items():
            if nameRest == workerDict["ФИО"]:
                listRestWorkers.append(workerDict["ФИО"])
            else:
                pass

    return listRestWorkers


def reduceSalary(sumSalaryReduce, nameEmpl):
    keyWorker = None
    for worker, workerDict in myWorkerDict.items():
        for k, v in workerDict.items():
            if nameEmpl in workerDict.values():
                keyWorker = worker

    # myWorkerDict[keyWorker]["Заработная плата"] =  int(myWorkerDict[keyWorker]["Заработная плата"]) + salaryAdd_value
    myWorkerDict[keyWorker]["Заработная плата"] -= sumSalaryReduce

    print(f'Новая ЗП сотрудника {myWorkerDict[keyWorker]["ФИО"]}: '
          f'{myWorkerDict[keyWorker]["Заработная плата"]}')


def findMinSalary():
    salaryList1 = []
    for worker, workerDict in myWorkerDict.items():
        salaryList1.append(workerDict["Заработная плата"])
    minSalary = min(salaryList1)

    nameWorker_minSalary = None
    for worker, workerDict in myWorkerDict.items():
        if workerDict["Заработная плата"] == minSalary:
            nameWorker_minSalary = workerDict["ФИО"]

    return nameWorker_minSalary


def main():
    menu = """
      1 - Поиск сотрудника 
      2 - Добавление нового сотрудника 
      3 - Удаление сотрудника 
      4 - Составить список для награждения сотрудников 
      5 - Составить список сотрудников на отпуск 
      6 - Повышение З-П 
      7 - Понижение З-П 
      8 - Отобразить имя сотрудника, получающий максимальную З-П 
      9 - Отобразить имя сотрудника, получающий минимальную З-П 
      10 - Подсчет среднемесячной Заработной платы 
      11 - Вывод суммарной З-П всех сотрудников 
      12 - Виды транспорта всех сотрудников 
      13 - Отобразить имена и кол-во детей всех сотрудников 
      14 - Отобразить всех сотрудников 
      0 - Выход из Программы
    """
    option = None
    while option != 0:
        print(menu)
        option = int(input('Ввод: '))

        if option == 1:

            try:
                nameSearch = input('Вы выбрали меню №1.\nНапишите имя для поиска: ')
            except:
                print('Please enter the string, not number')

                nameSearch = input('Вы выбрали меню №1.\nНапишите имя для поиска: ')

            searchWorker(nameSearch)

        elif option == 2:
            addingWorker()
            showWorkers()
        elif option == 3:
            try:
                nameDelete = input('Вы выбрали меню "Удаление сотрудника"\n'
                               'Напишите имя сотрудника для удаления: ')
            except KeyError:
                nameDelete = input('Вы выбрали меню "Удаление сотрудника"\n'
                                   'Напишите имя сотрудника для удаления еще раз: ')

            delWorker(nameDelete)
            print('\nНовый словарь работников теперь выглядит так:')
            showWorkers()
        elif option == 4:
            counter = 1
            listWorkerAwarded = showListAwarded()
            for i in listWorkerAwarded:
                print(f'Сотрудник {counter} -ый для награды {i}')
                counter += 1
        elif option == 5:

            counter = 1
            listWorkerRest = showListRest()
            for i in listWorkerRest:
                print(f'Сотрудник {counter} -ый для отпуска {i}')
                counter += 1
        elif option == 6:
            print('Вы выбрали меню 6 - Повышение З-П')
            nameWorker = None
            salaryAdd_value = None

            try:
                nameWorker = input('Введите имя сотруд-ка, для повышение ЗП: ')
                salaryAdd_value = int(input('На сколько повысить ЗП? :'))
            except ValueError:
                print('Введите число! Повторите вновь:')

                nameWorker = input('Введите имя сотруд-ка, для повышение ЗП: ')
                salaryAdd_value = int(input('На сколько повысить ЗП? :'))
            except BaseException:
                print('Ошибка! Повторите вновь: ')

                nameWorker = input('Введите имя сотруд-ка, для повышение ЗП: ')
                salaryAdd_value = int(input('На сколько повысить ЗП? :'))
            finally:
                addingSalary(salaryAdd_value, nameWorker)
        elif option == 7:
            print('Вы выбрали меню 7 - Понижение З-П')
            nameEmpl = None
            salaryReduce_value = None

            try:
                nameEmpl = input('Введите имя сотруд-ка, для понижения ЗП: ')
                salaryReduce_value = int(input('На сколько понизить ЗП? :'))
            except ValueError:
                print('Введите число! Повторите вновь:')

                nameEmpl = input('Введите имя сотруд-ка, для понижения ЗП: ')
                salaryReduce_value = int(input('На сколько понизить ЗП? :'))
            except BaseException:
                print('Ошибка! Повторите вновь: ')

                nameEmpl = input('Введите имя сотруд-ка, для понижения ЗП: ')
                salaryReduce_value = int(input('На сколько понизить ЗП?: '))
            finally:
                reduceSalary(salaryReduce_value, nameEmpl)

        elif option == 8:
            print('Вы выбрали меню 8 - Отобразить имя сотрудника, получающий максимальную З-П ')
            nameWorkerMaxSalary = findMaxSalary()
            print(f'Сотрудник с максимальной ЗП: {nameWorkerMaxSalary}')
        elif option == 9:
            print('Вы выбрали меню 9 - Отобразить имя сотрудника, получающий минимальную З-П ')
            nameWorkerMinSalary = findMinSalary()
            print(f'Сотрудник с минимальной ЗП: {nameWorkerMinSalary}')
        elif option == 10:
            print(f'Вы находитесь в 10 Меню - Нахождения Среднемесячной ЗП\n '
                  f'Среднемесячная ЗП {avgSalary()}')
        elif option == 11:
            print(f'Суммарная З-П всех сотрудников: {findSumSalary()}')
        elif option == 12:
            print(f'Вы находитесь в 11 Меню - Отображение всех транспортов Сотрудников')
            showTransport()
        elif option == 13:
            listOfChilds = showKids()

            counter = 1
            for child in listOfChilds:
                print(f'Ребенок {counter}: {child}')
                counter += 1

        elif option == 14:
            showWorkers()
        if option == 0:
            print('Программа Завершена! Всего Вам хорошего!')
            break

        elif option not in (range(0, 15)):
            print('Вы выбрали не правильную опцию! Попытайтесь заново!')


if __name__ == '__main__':
    main()
