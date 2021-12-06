from entities.generic import Generic


class Dept(Generic):

    def __init__(self,did,dtnm):
        self.deptCode = did
        self.deptName = dtnm
