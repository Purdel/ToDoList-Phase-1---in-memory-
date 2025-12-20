from abc import ABC, abstractmethod
from app.models.project import Project


class ProjectRepository(ABC):


@abstractmethod
def add(self, project: Project) -> None: ...


@abstractmethod
def get_by_name(self, name: str) -> Project | None: ...


@abstractmethod
def list_all(self) -> list[Project]: ...


@abstractmethod
def remove(self, project: Project) -> None: ...