games = [ "Call of Duty", "Need for Speed", "Asphalt 8", "Soccer", "8 Pool" ]

choice = int(input("Enter the index of the game you want to play:" ))

if choice >= 0 and choice < len(games):
    print(games[choice])