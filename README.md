# BAND BAAJA BAARAT

- An api that give information to plan a wedding in any city.
- This provides wedding halls, tents , catering information.
- Also the wedding halls are sorted in distance from your locality.
- It also provide user authentication through tokens

## LIBRARIES USED
- BEAUTIFUL SOUP for web scraping.
- UUID to generate random numbers.
- SQLITE3 to create databse and sql files.
- FLASK to host the api on a local server.

## Scripts and their functions-

**catering**
Takes in city and finds out all the caters in that city and finally write those data in database.

**creatingtable**
This creates tables and the file of the database. Have to run just one time to create those tables.

**distance**
script finds out the distance between 2 localities in a city.

**halls_with_lawns**
Takes in city and locality to get data of halls with lawns situated in that city in a sorted order of distance and finally write those data in database.

**halls_without_lawns**
Takes in city and locality to get data of halls without lawns situated in that city in a sorted order of distance and finally write those data in database.

**server_api**
integrates the api server to the localhost and checking if the data exist in the database or not.

**tents**
Takes in city and locality and finds the tents available in that city and finally write those data in database.

**weather**
interactive program to find out weather in the near 15 days.



    
