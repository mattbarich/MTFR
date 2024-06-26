import argparse
import utils.gallatin
import utils.menus

# Define Global Variables
bozemanFlySupplyURL = "https://www.bozemanflysupply.com/river-report/"
riverEdgeURL = "https://theriversedge.com/pages/"
montanaAnglersURL = "https://www.montanaangler.com/montana-fishing-report/"
yellowDogURL = "https://www.yellowdogflyfishing.com/pages/"

def gallatin(river):
    userInput = utils.menus.gallatinMenu()
    if userInput == 1:
        url = bozemanFlySupplyURL + river
        report = utils.gallatin.bozemanFlySupplyReport(url)
        print(report)
    elif userInput == 2:
        url = riverEdgeURL + river + "-river-fishing-report"
        report = utils.gallatin.riversEdgeReport(url)
        print(report)
    elif userInput == 3:
        url = montanaAnglersURL + river + "-river-fishing-report"
        utils.gallatin.montanaAnglersReport(url)
    elif userInput == 4:
        url = yellowDogURL + river + '-river-fishing-report'
        utils.gallatin.yellowDogReport(url)
    else:
        print(f"Unexpected input... Try again.")

def madison(river):
    section = utils.menus.upperOrLower()
    if section == 1:
        userInput = utils.menus.upperMadisonMenu()
        if userInput == 1:
            url = bozemanFlySupplyURL + "upper-" + river
            print(url)
        elif userInput == 2:
            url = riverEdgeURL + "upper-" + river + "-river-fishing-report"
            print(url)
        elif userInput == 3:
            url = montanaAnglersURL + "upper-" + river + "-river-fishing-report"
            print(url)
        else:
            print(f"Unexpected input... Try again.")
    elif section == 2:
        userInput = utils.menus.madisonMenu()
        print(userInput)
    else:
        print("Not an option try again...")

def yellowstone(river):
    userInput = utils.menus.yellowstoneMenu()
    print(userInput)

def missouri(river):
    userInput = utils.menus.missouriMenu()
    print(userInput)

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('arg', type=str, help='Which River do you want the fishing report for?')
    
    args = parser.parse_args()
    river = args.arg.lower()

    functions = {
        "gallatin": gallatin,
        "madison": madison,
        "missouri": missouri,
        "yellowstone": yellowstone
    }

    if river in functions:
        functions[river](river)
    else:
        print("Option not available at this time...Try again")
    


if __name__ == "__main__":
    main()