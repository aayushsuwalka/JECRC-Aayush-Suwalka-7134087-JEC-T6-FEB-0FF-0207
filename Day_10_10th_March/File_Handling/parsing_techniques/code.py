## DUMPS
## LOADS

'''
JSON

'''


import json
file = open('temp.txt', 'a+')
data = {
    'fullname' : 'Aayush Suwalka',
    'userid' : 89654623,
    'password' : '*********',
}


# print(f'Orginal Data : {data}')
# print(f'Type of Data : {type(data)}')
enc_data = json.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data = file.read()
print(type(enc_data))
ori_data = json.loads(enc_data)
print(ori_data, type(ori_data))

# enc_data = json.dumps(data)
# print(f'Encrypted data : {enc_data}')
# print(f'Type of Encrypted Data : {type(enc_data)}')

# dec_data = json.loads(enc_data)
# print(f'Decrypted data : {dec_data}')
# print(f'Type of Decrypted Data : {type(dec_data)}')