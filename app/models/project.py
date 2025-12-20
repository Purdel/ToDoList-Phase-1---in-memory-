import os
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
    def __init__(self, *, name: str, desc: str = ""):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.id: int | None = None # will be set by DB later
        self.name = name
        self.desc = desc


    def __str__(self) -> str:
        return f"Project(id={self.id}, name={self.name}, desc={self.desc})"