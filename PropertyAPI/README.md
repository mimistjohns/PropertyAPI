#Property API
This program takes data on properties for sale in San Francisco, 
and sorts by days on the market, price, and beds. 
##Dependencies
- pandas
- flask
- sqlite3
- sqlalchemy

##Instructions 
1. Run application.py to run local host. 

2. Enter local URL in browser. The home endpoint is all properties in ascending order of "Days on Market." 

3. Enter query; this program sorts by ascending and descending price,
beds, and baths. It also can sort by the minimum or maximum of a field.  
Example Queries: 

`http://127.0.0.1:5000/address/738-740%20North%20Point%20St`

`http://127.0.0.1:5000/address/1156-1158%20Church%20St`

`http://127.0.0.1:5000/sorted/Price/asc`

`http://127.0.0.1:5000/sorted/BEDS/desc`

`http://127.0.0.1:5000/sorted/BATHS/asc?baths_min=5&baths_max=6&beds_max=5`

