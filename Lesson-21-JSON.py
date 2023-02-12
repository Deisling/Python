





import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin=1')


player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]   
}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'Awards': ["WI", "TX", "MI"]   
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

 # -------------- SAVE by JSON ---------------

json.dump(myplayers, myfile)
myfile.close()


# --------- LOAD by JSON -------------------

myfile = open(filename, mode='r', encoding='Latin-1')
json_moyainformaziya = json.load(myfile)

for user in json_moyainformaziya:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award N1: " + str(user['Awards'][0]))
    print("Player Award N2: " + str(user['Awards'][1]))
    print("Player Award N2: " + str(user['Awards'][2]))
    print("------------------------------------------\n\n")



