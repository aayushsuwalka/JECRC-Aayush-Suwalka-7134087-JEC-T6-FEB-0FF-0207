
class Car():
    ## Below variables 
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40 kmph'
    max_speed = '180 kmph'
    gear_no = 4

    def __init__ (self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags = air_bags
        self.security = security
        self.base_budget = base_budget
        self.varient = varient
        self.total_sale = total_sale



# TATA = Car()
# TATA.engine = ['Petrol', 'Diesel', 'EV']
# TATA.airbags = True
# TATA.no_of_airbags = 4
# TATA.base_budget = '2L'
# TATA.no_of_varient = 12


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


    

TATA = Car(True, 'Level 5', '2L', 12, 1000000)
Toyota = Car(True, 'Level 4', '3L', 10, 860000)
