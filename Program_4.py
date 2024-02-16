from input_and_output import *

dict1 = dict_input()
sum=0
for key,value in dict1.items():
    sum+=value

print("Dictionary : ")
dict_output(dict1)
print("Sum of Items : ",sum)