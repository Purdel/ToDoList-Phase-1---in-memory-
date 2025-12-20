from app.repositories.inmemory_project_repository import InMemoryProjectRepository
from app.services.project_service import ProjectService
from app.cli.console import Console


# wiring dependencies
repo = InMemoryProjectRepository()
project_service = ProjectService(repo)
console = Console(project_service)


# demo usage
project_service.create_project("test1", "testing")
project_service.create_project("test2", "testing again")


console.show_projects()


project_service.delete_project("test2")
console.show_projects()