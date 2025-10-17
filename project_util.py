from project import Project
from tasks import Task
import os
from dotenv import load_dotenv, dotenv_values
project_list = []
project_name_list = []

# loading environment variables
MAX_LEN_OF_PROJ_DESC = os.getenv("MAX_LEN_OF_PROJ_DESC")
MAX_NUMBER_OF_PROJECTS = os.getenv("MAX_NUMBER_OF_PROJECTS")

def find_project(project: str):
    for proj in project_list:
        if proj.name() == project:
            return proj
    return None

def add_project(project: Project):
    if project_list.len() == MAX_NUMBER_OF_PROJECTS:
        raise TypeError("max number of projects reached")
    
    if project.name() in project_name_list:
        raise TypeError("a project with this name already exists")
    
    project_list.append(project)
    project_name_list.append(project.name())

def remove_project(project: str):
    if project not in project_name_list:
        raise TypeError("project not found for delete operation")
    
    project_to_delete = find_project(project)
    project_to_delete.remove_all_tasks()
    project_list.remove(project_to_delete)
    project_name_list.remove(project)

def edit_name(project: Project, new_name: str):
    if new_name in project_name_list:
        raise TypeError("a project with this name already exists")
    
    project.name(new_name)

    # delete the task list of the project before deleting the task itself for a cascade delete