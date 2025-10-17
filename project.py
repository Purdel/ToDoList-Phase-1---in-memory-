from .tasks import Task

class Project:

    def __init__ (self, name: str):
        self._name = name
        self._desc = ""
        self._tasks: list[Task] = []

    @property
    def name (self):
        return str(self._name)
    
    @name.setter
    def name (self, new_value: str):
        self._name = str(new_value)

    @property
    def desc (self):
        return str(self._desc)
    
    @desc.setter
    def desc (self, new_desc: str):
        self._desc = str(new_desc)

    @property
    def task (self):
        return list(self._tasks)
    
    @task.setter
    def task (self, tasks: list[Task]):

#       if not isinstance(task, list[Task]):
#           raise TypeError("add_task expects a Task instance")
# not sure what am i doing with the if statement here. but i know
# it's wrong in this way
        
        self._tasks = list(tasks)

    def remove_proj (self): 
        ...
        # to perform a cascade delete, this method
        # first remove the project from the project list and then
        # remove every task related to the deleted project from the
        # tasks list.
        # i think i should make a separated file and store the list
        # of all the Project instances/ Task instances.

    def add_task (self, task: Task):
        self._tasks.append(task)

    def remove_task (self, task: Task):
        self._tasks.remove(task)