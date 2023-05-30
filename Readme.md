AutosteamGrid
=============

What is it?
-----------

AutoSteamGrid is a short Python script automating the process of setting posters to games that only have banners in your Steam library grid-view.
It has been tried on a library of 

Requirements
------------
Windows version of Steam
SteamGrid API key https://www.steamgriddb.com/profile/preferences
Steam API Key https://steamcommunity.com/dev/apikey
Your Steam id

Usage
-----
To use this script, you need to suply three variables: 
- Your Steam api key. If you don't have one, get it at: 
- Your Steam api key. If you don't have one, get it at: 
- Your Steam ID 

You may put these variables in an .env-file like this:
    STEAMID=
    STEAMAPIKEY=""
    STEAMGRIDAPIKEY=""

If an .env is not found, you will have to enter when prompted.

If the script crashes you may enter the last checked id as a parameter when calling main on line 105.

Disclaimer
----------
Previously downloaded posters might be overwritten.