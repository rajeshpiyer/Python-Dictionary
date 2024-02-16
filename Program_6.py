from input_and_output import *

dict1 = dict_input()

maximum = max(dict1.values())
minimum = min(dict1.values())

print("Original Dictionary : ")
dict_output(dict1)

print("Maximum Value : ",maximum)
print("Minimum Value : ",minimum)

