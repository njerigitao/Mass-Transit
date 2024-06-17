from database.connection import get_db_connection

class Route:
    def __init__(self, name, start_location, end_location, id=None):
        self.id = id
        self.name = name
        self.start_location = start_location
        self.end_location = end_location
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO routes (name, start_location, end_location) VALUES (?, ?, ?)',
                            (self.name, self.start_location, self.end_location))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE routes SET name = ?, start_location = ?, end_location = ? WHERE id = ?',
                            (self.name, self.start_location, self.end_location, self.id))
            conn.commit()
            conn.close()

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM routes WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_by_id(route_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM routes WHERE id = ?', (route_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Route(row['name'], row['start_location'], row['end_location'], row['id'])
        return None
    
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM routes')
        rows = cursor.fetchall()
        conn.close()
        return [Route(row['name'], row['start_location'], row['end_location'], row['id']) for row in rows]