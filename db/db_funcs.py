def create_db(cur, conn):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            user_id INT PRIMARY KEY,
            organization TEXT,
            address TEXT,
            name TEXT,
            position TEXT,
            phone_number TEXT,
            model TEXT
        );
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS requests(
            id INT PRIMARY KEY,
            client_id INT,
            division TEXT,
            status TEXT,
            FOREIGN KEY(client_id) REFERENCES clients(user_id)
        ); 
    """)
    conn.commit()
    print("db created")


def is_user_registered(user_id: int, cur):
    cur.execute(f"SELECT user_id FROM clients WHERE user_id = {user_id}")
    if cur.fetchone():
        print("True")
        return True
    else:
        print("False")
        return False


async def insert_client(data, cur, conn):
    cur.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?);", data)
    conn.commit()
    print("registered")
