name = ['bas', 'bank', 'mek', 'dome']
print(name)

print(name[0], name[3])

print(name[-1], name[-3])

name[0] = 'pump'
print(name)

name.append('ploy')
print(name)

# add value from list
name.insert(0, 'bas')
print(name)

# remove value from list
name.pop(0)
print(name)

print(len(name))

# loop list
for index, name in enumerate(name):
    print(index, name)
