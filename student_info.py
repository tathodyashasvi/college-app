
from entities.prof_info import Person


class Student(Person):
    count = 1
    def __init__(self ,sid ,snm ,sag ,sfees,marks,year=1,sadr='Mumbai'):
        super().__init__(Student.count ,snm ,sag ,sadr)   #pers---init
        self.studFees = sfees
        self.marks = marks
        self.whichYear = year
        Student.count = Student.count + 1
