from input_and_output import *
s = input("Enter a String : ")
while(s==None or s==""):
    print("String Cannot be empty!")
    s = input("Enter a String : ")

def StringDetails(s):
    dict1={}
    for character in s:
        sum=0
        for check in s:
            if check==character:
                sum+=1
        dict1[character]=sum
    return dict1

result = StringDetails(s)
print("RESULTANT DICTIONARY : ")
dict_output(result)

