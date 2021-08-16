import xlrd
import sqlite3
import re

def createConnection(databaseLocation):
    conn = None
    try:
        conn = sqlite3.connect(databaseLocation)
    except Error as e:
        print(e)
    return conn
 

def commitExcelData(excelLocation, conn):

    # open workbook by using workbook location
    wb = xlrd.open_workbook(excelLocation)
    sheet = wb.sheet_by_index(0)


    # iterate through workbook & assign data to variables
    for row in range(1, sheet.nrows):
        ID = sheet.cell_value(row, 0)
        player = sheet.cell_value(row, 1)
        active = 0
        # determine if the player is active based on if they have a "*" at the end of their name
        if (re.search(".*\*", player) != None):
            active = 1
            player = player[:-2]
        gp = sheet.cell_value(row, 3)
        mpg = sheet.cell_value(row, 4)
        fgm = sheet.cell_value(row, 5)
        fga = sheet.cell_value(row, 6)
        fgp = sheet.cell_value(row, 7)
        tpm = sheet.cell_value(row, 8)
        tpa = sheet.cell_value(row, 9)
        tpp = sheet.cell_value(row, 10)
        ftm = sheet.cell_value(row, 11)
        fta = sheet.cell_value(row, 12)
        ftp = sheet.cell_value(row, 13)
        tov = sheet.cell_value(row, 14)
        pf = sheet.cell_value(row, 15)
        orb = sheet.cell_value(row, 16)
        drb = sheet.cell_value(row, 17)
        rpg = sheet.cell_value(row, 18)
        apg = sheet.cell_value(row, 19)
        spg = sheet.cell_value(row, 20)
        bpg = sheet.cell_value(row, 21)
        ppg = sheet.cell_value(row, 22)

        print("Player: " + player + ", PPG: " + str(ppg))

        data = (ID, player, active, gp, mpg, fgm, fga, fgp, tpm, tpa, tpp, ftm, fta, ftp, tov, pf, orb, drb, rpg, apg, spg, bpg, ppg)
        
        insertSQL = '''INSERT INTO playerStats(id, Player, Active, GP, MPG, FGM, FGA, FGP, TPM, TPA, TPP, FTM, FTA, FTP, TOV, PF, ORB, DRB, RPG, APG, SPG, BPG, PPG)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        c = conn.cursor()
        c.execute(insertSQL, data)
        conn.commit()
    print("Commit Successful")


def main():
    excelLocation = "../nba/allPlayers2021.xls"
    databaseLocation = "../nba/stats.db"

    conn = createConnection(databaseLocation)
    commitExcelData(excelLocation, conn)



main()
