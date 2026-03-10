file = open('temp1.txt', 'r')
# '''
# read() : Display the content as it is.
# readline() : nDisplay single line at a time
# readlines()
# '''
print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())



file.close()
# file = open('notes.txt')