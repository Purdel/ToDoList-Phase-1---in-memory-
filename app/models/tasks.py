from __future__ import annotations
import os
from dotenv import load_dotenv
from datetime import date


load_dotenv()

def _get_int_env(name: str, default: int) -> int:
    v = os.getenv(name)
    try:
        return int(v) if v is not None else default
    except (TypeError, ValueError):
        return default

# sensible defaults
MAX_LEN_OF_TASK_TITLE = _get_int_env("MAX_LEN_OF_TASK_TITLE", 50)
MAX_LEN_OF_TASK_DESC = _get_int_env("MAX_LEN_OF_TASK_DESC", 200)


class Task:
    _ALLOWED_STATUSES = {"todo", "doing", "done"}


    def __init__(
        self,
        *,
        title: str,
        desc: str = "",
        deadline: date | None = None,
        status: str = "todo",
    ):
        if status not in self._ALLOWED_STATUSES:
            raise ValueError("invalid status")


        self.id: int | None = None # DB primary key
        self.project_id: int | None = None # FK to Project
        self.title = title
        self.desc = desc
        self.deadline = deadline
        self.status = status


    def __str__(self) -> str:
        return f"Task(id={self.id}, title={self.title}, status={self.status})"