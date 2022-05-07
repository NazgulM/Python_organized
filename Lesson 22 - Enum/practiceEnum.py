myList = [23, 43, 54, 34, 54, 56]

for id in enumerate(myList, 1):
    print(f'Result of multiplication {id[0]} number: {id[1]*10}. \nResult of division {id[0]} number: {id[1]/2}')