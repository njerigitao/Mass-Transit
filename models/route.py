from database.connection import get_db_connection

class Route:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO routes (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE routes SET name = ? WHERE id = ?', (self.name, self.id))
            conn.commit()
            conn.close()