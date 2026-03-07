class Car():
    ## Below variables 
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40 kmph'
    max_speed = '180 kmph'
    gear_no = 4



TATA = Car()
TATA.engine = ['Petrol', 'Diesel', 'EV']
TATA.airbags = True
TATA.no_of_airbags = 4
TATA.base_budget = '2L'
TATA.no_of_varient = 12

def __init__ (self, air_bags, seurity, base_budget, varient, total_sale):
    self.air_bags = air_bags



## ---Constructor--- (__init__)
'''
class ClassName:
    properties

    def __init__(self, arg1, arg2, ...., argn):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        . . . .   = . .
        . . . .   = . .
        . . . .   = . .
        self.argn = argn

'''



## For accesing the properties, we have to follow the below syntax:


# TATA = Car()
# TATA.airbags = True
# TATA.security = 'Level 5'
# print('Properties for TATA ----')
# print(f'No of Wheelers: {TATA.wheelers}')
# print(f'Engine Type: {TATA.engine}')
# print(f'Base Speed: {TATA.base_speed}')
# print(f'Max Speed: {TATA.max_speed}')
# print(f'No of manual gears: {TATA.gear_no}')
# print()


# kia = Car()
# print('Properties for Kia ----')
# print(f'No of Wheelers: {kia.wheelers}')
# print(f'Engine Type: {kia.engine}')
# print(f'Base Speed: {kia.base_speed}')
# print(f'Max Speed: {kia.max_speed}')
# print(f'No of manual gears: {kia.gear_no}')
# print()


# mahindra = Car()
# print('Properties for Mahindra ----')
# print(f'No of Wheelers: {mahindra.wheelers}')
# print(f'Engine Type: {mahindra.engine}')
# print(f'Base Speed: {mahindra.base_speed}')
# print(f'Max Speed: {mahindra.max_speed}')
# print(f'No of manual gears: {mahindra.gear_no}')
# print()


# toyota = Car()
# print('Properties for Toyota ----')
# print(f'No of Wheelers: {toyota.wheelers}')
# print(f'Engine Type: {toyota.engine}')
# print(f'Base Speed: {toyota.base_speed}')
# print(f'Max Speed: {toyota.max_speed}')
# print(f'No of manual gears: {toyota.gear_no}')



# suzuki = Car()
# print('Properties for Suzuki ----')
# print(f'No of Wheelers: {suzuki.wheelers}')
# print(f'Engine Type: {suzuki.engine}')
# print(f'Base Speed: {suzuki.base_speed}')
# print(f'Max Speed: {suzuki.max_speed}')
# print(f'No of manual gears: {suzuki.gear_no}')
