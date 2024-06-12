from database.connection import get_db_connection
from models.route import Route
from models.stop import Stop

class Schedule:
    def __init__(self, route_id, stop_id, arrival_time, departure_time, id=None):
        self.id = id
        self.route_id = route_id
        self.stop_id = stop_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO schedules (route_id, stop_id, arrival_time, departure_time)
                VALUES (?, ?, ?, ?) ''',
                 (self.route_id, self.stop_id, self.arrival_time, self.departure_time))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE schedules
                SET route_id = ?, stop_id = ?, arrival_time = ?, departure_time = ?
                WHERE id = ?''',
                 (self.route_id, self.stop_id, self.arrival_time, self.departure_time, self.id))
        conn.commit()
        conn.close()