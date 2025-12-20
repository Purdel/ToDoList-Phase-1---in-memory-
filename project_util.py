from app.models.project import Project
import os
from dotenv import load_dotenv

load_dotenv()

def _get_int_env(name: str, default: int) -> int:
    v = os.getenv(name)
    try:
        return int(v) if v is not None else default
    except (TypeError, ValueError):
        return default

# configuration
MAX_LEN_OF_PROJ_DESC = _get_int_env("MAX_LEN_OF_PROJ_DESC", 150)
MAX_NUMBER_OF_PROJECTS = _get_int_env("MAX_NUMBER_OF_PROJECTS", 10)

# shared storage
project_list: list[Project] = []
project_name_list: list[str] = []

def find_project(name: str) -> Project | None:
    for proj in project_list:
        if proj.name == name:
            return proj
    return None

def add_project(project: Project) -> None:
    if MAX_NUMBER_OF_PROJECTS is not None and len(project_list) >= MAX_NUMBER_OF_PROJECTS:
        raise TypeError("max number of projects reached")

    if project.name in project_name_list:
        raise TypeError("a project with this name already exists")
    
    # using something like insertion sort to keep the project list 
    # sorted by tag
    idx = None
    for i in range(0, len(project_list)):
        if project_list[i].tag >  project.tag:
            idx = i
            break

    if idx is None:
        project_list.append(project)
        project_name_list.append(project.name)
    else:
        project_list.insert(idx, project)
        project_name_list.insert(idx, project.name)


def remove_project(name: str) -> None:
    if name not in project_name_list:
        raise TypeError("project not found for delete operation")

    project_to_delete = find_project(name)
    if project_to_delete is None:
        raise TypeError("project not found for delete operation")

    project_to_delete.remove_all_tasks()
    project_list.remove(project_to_delete)
    project_name_list.remove(name)

def edit_name(project: Project, new_name: str) -> None:
    if new_name in project_name_list:
        raise TypeError("a project with this name already exists")

    old_name = project.name
    project.name = new_name

    # keep project_name_list in sync
    try:
        idx = project_name_list.index(old_name)
        project_name_list[idx] = new_name
    except ValueError:
        project_name_list.append(new_name)

def project_show() -> None:
    if len(project_list) == 0:
        print("you have no projects yet")
        return

    for proj in project_list:
        proj.show()
        print("-------------")

