from app.models.project import Project
from app.repositories.project_repository import ProjectRepository


class InMemoryProjectRepository(ProjectRepository):

    def __init__(self):
        self._projects: list[Project] = []


    def add(self, project: Project) -> None:
        if any(p.name == project.name for p in self._projects):
            raise ValueError("project with this name already exists")
        self._projects.append(project)


    def get_by_name(self, name: str) -> Project | None:
        return next((p for p in self._projects if p.name == name), None)


    def list_all(self) -> list[Project]:
        return list(self._projects)


    def remove(self, project: Project) -> None:
        self._projects.remove(project)