from input_and_output import *

dict1 = dict_input()
product=1
for key,value in dict1.items():
    product*=value

print("Dictionary : ")
dict_output(dict1)
print("Sum of Items : ",product)