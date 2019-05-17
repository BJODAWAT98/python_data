
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""


import pymongo
client = pymongo.MongoClient("mongodb://bjodawat:bhavya%40123@bhayva0-shard-00-00-nylky.mongodb.net:27017,bhayva0-shard-00-01-nylky.mongodb.net:27017,bhayva0-shard-00-02-nylky.mongodb.net:27017/test?ssl=true&replicaSet=bhayva0-shard-0&authSource=admin&retryWrites=true")


mydb = client.forsk_database
Student_Name=input("enter the name of student")
Student_Age=input("enter the age of the student")
Student_Roll_no=input("enter the roll number of student")
Student_Branch=input("enter the branch of the student")


def student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    mydb.university.insert_one(
            {
                    "Student_Name" : Student_Name,
                    "Student_Age" : Student_Age,
                    "Student_Roll_no" : Student_Roll_no,
                    "Student_Branch" : Student_Branch
            
            })
    return "Employee added successfully"

student(Student_Name, Student_Age, Student_Roll_no, Student_Branch)
def fetch_all_student():
    data=mydb.yourcollectionname.find()
    print(data.collection)
fetch_all_student()
        

"""


Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.


Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database

"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS


browser = webdriver.Chrome("C:\Users\Anant Jodawat\Documents\Forsk_training\day8_data\chromedriver")
browser.get(url)


sleep(2)

A=[]
B=[]
C=[]
D=[]

for i in range(1,11):
    A.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[1]/p[1]/a").text)    
    B.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[1]/span").text)
    C.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[2]/span").text)
    D.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[3]/p[2]").text)


import pymongo
client = pymongo.MongoClient("mongodb://bjodawat:bhavya%40123@bhayva0-shard-00-00-nylky.mongodb.net:27017,bhayva0-shard-00-01-nylky.mongodb.net:27017,bhayva0-shard-00-02-nylky.mongodb.net:27017/test?ssl=true&replicaSet=bhayva0-shard-0&authSource=admin&retryWrites=true")




mydb = client.Bid_plus
def insert_database(A,B,C,D):
    for i in range (0,10):
        mydb.bid_table.insert_one(
            {
                    "BID NO" : A[i],
                    "items" : B[i],
                    "Quantity Required" : C[i],
                    "Department Name And Address" : D[i]
            
            })
        print("Employee added successfully")
        

insert_database(A,B,C,D)

"""

Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text


soup = BeautifulSoup(source,"lxml")

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


import pymongo
client = pymongo.MongoClient("mongodb://bjodawat:bhavya%40123@bhayva0-shard-00-00-nylky.mongodb.net:27017,bhayva0-shard-00-01-nylky.mongodb.net:27017,bhayva0-shard-00-02-nylky.mongodb.net:27017/test?ssl=true&replicaSet=bhayva0-shard-0&authSource=admin&retryWrites=true")


mydb = client.cricket
def insert_database(team_name,weighted_matches,points,points,rating):
    for i in range (0,16):
        mydb.rank_table.insert_one(
            {
                    "team_name" : team_name[i],
                    "weighted_matches" : weighted_matches[i],
                    "points" : points[i],
                    "rating" : rating[i]
            
            })
        print("Employee added successfully")
         

insert_database(team_name,weighted_matches,points,rating)