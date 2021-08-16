
# RUN WITH PYTHON3!!!!!!!!!!!!!!!!!!!!!!!!!

# function to get a player's ID by providing their name
from nba_api.stats.static import players
def getPlayerID(playerName):
    playerList = players.find_players_by_full_name(playerName)
    print(playerList[0])
    playerID = playerList[0].get("id")
    print(playerID)
    return playerID
# playerName = "LeBron James"


# function which writes a players complete game log to a CSV
# we can then take that CSV and parse it by season to get the averages
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import matplotlib.pyplot as plt
def getCareerGameStats(playerName, playerID):
    # pd.set_option("display.max_rows", None, "display.max_columns", None)

    completeGamelog = playergamelog.PlayerGameLog(player_id=playerID, season = SeasonAll.all)
    completeCareerDataFrame = completeGamelog.get_data_frames()[0]
    completeCareerDataFrame

    relativePath = "./"
    filename = relativePath + playerName + '.csv'
    completeCareerDataFrame.to_csv(filename)

    # get a list of each season the player has played (and a count of seasons)
    # to do so, parse through CSV and get unique season IDs
    # reverse this list so it becomes chronological
    # then get the season averages of each stat category for that season
    # store this as a dictionary
    # then graph the data
    seasonsPlayed = []
    seasonCount = 0

    df = pd.read_csv(filename)
    seasonCol = df.SEASON_ID
    for season in seasonCol:
        if season not in seasonsPlayed:
            seasonsPlayed.append(season)
            seasonCount += 1

    seasonsPlayed.reverse()
    seasonAverages = {}
    count = 0
    for season in seasonsPlayed:
        count += 1
        totalPoints = 0
        totalAssists = 0
        totalRebounds = 0
        gameCount = 0
        for index, row in df.iterrows():
            if row["SEASON_ID"] == season:
                totalPoints += row["PTS"]
                totalAssists += row["AST"]
                totalRebounds += row["REB"]
                gameCount += 1
        PTS = round(totalPoints / gameCount, 1)
        AST = round(totalAssists / gameCount, 1)
        REB = round(totalRebounds / gameCount, 1)
        tempList = [season, PTS, AST, REB]
        seasonAverages[count] = tempList
    # print(seasonAverages)

    seasons = seasonAverages.keys()
    points = []
    for key in seasons:
        points.append(seasonAverages.get(key)[1])
    # print(seasons)
    # print(points)
    plt.plot(seasons, points, label="Points")
    plt.show()

    


def main():
    
    playerName = "Ben Simmons"
    playerID = getPlayerID(playerName)
    getCareerGameStats(playerName, playerID)



main()