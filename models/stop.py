from database.connection import get_db_connection

class Stop:
    def __init__(self, name, location, id=None):
        self.id =id
        self.name = name
        self.location = location
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO stops (name, location) VALUES (?, ?)',
                           (self.name, self.location))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE stops SET name = ?, location = ? WHERE id =?',
                           (self.name, self.location, self.id))
            conn.commit()
            conn.close()
    
    