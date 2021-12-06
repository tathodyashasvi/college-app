

from services.genericservice import GenericService
from entities.student_info import *

def sort_by(stud):
    return stud.agrmarks

class StudentService(GenericService):
    studentList = []

    def add_entity(self, stud):             #instance --> method --> Object--> StudentServices
        if type(stud)==Student:
            StudentService.studentList.append(stud)
            print('Student Added Successfully....!')
        else:
            print('Invalid Student Type..')

    def delete_entity(self, sid):
        for stud in StudentService.studentList:
            if stud.personId == sid:
                StudentService.studentList.remove(stud)
                print('Student Record removed...!')
                return

        print('No Student with Given Id found..!')


    def get_entity(self, sid):  #search on the basis of ID
        for stud in StudentService.studentList:
            if stud.personId == sid:
                return stud

        print('No STudent WIth Given Id..!')

    def get_all_entities(self):
        return StudentService.studentList

    def update_entities(self,sid,values):
        pass

    def find_topper(self):
        for stud in StudentService.studentList:
            marks = stud.marks
            if marks.physics>=40 and marks.chemestry>=40 and marks.mathamatics>=40:
                sum = marks.physics + marks.chemestry + marks.mathamatics
                stud.agrmarks = sum
            else:
                stud.agrmarks = 0


        StudentService.studentList.sort(key=sort_by,reverse=True)

        topper = StudentService.studentList[0]   # topper ---> sure shot..

        topperList = [topper]
        for stud in StudentService.studentList[1::]:
            if stud.agrmarks==topper.agrmarks:
                topperList.append(stud)
            else:
                break

        return topperList

        '''
        max_marks = 0
        topper = None
        for stud in StudentService.studentList:
            if stud.agrmarks>=max_marks:  #262>262
                max_marks = stud.agrmarks
                topper = stud
        return topper
        '''

    def get_max_fees_paid_student(self):
        max_fees = 0.0          #55
        student = None          #s1
        for stud in StudentService.studentList:     #[s1:55,s2:33,s3:66,s4:3,s5:35]
            if stud.whichYear==3 and stud.studFees>max_fees:
                max_fees = stud.studFees
                student  = stud
        return student



from entities.marks_info import Marks
if __name__ == '__main__':
    studService = StudentService()
    s1 = Student(sid=101 ,snm='AAAA1' ,sag=23 ,sadr='Pune' ,sfees=5299.23,marks=Marks(phy=67,chem=46,math=59),year=1)
    s2 = Student(sid=102, snm='AAAA2', sag=23, sadr='Pune', sfees=29894.23,marks=Marks(phy=87,chem=88,math=18),year=1)
    s3 = Student(sid=103, snm='AAAA3', sag=23, sfees=96495.23,marks=Marks(phy=97,chem=64,math=59),year=2)
    s4 = Student(sid=104, snm='AAAA4', sag=23, sadr='Chennai', sfees=2969.23,marks=Marks(phy=91,chem=94,math=77),year=4)
    s5 = Student(sid=105, snm='AAAA1', sag=23, sadr='Pune', sfees=54299.23,marks=Marks(phy=77,chem=37,math=79),year=4)
    s6 = Student(sid=106, snm='AAAA2', sag=23, sadr='Pune', sfees=72994.23,marks=Marks(phy=57,chem=33,math=59),year=3)
    s7 = Student(sid=107, snm='AAAA3', sag=23, sfees=6299495.23,marks=Marks(phy=91,chem=94,math=77),year=2)
    s8 = Student(sid=108, snm='AAAA4', sag=23, sadr='Pune', sfees=24969.23,marks=Marks(phy=93,chem=54,math=35),year=3)
    studService.add_entity(s1)
    studService.add_entity(s2)
    studService.add_entity(s3)
    studService.add_entity(s4)
    studService.add_entity(s5)
    studService.add_entity(s6)
    studService.add_entity(s7)
    studService.add_entity(s8)

    stud = studService.get_max_fees_paid_student()
    print(stud)
    import sys
    sys.exit(0)
    topper = studService.find_topper()
    print(studService.get_all_entities())
    print('--------')
    print(topper)
    #print(studService.get_all_entities())

    import sys
    sys.exit(0)

    students = studService.get_all_entities()
    print(students)

    studService.delete_entity(1023)

    students = studService.get_all_entities()
    print(students)

    print('----------------')
    stud  = studService.get_entity(103)
    print(stud)
    print('max-fees paid---')
    student = studService.get_max_fees_paid_student()
    print(student)