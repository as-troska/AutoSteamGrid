AutoSteamGrid
=============

What is it?
-----------

AutoSteamGrid is a short Python script automating the process of setting posters to games that only have banners in your Steam library grid-view.
It has been tried on a library of about 3000. Please note that the script takes quite some time to finish when dealing with libraries of these sizes. Your results should be visible in your Steam library as the script is running.

Requirements
------------
- Windows version of Steam  
- SteamGrid API key  
- Steam API Key  
- Your Steam id
- doten library. Install with pip install python-dotenv

Usage
-----
To use this script, you need to suply three variables:  
- Your Steam api key. If you don't have one, get it at: https://www.steamgriddb.com/profile/preferences  
- Your Steam api key. If you don't have one, get it at: https://steamcommunity.com/dev/apikey  
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