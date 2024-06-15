from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_location TEXT NOT NULL,
            end_location TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            route_id INTEGER NOT NULL,
            stop_id INTEGER NOT NULL,
            arrival_time TEXT NOT NULL,
            departure_time TEXT NOT NULL,
            FOREIGN KEY (route_id) REFERENCES routes (id),
            FOREIGN KEY (stop_id) REFERENCES stops (id)
        )
    ''')

    conn.commit()
    conn.close()
