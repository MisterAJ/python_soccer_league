import csv
import os

# Prevent code from running on import
if __name__ == "__main__":

    # Create list variables
    sharks = []
    dragons = []
    raptors = []

    newplayers = []
    expplayers = []

    with open('soccer_players.csv', newline='') as csvfile:
        soccer_reader = csv.DictReader(csvfile, delimiter=',')
        rows = list(soccer_reader)

        # Sort players between lists
        for row in rows:
            if row['Soccer Experience'] == 'YES':
                expplayers.append(row)
            else:
                newplayers.append(row)

    #   Sort players between teams
    for player in newplayers:
        min(sharks, dragons, raptors, key=len).append(player)

    for player in expplayers:
        min(sharks, dragons, raptors, key=len).append(player)

    # function to create the files
    def make_teams():
        teams = [[sharks, "Sharks"], [dragons, "Dragons"], [raptors, "Raptors"]]
        file = open("teams.txt", "w")
        if not os.path.exists("letters/"):
            os.makedirs("letters/")
        for team in teams:
            file.write(team[1] + "\n")
            for player in team[0]:
                # Create welcome letter
                player_letter = open("letters/" + '_'.join(player["Name"].split()) + ".txt", "w")
                player_letter.write(
                    'Dear ' + player["Guardian Name(s)"] + ",\n\n" +
                    "We would like to welcome " + player["Name"] +
                    ' to the ' + team[1] + '!\n' +
                    'The first practice will be July 7th at 5am.\n\n' +
                    'Players more than 10 minutes late will be flogged'
                )
                player_letter.close()

                # Append player to roster
                file.write(
                    player["Name"] + ", " +
                    player["Soccer Experience"] + ", " +
                    player["Guardian Name(s)"] + "\n"
                )
            file.write("\n")
        file.close()


    make_teams()
