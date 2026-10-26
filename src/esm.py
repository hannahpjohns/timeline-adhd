import sqlite3


def create_table():
    conn = sqlite3.connect("data/esm.db")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS
        esm_responses(
        ping_id INTEGER PRIMARY KEY,
        ts TEXT,
        activity_top TEXT,
        activity_mid TEXT,
        activity_leaf TEXT,
        free_text TEXT,
        intended TEXT,
        duration TEXT);"""
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()