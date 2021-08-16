# script to connect to database & set up table properly
import sqlite3

def createConnection(databaseLocation):
    conn = None
    try:
        conn = sqlite3.connect(databaseLocation)
    except Error as e:
        print(e)
    return conn


def clearTable(conn, clearStatement):
    try: 
        cur = conn.cursor()
        cur.execute(clearStatement)
        conn.commit()
    except:
        print("Table Error")

    

def main():
    databaseLocation = "../nba/stats.db"
    conn = createConnection(databaseLocation)

    clearStatement = "DELETE FROM playerStats"
    clearTable(conn, clearStatement)

main()