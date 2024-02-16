from input_and_output import *

dict1 = dict_input()
result = dict1.copy()
dict2 = dict_input()
result.update(dict2)

print("--- Dictionary 1 ---")
dict_output(dict1)
print("--- Dictionary 2 ---")
dict_output(dict2)
print("--- Merged Dictionary ---")
dict_output(result)