
class Student:
    count = 100

    def __init__(self ,sid ,snm ,sag ,sfees,phy,chem,math,gen,sadr='Mumbai'):
        Student.count = Student.count + 1
        self.studId = sid
        self.studName = snm
        self.studAge = sag
        self.studFees = sfees
        self.studGender = gen
        self.studMarks = {"PHY":phy,"CHEM":chem,"MATH":math}
        self.studAddress = sadr

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)

from abc import ABC,abstractmethod
class StudentServices(ABC):

    @abstractmethod
    def add_new_student(self,stud):
        pass

    @abstractmethod
    def get_student(self, stud):
        pass

    @abstractmethod
    def get_all_student(self, stud):
        pass


    @abstractmethod
    def find_first_three_toppers(self, stud):
        pass


    @abstractmethod
    def find_failed_candidates(self, stud):
        pass


    @abstractmethod
    def find_pass_candidates(self, stud):
        pass


    @abstractmethod
    def find_topper_basedon_subj(self, stud):
        pass


    @abstractmethod
    def find_failed_students_basedon_subj(self, stud):
        pass


    @abstractmethod
    def find_specific_location_students(self, stud):
        pass


    @abstractmethod
    def find_total_fees_collection(self, stud):
        pass


    @abstractmethod
    def find_topper_basedon_gender(self, stud):
        pass


    @abstractmethod
    def find_max_fees(self, stud):
        pass


    @abstractmethod
    def find_avg_fees(self, stud):
        pass


class StudentServiceImpl(StudentServices):

    def add_new_student(self, stud):
        pass

    def get_student(self, stud):
        pass

    def get_all_student(self, stud):
        pass

    def find_first_three_toppers(self, stud):
        pass

    def find_failed_candidates(self, stud):
        pass

    def find_pass_candidates(self, stud):
        pass

    def find_topper_basedon_subj(self, stud):
        pass

    def find_failed_students_basedon_subj(self, stud):
        pass

    def find_specific_location_students(self, stud):
        pass

    def find_total_fees_collection(self, stud):
        pass

    def find_topper_basedon_gender(self, stud):
        pass

    def find_max_fees(self, stud):
        pass

    def find_avg_fees(self, stud):
        pass

if __name__ == '__main__':
    serviceImpl = StudentServiceImpl()
    pass