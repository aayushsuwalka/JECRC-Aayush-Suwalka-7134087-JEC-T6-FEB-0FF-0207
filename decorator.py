##--Syntax--
'''
class ClassName:
    @classmethod
    def method_name(cls, args):
        statement
        block
'''

class Car():
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40 kmph'
    max_speed = '120 kmph'
    gears = 4

    def __init__(self, air_bags, security, base_budget, varient, total_sale):
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
            'max_speed': self.max_speed,
            'gears': self.gears,  
            'security': self.security,
            'base_budget': self.base_budget,
            'varient': self.varient,
            'total_sale': self.total_sale
        })

    @classmethod
    def update_gears(cls, new_gears):
        cls.gears = new_gears
        print(f'No of Gears: {cls.gears}')


TATA = Car(True, 'Level 5', '2L', 12, 100000)

print('Properties Before Updation')
TATA.display_properties()
print()

print('Properties After Updation')
TATA.update_gears(5)
TATA.display_properties()


mahindra = Car(True, 'Level 4', '4L', 10, 20678)
mahindra.display_properties()