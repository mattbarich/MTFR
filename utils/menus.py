def printMenu(options):
    for inx, option in enumerate(options, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter Number: "))

    return choice

def upperOrLower():
    section = ["Upper", 
               "Lower"]
    print("What section of the Madison?\n")

    return printMenu(section)

def gallatinMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")

    return printMenu(flyShops)

def upperMadisonMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog", 
                "The Tackle Shop", 
                "Madison River Fishing Company"]
    print("Which fly shop would you like your report from?\n")

    return printMenu(flyShops)

def lowerMadisonMenu():
    flyShops = ["Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")

    return printMenu(flyShops)

def yellowstoneMenu():
    flyShops = ["Yellowstone Angler",
                "Dan Bailys",
                "Bozeman Fly Supply", 
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")

    return printMenu(flyShops)

def missouriMenu():
    flyShops = ["Headhunters",
                "Cross Current",
                "The Rivers Edge", 
                "Montana Angler", 
                "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")

    return printMenu(flyShops)
