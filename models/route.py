from database.connection import get_db_connection

class Route:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name