import sqlite3

def create_db():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
                    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    status TEXT DEFAULT 'open',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

def insert_ticket(user_id):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("INSERT INTO tickets (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_open_tickets():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tickets WHERE status = 'open'")
    tickets = c.fetchall()
    conn.close()
    return tickets

def close_ticket(ticket_id):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("UPDATE tickets SET status = 'closed' WHERE ticket_id = ?", (ticket_id,))
    conn.commit()
    conn.close()
