
from entities.generic import Generic


class College(Generic):

    def __init__(self, clgid, clgnm, cladr):
        self.collegeId = clgid
        self.colelgeName = clgnm
        self.clgadr = cladr

