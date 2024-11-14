import sqlite3

def create_database():
    conn = sqlite3.connect('hall_ticket_booking.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            event_name TEXT NOT NULL,
            date TEXT NOT NULL,
            seats INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    conn.commit()
    conn.close()

def add_user(name, email):
    conn = sqlite3.connect('hall_ticket_booking.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

def add_booking(user_id, event_name, date, seats):
    conn = sqlite3.connect('hall_ticket_booking.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bookings (user_id, event_name, date, seats) VALUES (?, ?, ?, ?)', (user_id, event_name, date, seats))
    conn.commit()
    conn.close()

def get_booking_analysis():
    conn = sqlite3.connect('hall_ticket_booking.db')
    cursor = conn.cursor()
    cursor.execute('SELECT event_name, SUM(seats) FROM bookings GROUP BY event_name')
    data = cursor.fetchall()
    conn.close()
    return data