from input_and_output import *

dict1 = dict_input()
print("ORIGINAL DICTIONARY : ")
dict_output(dict1)

choice=1
list1=[]
print("List of Keys to Delete : ")
while(choice==1):
    key = input("Key : ")
    while(key==None or key=="" or key==" "):
        key = input("!-KEY CANNOT BE EMPTY-!\nKey : ")
    if key.isdigit():
        key = int(key)
    list1.append(key)
    choice = int(input("Do you want to add another key?\n1.Yes\t2.No\nChoice : "))

for key in list1:
    if key in dict1:
        del dict1[key]

print("DICTIONARY AFTER DELETION : ")
dict_output(dict1)

