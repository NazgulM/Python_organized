# create dictionary if only string keys
# r = dict(moscow=495, piter=812, penza=8412)
# print(r)
# a = [['moscow', 495], ['piter', 812]]
# t = dict(a)
# q = dict.fromkeys(['a', 'b', 'c'], 100)
# print(q)
v = {}
print(v, type(v))
d = {
    1: 45,
    'hello': 'two',
    3: 'three'
}
print(d[3])

technic_dict = {0: 'turn on',
                1: 'turn off'}
print(technic_dict)
technic_dict[2] = 'neither one'
print(technic_dict[2])

technic_dict.update({3: 'break', 4: 'never worked'})
print(technic_dict)

print(technic_dict.get(2))
print(technic_dict.get(5, 'nothing found'))

for key in technic_dict:
    print(key)
print()
for key in technic_dict.keys():
    print(key)
print()
for val in technic_dict.values():
    print(val)
print()
for key in technic_dict.keys():
    print(technic_dict[key])
