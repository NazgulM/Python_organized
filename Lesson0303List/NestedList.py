listNested = [12,3,23,[223,43,4], [232,43,4], 34,[134,[23,43,5]]]
print(listNested)
print()
print(listNested[3][2]) #4
print(listNested[6][1][1])

listNested2 = [
              [12,43,4],
              [34,5,6],
              [12,6,7]
               ]
for row in listNested2:
    for elem in row:
        print(f'{elem}', end=' ')
        print('\n')