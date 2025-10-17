from tasks import Task
import os
import gc
from dotenv import load_dotenv

load_dotenv()

def _get_int_env(name: str, default: int) -> int:
    v = os.getenv(name)
    try:
        return int(v) if v is not None else default
    except (TypeError, ValueError):
        return default

MAX_LEN_OF_PROJ_NAME = _get_int_env("MAX_LEN_OF_PROJ_NAME", 30)
MAX_LEN_OF_PROJ_DESC = _get_int_env("MAX_LEN_OF_PROJ_DESC", 150)
MAX_NUMBER_OF_PROJECTS = _get_int_env("MAX_NUMBER_OF_PROJECTS", 10)
MAX_NUMBER_OF_TASKS = _get_int_env("MAX_NUMBER_OF_TASKS", 100)

class Project:
    _tag_generator = 0

    def __init__(self, *, name: str, desc: str = "", tasks: list[Task] | None = None):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) > MAX_LEN_OF_PROJ_NAME:
            raise TypeError("max length of a project name exceeded")

        type(self)._tag_generator += 1
        self._tag = type(self)._tag_generator

        self._name = name
        self._desc = desc
        # avoid mutable default
        self._tasks: list[Task] = list(tasks) if tasks is not None else []

    @property
    def tag(self) -> int:
        return self._tag

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_value: str):
        if not isinstance(new_value, str):
            raise TypeError("name must be a string")
        if len(new_value) > MAX_LEN_OF_PROJ_NAME:
            raise TypeError("max length of a project name exceeded")
        self._name = new_value

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, new_desc: str):
        if not isinstance(new_desc, str):
            raise TypeError("desc must be a string")
        if len(new_desc) > MAX_LEN_OF_PROJ_DESC:
            raise TypeError("max length of a project description exceeded")
        self._desc = new_desc

    @property
    def tasks(self) -> list[Task]:
        # return a shallow copy to protect internal list
        return list(self._tasks)

    @tasks.setter
    def tasks(self, tasks: list[Task]):
        if not isinstance(tasks, (list, tuple)):
            raise TypeError("tasks must be a list or tuple of Task instances")
        if not all(isinstance(t, Task) for t in tasks):
            raise TypeError("all elements of tasks must be Task instances")
        self._tasks = list(tasks)

    def find_task(self, tag: int) -> Task | None:
        for task in self._tasks:
            if getattr(task, "tag", None) == tag:
                return task
        return None

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("add_task expects a Task instance")
        if MAX_NUMBER_OF_TASKS is not None and len(self._tasks) >= MAX_NUMBER_OF_TASKS:
            raise TypeError("max number of tasks for this project reached")
        self._tasks.append(task)

    def remove_task(self, task: Task):
        try:
            self._tasks.remove(task)
        except:
            print("something went wrong")
        else:
            print("task deleted successfully")
            
    def remove_task_by_tag(self, tag: int):
        the_task = self.find_task(tag)
        if the_task is None:
            print("the task was not found")
            return
        return self.remove_task(the_task)

    def remove_all_tasks(self):
        self._tasks.clear()
        gc.collect()

    def __str__(self) -> str:
        return f"tag: {self._tag} -- name: {self._name} -- description: {self._desc}"

    def show(self) -> None:
        if self == None:
            print("no project found")
            return None

        print(str(self))

    def show_tasks(self) -> None:
        if self == None:
            print("no project found")
            return None
        
        for task in self._tasks:
                task.show()
                print("-------------")
        
    