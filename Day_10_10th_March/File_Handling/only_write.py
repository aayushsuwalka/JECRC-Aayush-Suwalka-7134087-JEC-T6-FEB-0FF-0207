file = open('temp1.txt', 'w+')
file.writelines([
    'first line \n'
    'second line \n'
    'third line \n'
    'forth line \n'
    'fifth line \n'
    'sixth line \n'
])
file.seek(0) # to make the python interpreter to point at a specific index, we use seek(index)
print(file.read())
file.close()