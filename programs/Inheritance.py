'''
Inheritance
parent
child
'''
class Parent():

    def profession(self):
        return "Doctor"

    def whoAmI(self):
        return "parent"
'''
inheritance
'''
class Child(Parent):

    def hobby(self):
        return "Singing"

    def whoAmI(self):
        return "Child"

parent1 = Parent()
print("whoami on parent" ,parent1.whoAmI())

child1 = Child()
'''
Child is inheriting parent method
'''
print('child profession ' ,child1.profession())
'''
overriding
'''
print('child whoami ' ,child1.whoAmI())


