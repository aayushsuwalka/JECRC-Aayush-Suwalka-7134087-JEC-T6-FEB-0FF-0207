# INHERITENCE 
'''
1. Single Level Inheritence 
2. Multilevel Inheritence '
3. Multiple Inheritence
4. Herarchical Inheritence
5. Hybrid Ingeritence

'''

# Single Level :- We will have a single parent and child class. Also the properties will be derived only once.
class Parent:
# The class from which we are going derive the properties 
    bank_balance = '50L'
    def __init__(self, members):
        self.members = members
    def desc(self):
        print("I m the parent class")
class Child(Parent):
# The class in whichj we are going to derive the properties
    def __init__(self, child_name, *args):
        self.child_name = child_name
        super().__init__(args)
    pass
obj = Child("Rakesh", "Mom", "DAD")
print(obj.members)
print(obj.child_name)
obj.desc()


# Constructor Chaining : Calling parent class constructor from inside child class's constructor


# Multilevel Inheritence : It is a type of inheritence in which the properties will be derived from one to another class by considering more than one level

class Class_1:
    a = 'class_1'
class Class_2(Class_1):
    b = 'class_2'
class Class_3(Class_2):
    c = 'class_3'
class Class_4(Class_3):
    d = 'class_4'
class Class_5(Class_4):
    e = 'class_5'
obj = Class_5()
print(obj.a, obj.b, obj.c, obj.d, obj.e)

# Multiple Inheritence : It is a type of inheritence in which the properties will be derived from multiple parent class to a single child class
class Parent_1:
    a = 10
class Parent_2:
    b = 100
class Parent_3:
    c = 1000
class Parent_4:
    d = 10000
class Child(Parent_1, Parent_2, Parent_3, Parent_4):
    pass

print(Child.a, Child.b, Child.c, Child.d)

# Herarchical Inheritence: It is a type of inheritence in which the properties will be derived from single parent class to multiple class child class 
class Parent:
    gold = '2kg'
    silver = '10kg'
    no_of_flats = 12

class SmallestBrother(Parent):
    name = 'Rickon'
class ElderBrother(Parent):
    my_name = 'Rob'
class Sister(Parent):
    sis_name = 'Sansa'
print(SmallestBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)

