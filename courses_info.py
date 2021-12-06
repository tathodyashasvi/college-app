from entities.generic import Generic
class Course(Generic):

    def __init__(self,crid,crnm,crfees):
        self.courseId = crid
        self.courseName = crnm
        self.courseFees = crfees

