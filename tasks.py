from __future__ import annotations
from date import Date
import os
from dotenv import load_dotenv
from typing import Optional

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
    _tag_generator = 0
    _ALLOWED_STATUSES = {"todo", "doing", "done"}

    def __init__(
        self,
        *,
        title: str,
        desc: str = "",
        deadline: Optional[Date] = None,
        status: str = "todo",
        proj_name: str = "",
    ):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if MAX_LEN_OF_TASK_TITLE is not None and len(title) > MAX_LEN_OF_TASK_TITLE:
            raise TypeError("max length of task title exceeded")

        if not isinstance(desc, str):
            raise TypeError("desc must be a string")
        if MAX_LEN_OF_TASK_DESC is not None and len(desc) > MAX_LEN_OF_TASK_DESC:
            raise TypeError("max length of task description exceeded")

        if status not in self._ALLOWED_STATUSES:
            raise TypeError("the status is invalid")

        if deadline is not None and not isinstance(deadline, Date):
            raise TypeError("deadline must be a Date instance or None")

        type(self)._tag_generator += 1
        self._tag = type(self)._tag_generator

        self._title = title
        self._desc = desc
        self._deadline = deadline
        self._status = status
        self._proj_name = proj_name

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str):
        if not isinstance(new_title, str):
            raise TypeError("title must be a string")
        if MAX_LEN_OF_TASK_TITLE is not None and len(new_title) > MAX_LEN_OF_TASK_TITLE:
            raise TypeError("max length of task title exceeded")
        self._title = new_title

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, new_desc: str):
        if not isinstance(new_desc, str):
            raise TypeError("desc must be a string")
        if MAX_LEN_OF_TASK_DESC is not None and len(new_desc) > MAX_LEN_OF_TASK_DESC:
            raise TypeError("max length of task description exceeded")
        self._desc = new_desc

    @property
    def deadline(self) -> Optional[Date]:
        return self._deadline

    @deadline.setter
    def deadline(self, new_deadline: Optional[Date]):
        if new_deadline is not None and not isinstance(new_deadline, Date):
            raise TypeError("deadline must be a Date instance or None")
        self._deadline = new_deadline

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str):
        if new_status not in self._ALLOWED_STATUSES:
            raise TypeError("the status is invalid")
        self._status = new_status

    @property
    def proj_name(self) -> str:
        return self._proj_name

    @proj_name.setter
    def proj_name(self, new_proj_name: str):
        self._proj_name = str(new_proj_name)

    @property
    def tag(self) -> int:
        return int(self._tag)

    def __str__(self) -> None:
        return f"title: {self._title} -- description: {self._desc} -- deadline: {self._deadline} -- status: {self._status}"
    
    def show(self) -> None:
        print(str(self))