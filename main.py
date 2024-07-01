import argparse
import utils.gallatin
import utils.menus

# Define Global URL Variables
bozemanFlySupplyURL = "https://www.bozemanflysupply.com/river-report/"
riverEdgeURL = "https://theriversedge.com/pages/"
montanaAnglersURL = "https://www.montanaangler.com/montana-fishing-report/"
yellowDogURL = "https://www.yellowdogflyfishing.com/pages/"
madisonRiverFishingCompany = "https://www.mrfc.com/pages/madison-river-fishing-report"
tackleShop = "https://www.thetackleshop.com/fishing_report/salmon-fly-madness-on-the-madison-river/" # Dynamic URL must set manually

#URL postfix
end = "-river-fishing-report"

def gallatin(river):
    userInput = utils.menus.gallatinMenu()
    if userInput == 1:
        url = bozemanFlySupplyURL + river
        report = utils.gallatin.bozemanFlySupplyReport(url)
        print(report)
    elif userInput == 2:
        url = riverEdgeURL + river + end
        report = utils.gallatin.riversEdgeReport(url)
        print(report)
    elif userInput == 3:
        url = montanaAnglersURL + river + end
        report = utils.gallatin.montanaAnglersReport(url)
        print(report)
    elif userInput == 4:
        url = yellowDogURL + river + end
        utils.gallatin.yellowDogReport(url)
    else:
        print(f"Unexpected input... Try again.")

def madison(river):
    section = utils.menus.upperOrLower()
    if section == 1:
        userInput = utils.menus.upperMadisonMenu()
        if userInput == 1:
            url = bozemanFlySupplyURL + "upper-" + river
        elif userInput == 2:
            url = riverEdgeURL + "upper-" + river + end
        elif userInput == 3:
            url = montanaAnglersURL + "upper-" + river + end
        elif userInput == 4:
            url = yellowDogURL + "upper" + river + "-fishing-reports"
        elif userInput == 5:
            url = tackleShop
        elif userInput == 6:
            url = madisonRiverFishingCompany
        else:
            print(f"Unexpected input... Try again.")
    elif section == 2:
        userInput = utils.menus.lowerMadisonMenu()
        if userInput == 1:
            url = bozemanFlySupplyURL + "lower-" + river
        elif userInput == 2:
            url = riverEdgeURL + "lower-" + river + end
        elif userInput == 3:
            url = montanaAnglersURL + "lower-" + river + end
        elif userInput == 4:
            url = yellowDogURL + "lower-" + river + "-fishing-reports"
            print(url)
    else:
        print("Not an option try again...")

def yellowstone(river):
    userInput = utils.menus.yellowstoneMenu()
    if userInput == 1:
        url = bozemanFlySupplyURL + river
    elif userInput == 2:
        url = riverEdgeURL + river + end
    elif userInput == 3:
        url = montanaAnglersURL + river + end
    elif userInput == 4: 
        url = yellowDogURL + river + end
    else:
            print(f"Unexpected input... Try again.")

def missouri(river):
    userInput = utils.menus.missouriMenu()
    if userInput == 1:
        url = bozemanFlySupplyURL + river
    elif userInput == 2:
        url = riverEdgeURL + river + end
    elif userInput == 3:
        url = montanaAnglersURL + river + end
        print(url)
    elif userInput == 4: 
        url = yellowDogURL + river + end
    else:
            print(f"Unexpected input... Try again.")
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