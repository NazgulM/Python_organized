numberDict = {'One': 1, 'Two': 2, 'Ten': 10, 'Nineteen': 19}

# for i in numberDict:
#     print(numberDict.get(i))
#
# print(numberDict.keys())
# print(numberDict.values())
#
# for j in numberDict.keys():
#     print(j)
#
# for v in numberDict.values():
#     print(v)

for k,v in numberDict.items():
    print('This is a key ' + str(k) + ', This is a value ' + str(v))
print()
print(numberDict.keys())
print(numberDict.values())
print(numberDict.items())
usersInput = 19
for i in numberDict.keys():
    if i ==usersInput:
        print(numberDict.get(i))