from input_and_output import *

dict1 = {}
for i in range(1,16):
    key = i
    value = i**2
    dict1[key] = value

print("--- Resultant Dictionary ---")
dict_output(dict1)