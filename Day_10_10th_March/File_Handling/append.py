file = open('jecrc.txt', 'a+')
# file.write("JECRC is the world's best univerity")
file.write("JECRC is also popular for placements")
file.writelines([
    '\n Here Food is Good \n',
    'ECO System is Good \n',
    'Facilities are very supportive \n'
])
file.seek(0)
print(file.read())



file.close()