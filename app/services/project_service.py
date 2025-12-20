from app.models.project import Project
from app.repositories.project_repository import ProjectRepository


class ProjectService:

    def __init__(self, repo: ProjectRepository):
        self.repo = repo


    def create_project(self, name: str, desc: str = "") -> Project:
        project = Project(name=name, desc=desc)
        self.repo.add(project)
        return project


    def list_projects(self) -> list[Project]:
        return self.repo.list_all()
    
    def delete_project(self, name: str) -> None:
        project = self.repo.get_by_name(name)
        if project is None:
            raise ValueError("project not found")
        self.repo.remove(project)