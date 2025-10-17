from tasks import Task
import os
import gc
from dotenv import load_dotenv, dotenv_values

# loading environment variables
MAX_LEN_OF_PROJ_NAME = os.getenv("MAX_LEN_OF_PROJ_NAME")
MAX_LEN_OF_PROJ_DESC = os.getenv("MAX_LEN_OF_PROJ_DESC")
MAX_NUMBER_OF_PROJECTS = os.getenv("MAX_NUMBER_OF_PROJECTS")

class Project:

    def __init__ (self, name: str):
        if name.len() > MAX_LEN_OF_PROJ_NAME:
            raise TypeError("max length of a project name exceeded")
        
        self._name = name
        self._desc = ""
        self._tasks: list[Task] = []

    @property
    def name(self):
        return str(self._name)
    
    @name.setter
    def name(self, new_value: str):
        if new_value.len() > MAX_LEN_OF_PROJ_NAME:
            raise TypeError("max length of a project name exceeded")
        
        self._name = str(new_value)

    @property
    def desc(self):
        return str(self._desc)
    
    @desc.setter
    def desc(self, new_desc: str):
        if new_desc.len() > MAX_LEN_OF_PROJ_DESC:
            raise TypeError("max length of a project describtion exceeded")
        self._desc = str(new_desc)

    @property
    def task(self):
        return list(self._tasks)
    
    @task.setter
    def task(self, tasks: list[Task]):
        self._tasks = list(tasks)

    def add_task(self, task: Task):
        self._tasks.append(task)

    def remove_task(self, task: Task):
        self._tasks.remove(task)

    def remove_all_tasks(self):
        self._tasks.clear() # removes references to task objects
        gc.collect()