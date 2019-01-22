class Student():
    def __init__ (self, name, type):
        self.name = name
        self.type = type #defines whether undergrad or grad
        #set up other attributes
        pass

    def apply():
        #student can apply to either university or college
        #create an university instance, specifying with univerisity of college it is
        pass

class Undergrad(Student):
    def __init__ (self):
        self.type = undergrad
        pass

class Grad(Student):
    pass

class University:
    def __init__(self):
        self.student = Student()

    def enroll_undergrad():
        #university can enroll only undergrads
        pass

class College(University):
    #enrolls grad students
    pass
