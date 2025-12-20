from app.services.project_service import ProjectService


class Console:

    def __init__(self, project_service: ProjectService):
        self.project_service = project_service


    def show_projects(self):
        projects = self.project_service.list_projects()
        if not projects:
            print("you have no projects yet")
            return
        for p in projects:
            print(p)
            print("-------------")