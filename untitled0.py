shopping_list=[]
print("enter the purchesed item one by one")
print("enter QUITE to quite the input mode")

while True:
    new_item=(input("enter the item ")).title()
    if new_item=="Quite":
        break
    elif new_item =="Show":
        for item in shopping_list:
            print(shopping_list.index(item)+1,".   ",item)
    elif new_item =="Help":
        print("type--------------- \nQUITE for quite the input mode \nSHOW for get detail of  enterd item ")
    else:
        value=new_item.split(",")
        shopping_list.extend(value)
for item in shopping_list:
    print(shopping_list.index(item)+1,".   ",item)
    
     