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
    
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM stops WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()

    
    @staticmethod
    def get_by_id(stop_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM stops WHERE id = ?', (stop_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Stop(row['name'], row['location'], row['id'])
        return None
    
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM stops')
        rows = cursor.fetchall()
        conn.close()
        return [Stop(row['name'], row['location'], row['id']) for row in rows]