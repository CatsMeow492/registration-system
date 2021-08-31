try:
    name = input()
    if len(name) < 4:
        raise ValueError
    print("Account Created")
    
except:
    print("Invalid Name")