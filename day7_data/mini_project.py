"""
Create a client REST API that sends and receives some information from the Server by calling server's REST API.
You are expected to create two functions each for Sending and Receiving data.


You need to make two api calls, one with POST method for sending data and the other with GET method to receive data
All the communication i.e. sending and receiving of data with the server has to be in JSON format
First send the data to cloud using the "http://13.127.155.43/api_v0.1/sending" api with the following fields (Field names should be same as shown ):
Phone_Number (pass phone number as string and not as integer)
Name
College_Name
Branch
Now receive the data from cloud using the "http://13.127.155.43/api_v0.1/receiving" api with     “Phone_Number” along with the number you are looking for as query parameter
Print the server responses from both the cases. The first one will give response-code : 200 and response-message : "Data added Successfully", if all goes well. The second one will give all the details stored with the phone number you provided as query parameter. Both the responses will be in JSON format.
Output

response-code : 200 
response-message : Data added Successfully 


Submitted_at : Mon, 11 Sep 2017 13:32:30 GMT
Phone Number : 7877757144
Name : Kunal Vaid
Branch : B.Tech CSE
College_Name : Amity University
"""



import json
import requests

data={
      "Submitted_at" : "Mon, 11 Sep 2017 13:32:30 GMT",
      "Phone Number" : "7877757144",
      "Name" : "Kunal Vaid",
      "Branch" : "B.Tech CSE",
      "College_Name" : "Amity University"
            
      }

Host = "http://13.127.155.43/api_v0.1/sending"


headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post():
    responce=requests.post(Host,data,headers)
    return responce

print(post())




import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''

API_KEY = "XXXXXXXXXXXXXXXXX"
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 

r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.txt
 












