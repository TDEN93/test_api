import requests
import json

response = requests.get("http://127.0.0.1:5000/players")
players = response.json()


players_obj = []

count = 0

for key in players:
    players_obj.append(players[key])

total_meditation_of_team = 0

while count < len(players_obj):
    total_meditation_of_team += players_obj[count]["meditation_length"]
    # if(players_obj[count]["name"]) == "Tray":
        # if(players_obj[count]["meditation_length"] > 3):
        #     print("meditate less")
    count += 1


print(total_meditation_of_team / len(players_obj))