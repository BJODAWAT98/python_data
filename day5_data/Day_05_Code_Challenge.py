"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
number=input("enter the number")

import re

result=re.findall(r"^[+-]*\d*\.\d",number)
print(result)


"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
input_email=input("enter the email")
emails=input_email.split(",")
list1=[]

for email in emails:
    list2=re.findall(r"\w+@[a-z]+\.[a-z]{2,4}",email)
    list1.append()
print(list1)






"""

Code Challenge
  Name: 
    Regular Expression 3
  Filename: 
    regex3.py
  Problem Statement:
    You and Virat are good friends. 
    Yesterday, Virat received credit cards from ABCD Bank. 
    He wants to verify whether his credit card numbers are valid or not. 
    You happen to be great at regex so he is asking for your help!

    A valid credit card from ABCD Bank has the following characteristics:

    It must start with a '4', '5' or ' 6'.
    It must contain exactly 16 digits
    It must only consist of digits (0-9)
    It may have digits in groups of 4, separated by one hyphen "-"
    It must NOT use any other separator like ', ' , '_', etc
    It must NOT have 4 or more consecutive repeated digits 
 
  Hint: 
    Using Regular Expression 
  Input:
    4123456789123456
    5123-4567-8912-3456
    61234-567-8912-3456
    4123356789123456
    5133-3367 -8912-3456
    5123 - 3567 - 8912 - 3456
  Output:
    Valid
    Valid
    Invalid
    Valid
    Invalid
    Invalid
"""
card_detail=input("enter the card deatil")

list_card=(card_detail.split(","))


for card in list_card:
    if re.findall("^[456]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}",card):
        conter=0
        for degi in range(0,len(card)-1):
            pass
        print("valid")
    else:
        print("invelid")
    





"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
 
"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""
import re
with open("simpsons_phone_book.txt","rt") as fp1:
    lines=fp1.readlines()
    for line in lines:
        if re.findall(r"[Jj]{1}\w*\s+neu",line):
            print(line)
        else:
            print(line)



