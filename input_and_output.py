def dict_input():
    print("--- Dictionary Input ---")
    choice=1
    dict={}
    while(choice==1):

        key = input("Key : ")
        while(key==None or key=="" or key==" "):
            key = input("!-DICTIONARY CANNOT BE EMPTY-!\nKey : ")
        if key.isdigit():
            key = int(key)

        value = input("Value : ")
        while(value==None or value== " " or value==""):
            value = input("!-DICTIONARY CANNOT BE EMPTY-!\nValue : ")
        if value.isdigit():
            value = int(value)
        dict[key] = value
        choice = int(input("1.Enter Another Value\t2.No\nYour Choice : "))
        while(choice==1):
             choice = int(input("INVALID INPUT!!\n1.Enter Another Value\t2.No\nYour Choice : "))
    return dict

def dict_output(dict):
    print("Key\tValue")
    for key,value in dict.items():
        print(str(key)+"\t"+str(value))