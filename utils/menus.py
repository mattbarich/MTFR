def printMenu(options):
    for inx, option in enumerate(options, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter Number: "))

    return choice

def upperOrLower():
    section = ["Upper", 
               "Lower"]
    print("What section of the Madison?\n")
    choice = printMenu(section)

    return choice

def gallatinMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    choice = printMenu(flyShops)

    return choice

def upperMadisonMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog", 
                "The Tackle Shop", 
                "Madison River Fishing Company"]
    print("Which fly shop would you like your report from?\n")
    choice = printMenu(flyShops)

    return choice
def lowerMadisonMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    choice = printMenu(flyShops)

    return choice

def yellowstoneMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    choice = printMenu(flyShops)

    return choice

def missouriMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    choice = printMenu(flyShops)

    return choice
