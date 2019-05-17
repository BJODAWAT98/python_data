input_list=input("enter the commaseperated numbers")
main_list=list(input_list.split(","))
main_list=[int(x) for x in main_list]
main_tuple=tuple(main_list)

###########################################
all_days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
my_days=('Wednesday', 'Thursday', 'Friday')
my_days=list(my_days)
for day in all_days:
    if day not in my_days:
        my_days.append(day)
print(tuple(my_days))
        
#############################################

item_dictionary={}

while True:  
    item_input=input("enter the item name and net price").lower()
    if item_input=="exit":
        for product,price in item_dictionary.keys,item_dictionary.values:
            print(product,price)
        break
    else:
        item_detail=item_input.split(" ")
        print("item list",item_detail)
        if len(item_detail)==2:
            if item_detail[0] not in item_dictionary:
                item_dictionary[item_detail[0]]=int(item_detail[1])
            else:
                item_dictionary[item_detail[0]]=item_dictionary[item_detail[0]]+int(item_detail[1])
        else:## for length 3
            if item_detail[0]+" "+item_detail[1] not in item_dictionary:
                item_dictionary[item_detail[0]+" "+item_detail[1]]=int(item_detail[2])
            
            else:
                item_dictionary[item_detail[0]+" "+item_detail[1]]=item_dictionary[item_detail[0]+" "+item_detail[1]]+int(item_detail[2])
        
    
#################################################################
                
teen_dictionary=dict()
while True:
    key_elements=input("enter the key ")
    value_elements=int(input("enter the value of { key_elements}",key_elements))
    if key_elements=="exit":
        print(teen_dictionary)
        break
    else:
        if (value_elements) not in(13,14,17,18,19):
            teen_dictionary[key_elements]=value_elements
        else:
            teen_dictionary[key_elements]=0
#################################################################
            
string="www.google.com"
frequency = {}
for char in string:
    if char not in frequency:
        frequency[char]=1
    else:
        frequency[char]=frequency[char]+1
print(frequency)
###############################################################

            
compair_string="Python 3.2"
output_dictionary={"Digit":0,"Letters":0}
for char in compair_string:
    if char.isdigit() == True:
        output_dictionary["Digit"]+=1
    elif char.isalpha() == True:
        output_dictionary["Letters"]+=1
    else:
        pass
print(output_dictionary)
    
##################################################################

string1=""
for char in string:
    if char not in frequency:
        frequency[char]=1
    else:
        frequency[char]=frequency[char]+
    
    
#####################################################################

list_a=[1,3,6,78,35,55]
list_b=[12,24,35,24,88,120,155]

list_c=set(list_a).intersection(set(list_b))
print(list_c)

################################################################
list_main=list(set([12,24,35,24,88,120,155,12,24,35,24,88,120,155,88,120,155]))    
    
print(list_main)
###############################################################################
old_list = ["janusfury@aol.com","ajlitt@me.com","dburrows@me.com","robles@yahoo.com","jshirley@gmail.com","saridder@live.com","dmiller@mac.com","agapow@yahoo.ca","hamilton@sbcglobal.net","madler@att.net","grady@gmail.com","iami@gmail.com","heroine@gmail.com","loxy@att.net","violinhi@icloud.com","morain@sbcglobal.net","rgiersig@gmail.com","jhardin@outlook.com","pappp@msn.com","hermanab@live.com","avollink@verizon.net","bulletin@yahoo.com","smallpaul@msn.com","wagnerch@hotmail.com","harryh@me.com","gbacon@live.com","jcholewa@yahoo.ca","thassine@sbcglobal.net","amky@me.com","mgreen@gmail.com","srour@icloud.com","heidrich@gmail.com","danzigism@me.com","sabren@mac.com","arebenti@sbcglobal.net","marcs@live.com","shrapnull@att.net","jguyer@mac.com","msherr@me.com","aaribaud@aol.com","mfleming@yahoo.com","seano@icloud.com","laird@icloud.com","manuals@live.com","mfburgo@live.com","budinger@optonline.net","udrucker@verizon.net","benits@outlook.com","baveja@mac.com","feamster@gmail.com"]

print(len(old_list))

new_list = ["violinhi@icloud.com","morain@sbcglobal.net","rgiersig@gmail.com","jhardin@outlook.com","pappp@msn.com","hermanab@live.com","avollink@verizon.net","bulletin@yahoo.com","smallpaul@msn.com","wagnerch@hotmail.com","harryh@me.com","gbacon@live.com","jcholewa@yahoo.ca","thassine@sbcglobal.net","amky@me.com","mgreen@gmail.com","srour@icloud.com","heidrich@gmail.com","danzigism@me.com","sabren@mac.com","arebenti@sbcglobal.net","marcs@live.com","shrapnull@att.net","jguyer@mac.com","msherr@me.com","aaribaud@aol.com","mfleming@yahoo.com","seano@icloud.com","laird@icloud.com","manuals@live.com","mfburgo@live.com","budinger@optonline.net","udrucker@verizon.net","benits@outlook.com","baveja@mac.com","feamster@gmail.com"]

not_present=[]

for mail in old_list:
    if mail not in new_list:
        not_present.append(mail)
print(not_present)























