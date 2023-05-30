import os
import requests
from dotenv import load_dotenv

load_dotenv()
STEAMAPIKEY = os.getenv("STEAMAPIKEY")
if not STEAMAPIKEY:
    STEAMAPIKEY = input("Skriv inn STEAMAPIKEY: ")

STEAMID = os.getenv("STEAMID")
if not STEAMID:
    STEAMID = input("Skriv inn STEAMID: ")

STEAMGRIDAPIKEY = os.getenv("STEAMGRIDAPIKEY")
if not STEAMGRIDAPIKEY:
    STEAMGRIDAPIKEY = input("Skriv inn STEAMGRIDAPIKEY: ")

def getSteamNumericUserID():
    userdataDir = "C:\\Program Files (x86)\\Steam\\userdata"
    subfolders = os.listdir(userdataDir)

    if len(subfolders) == 1:
        return subfolders[0]
    else:
        return subfolders[0]

def getSteamUserID():
    steamDir = "C:\\Program Files (x86)\\Steam"
    configPath = os.path.join(steamDir, "config", "config.vdf")

    with open(configPath, 'r') as file:
        configData = file.read()

    userIDStart = configData.find('"SteamID"') + len('"SteamID"')
    userIDEnd = configData.find('\n', userIDStart)
    userID = configData[userIDStart:userIDEnd].strip().strip('"')

    return userID

def getUserGames(userid):    
    response = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + STEAMAPIKEY + "&steamid=" + str(userid) + "&format=json")
    listOfAppIds = []
    for game in response.json()["response"]["games"]:
        listOfAppIds.append(game["appid"])
    return listOfAppIds

def doesPosterExist(appid):
    url="https://steamcdn-a.akamaihd.net/steam/apps/" + str(appid) + "/library_600x900_2x.jpg"
    
    print("Checking item with appid: " + str(appid))
    httpStatusResponse = requests.get(url)   

    return httpStatusResponse.status_code

def getSteamGridId(appid):
    config = {
        'authorization': 'Bearer ' + STEAMGRIDAPIKEY,
    }
    steamGridId = requests.get("https://www.steamgriddb.com/api/v2/games/steam/" + str(appid), headers=config)
    if(steamGridId.status_code == 200):
        data = steamGridId.json()
        
        return data["data"]["id"]

def getPoster(appid):
    config = {
        'authorization': 'Bearer ' + STEAMGRIDAPIKEY,
    }
    data = requests.get("https://www.steamgriddb.com/api/v2/grids/game/" + str(getSteamGridId(appid)), headers=config)
    data = data.json()

    if data != {}:
        if data.get('data'):
            if len(data['data']) > 0:
                poster = requests.get(str(data['data'][0]['url']))
                
                if poster.status_code == 200:
                    filename = "C:\\Program Files (x86)\\Steam\\userdata\\" + str(getSteamNumericUserID()) +"\\config\\grid\\" +  str(appid) + "p.png"
                    with open(filename, 'wb') as file:
                        file.write(poster.content)
                    print("Image downloaded and saved successfully.")
                else:
                    print("Failed to download the image.")
            else:
                print("No data available for the given appid.")
        else:
            print("Invalid response from the API.")
    else:
        print("Empty response from the API.")

def main(index = 0):
    listOfGames = getUserGames(STEAMID)
    
    if (index != 0):
        index = listOfGames.index(index) #Use to recover after crash. Enter last checked appid, and the script will continue from there.
        listOfGames = listOfGames[index+1:]

    for game in listOfGames:
        if doesPosterExist(game) != 200:
            getPoster(game)                           
        else:
            print("Poster already exists for game with appid: " + str(game))

main() #To recover from crash. Enter last checked appid as parameter, and the script will continue from there.