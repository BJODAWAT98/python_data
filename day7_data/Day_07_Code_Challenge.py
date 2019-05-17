"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
{
 "first_name":"BHAVYA",
 "last_name":"JODAWAT",
 "contect_number":[937487287,983789387,1238475378],
 "lecture":{
         "subject":"PYTHON",
         "class":"III YEAR",
         "timing":"10.00 AM"
         },
 "qualification":"PHD",
 "photo":"https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Ffree-vector%2Flovely-world-teachers-day-composition-with-flat-design_23-2147894442.jpg%3Fsize%3D338%26ext%3Djpg&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fteacher&docid=djeqU-CLBYw4YM&tbnid=9Z0mNUrHzeBVjM%3A&vet=10ahUKEwiRl8fNopriAhVOSX0KHVNcD8IQMwhmKAAwAA..i&w=338&h=338&bih=608&biw=1366&q=teacher%20image&ved=0ahUKEwiRl8fNopriAhVOSX0KHVNcD8IQMwhmKAAwAA&iact=mrc&uact=8",
 "research_areas":"TOC"
}



"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=5372b42f877d451e94ace089720437c0"
url=url1+url2+url3

response= requests.get(url)
print(response.content)

print(response.text)

data=response.json()

print("Latitude",data["coord"]["lon"])


print("Longitude",data["coord"]["lat"])
print("Weather Condition",data["weather"])
print("wind Speed",data["wind"])

for item in data:
    print(item)

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

response1=requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=0f5ece04061ac3026963")
data1=response1.json()
print(data1)




# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com







