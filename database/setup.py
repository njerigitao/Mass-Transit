from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            route_id INTEGER,
            stop_id INTEGER,
            time TEXT NOT NULL,
            FOREIGN KEY (route_id) REFERENCES routes (id),
            FOREIGN KEY (stop_id) REFERENCES stops (id)
        )
    ''')

    conn.commit()
    conn.close()
