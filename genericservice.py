
from abc import ABC,abstractmethod

# what services that we are going to offer to the end user
class GenericService(ABC): #CRUD --> create read update delete

    @abstractmethod     #what services
    def add_entity(self,entity):
        pass

    @abstractmethod
    def delete_entity(self,eid):
        pass

    @abstractmethod
    def get_entity(self,eid):
        pass

    @abstractmethod
    def get_all_entities(self):
        pass

    @abstractmethod
    def update_entities(self):
        pass
