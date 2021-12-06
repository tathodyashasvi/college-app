from entities.generic import Generic

class Person(Generic):

    def __init__(self,pid,pnm,pag,padr):
        self.personId = pid
        self.personName = pnm
        self.personAge = pag
        self.personAddress = padr


class Professor(Person):

    def __init__(self,pid,pnm,pag,padr,exp,salary):
        super().__init__(pid,pnm,pag,padr)      # super()-->person-init
        self.experience = exp
        self.salary = salary


