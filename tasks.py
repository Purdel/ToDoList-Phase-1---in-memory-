class Task:

    def __init__ (self, title: str, desc: str, deadline: str):
        self._title = title
        self._desc = desc
        self._deadline = deadline 
        self._status = "todo"
        self._proj_name = ""

    @property
    def title (self):
        return self._title

    @title.setter
    def title (self, new_title):
        self._title = new_title

    # getter / setter for desc
    @property
    def desc (self):
        return self._desc

    @desc.setter
    def desc (self, new_desc):
        self._desc = new_desc

    # getter / setter for deadline
    @property
    def deadline (self):
        return self._deadline

    @deadline.setter
    def deadline (self, new_deadline):
        self._deadline = new_deadline

    # getter / setter for status
    @property
    def status (self):
        return self._status

    @status.setter
    def status (self, new_status):
        self._status = new_status

    # getter / setter for proj_name which is not supposed to be used.
    @property
    def proj_name (self):
        return self._proj_name
    
    @proj_name.setter
    def proj_name (self, new_proj_name):
        self._proj_name = new_proj_name