from app.db.database import Database

class BaseModel:
    def __init__(self):
        self.connection = Database.get_connection() 