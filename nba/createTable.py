# script to connect to database & set up table properly

import sqlite3

def createConnection(databaseLocation):
    conn = None
    try:
        conn = sqlite3.connect(databaseLocation)
    except:
        print("Connection Error")
    return conn


def createTable(conn, tableSQL):
    try: 
        c = conn.cursor()
        c.execute(tableSQL)
    except:
        print("Table Error")

    

def main():
    databaseLocation = "../nba/stats.db"
    conn = createConnection(databaseLocation)

    tableSQL = """CREATE TABLE IF NOT EXISTS playerStats (
        id integer PRIMARY KEY,
        Player text NOT NULL,
        Active integer,
        GP integer,
        MPG real,
        FGM real,
        FGA real,
        FGP real,
        TPM real, 
        TPA real, 
        TPP real,
        FTM real,
        FTA real, 
        FTP real,
        TOV real,
        PF real,
        ORB real,
        DRB real,
        RPG real,
        APG real,
        SPG real,
        BPG real,
        PPG real

    );"""



    createTable(conn, tableSQL)

main()