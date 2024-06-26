def upperOrLower():
    section = ["Upper", "lower"]
    print("What section of the Madison?\n")
    for inx, option in enumerate(section, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter Number: "))

    return choice

def gallatinMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge", "Montana Angler", "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))

    return choice

def upperMadisonMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog", 
                "The Tackle Shop", 
                "Madison River Fishing Company"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))

    return choice
def lowerMadisonMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge", "Montana Angler", "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))

    return choice

def yellowstoneMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge", "Montana Angler", "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))

    return choice

def missouriMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge", "Montana Angler", "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))

    return choice
