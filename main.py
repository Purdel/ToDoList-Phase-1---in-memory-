# testing some of the features

from project import Project
from tasks import Task
import project_util as util
from date import Date

proj1 = Project(name = "test1", desc = "testing")
proj2 = Project(name = "test2", desc = "testing again")
util.add_project(proj1)
util.add_project(proj2)

# testing

date1 = Date(day = 7, month = 8, year = 1404)
task1 = Task(title = "task1", desc = "first task", deadline = date1)

proj1.add_task(task1)
proj1.show()

proj1.show_tasks()

util.project_show()
util.remove_project("test2")
util.project_show()