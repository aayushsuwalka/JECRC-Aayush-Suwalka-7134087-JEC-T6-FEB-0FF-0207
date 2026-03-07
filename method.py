#--Syntax--
'''
class ClassName:
    def method_name(self, arg):
        Statement
        Block
'''

from sys import _enablelegacywindowsfsencoding


class Car():
 
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


    def display_properties(self):
        print({
            'wheelers': self.wheelers,
            'engine': self.engine,
            'base_speed': self.base_speed,
            'max_speed' : self.max_speed,
            'gear_no': self.gear_no,
            'security': self.security,
            'base_budget': self.base_budget,
            'varient': self.varient,
            'total_sale': self.total_sale 
        })

    def update_base_speed(self, new_speed):
        self.base_speed = new_speed
        print(f'New Base Speed: {self.base_speed}')


    
    def update_max_speed(self, new_speed):
        self.max_speed = new_speed
        print(f'New Max Speed: {self.max_speed}')


TATA = Car(True, 'Level 5', '2L', 12, 100000)
print('Properties Befor Updation')
TATA.display_properties()
print()

print('Properties After Updation')
TATA.update_base_speed(60)
TATA.update_max_speed(200)
TATA.display_properties()
print()