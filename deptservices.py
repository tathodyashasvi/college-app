

from services.genericservice import GenericService

from entities.dept_info import Dept
class DeptService(GenericService):
    deptList = []

    def add_entity(self, dept):
        if type(dept) == Dept:
            DeptService.add_entity(dept)
            print('Dept Added Successfully....')
        else:
            print('Invalid Dept Type')

    def delete_entity(self, did):
        pass

    def get_entity(self, did):
        pass

    def get_all_entities(self):
        pass

    def update_entities(self, did, values):
        pass