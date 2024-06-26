import argparse
import utils.gallatin

def displayMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge", "Montana Angler", "Yellow Dog"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))
    return choice

def main(arg):
    bozemanFlySupplyURL = "https://www.bozemanflysupply.com/river-report/"
    riverEdgeURL = "https://theriversedge.com/pages/"
    montanaAnglersURL = "https://www.montanaangler.com/montana-fishing-report/"
    yellowDogURL = "https://www.yellowdogflyfishing.com/pages/"

    arg = arg.lower()
    userInput = displayMenu()
    if userInput == 1:
        url = bozemanFlySupplyURL + arg
        report = utils.gallatin.bozemanFlySupplyReport(url)
        print(report)
    elif userInput == 2:
        url = riverEdgeURL + arg + "-river-fishing-report"
        report = utils.gallatin.riversEdgeReport(url)
        print(report)
    elif userInput == 3:
        url = montanaAnglersURL + arg + "-river-fishing-report"
        report = utils.gallatin.montanaAnglersReport(url)
        print(report)
    elif userInput == 4:
        url = yellowDogURL + arg + '-river-fishing-report'
        utils.gallatin.yellowDogReport(url)
    else:
        print(f"Unexpected input... Try again.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('arg', type=str, help='Which River do you want the fishing report for?')
    args = parser.parse_args()
    
    main(args.arg)