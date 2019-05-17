

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests


source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print(source)


soup = BeautifulSoup(source,"lxml")
print(soup.prettify())

rank_table=soup.find("table",class_="table")

team_name=[]
weighted_matches=[]
points=[]
rating=[]

for team in rank_table.findAll("tr"):
    oneline=team.findAll("td")
    
    if len(oneline)==5:
        team_name.append(oneline[1].text.strip())
        weighted_matches.append(oneline[2].text.strip())
        points.append(oneline[3].text.strip())
        rating.append(oneline[3].text.strip())
        
        
import pandas as pd
from collections import OrderedDict
col_data = [team_name,weighted_matches,points,rating]
data_frame=pd.DataFrame(col_data)

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
     
     

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

from bs4 import BeautifulSoup
import requests


source = requests.get("https://bidplus.gem.gov.in/bidlists").text
print(source)

soup = BeautifulSoup(source,"lxml")

main_taible=soup.find(class="")


