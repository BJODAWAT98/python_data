a=list(range(0,20))
l1,l2 = [], []
final_lst = [l1.append(x) if x%2==0 else l2.append(x) for x in a]
print(l1,l2)

##########

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels=['a','e','i','o','u']
output=[]
for state in state_name:
    new_name=''
    for char in state.lower():
        if char not in vowels:
            new_name= new_name+char
    output.append(new_name)
print(output)    

##############################
length=6

for i in range (0,length):
    print('* '*i)
for j in range(length,0,-1):
    print('* '*(j))

#################################


inputvalues = "10 9 21 5"

input_list=inputvalues.split(" ")

a="false"
def positive(a,input_list):
    
    for number in input_list:    
        if int(number)> 0:
            a="true"
        else:
            a="false"
            break
    return a
a=positive(a,input_list)
def pallindrome(a,input_list):
    if a=="true":
        for number in input_list:
            if number==number[::-1]:
                break
                
    else:
        a="false"
    return a


print(pallindrome(a,input_list))

############################################    
import string
a_z = string.ascii_lowercase
a_z_list=list(a_z)

print(len(a_z_list))
input_string="Sphinx of black quartz judge my vow"
input_string=input_string.lower()

input_characher=list(set(list(input_string)))

input_characher=input_characher.sort()

a=""

for i in range (0,26):
    if a_z_list[i] in input_characher:
        a="yes"
    else:
        a='no'
        break
print(a)

#######################################################

inch1=2
inch5=2
length_wall=11
def bricks(inch1,inch5,length_wall):
    extra_brick=0
    a=False
    if length_wall <5:
        if 5-length_wall <= inch1:
            a=True
        else:
            a=False
    else:
        extra_bricks = int(length_wall/5)
        if length_wall-(extra_bricks*5) <= inch1:
            a=True
        else:
            a=False
    return a
  
bricks(2,4,18)             
######################################################

def reverse(input_string):
    output_string=''
    for char in range (len(input_string)-1,-1,-1):
        output_string+=input_string[char]
    return output_string

input_string=input("enter the string")
print(reverse(input_string))

##################################################

text="This is fun"

def translate(text):
    vowels=['a','e','i','o','u',' ']
    new_text=""
    for charecter in range(0,len(text)):
        if text[charecter] not in vowels:
            new_text=new_text+text[charecter]+'o'+text[charecter]
        else:
            new_text+=text[charecter]
    return new_text
translate(text)
###################################################
def average():
    result=0
    list_array=[1,2,3,4,100]
    l=len(list_array)
    for i in range(1,l-1):
        result=result+int(list_array[i])
    b=result/(len(list_array)-2)
    print('resutl',result)
    return b

print(average())
#################################################
input_data=input("enter the elements seperated by comma")
array=input_data.split(",")
print(array)
sm=0
for i in range(0,len(array)):
    if int(array[i])==13:
        array[i]=0
        array[i+1]=0
    else:
        sm= sm+int(array[i])
print(sm)    




        