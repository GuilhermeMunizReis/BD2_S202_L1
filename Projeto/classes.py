class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Member(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

class Chief(Person):
    def __init__(self, name, age, approval):
        super().__init__(name, age)
        self.approval = approval

class Clan():
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __inin__(self, member):
        self.members.append(member)