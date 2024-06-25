import argparse
import utils.gallatin

def displayMenu():
    flyShops = ["Bozeman Fly Supply", "The Rivers Edge"]
    print("Which fly shop would you like your report from?\n")
    for inx, option in enumerate(flyShops, start=1):
        print(f"{inx}. {option}")
    choice = int(input("Enter number: "))
    return choice

def main(arg):
    bozemanFlySupply = "https://www.bozemanflysupply.com/river-report/"
    riverEdge = "https://theriversedge.com/pages/"

    arg = arg.lower()
    userInput = displayMenu()
    if userInput == 1:
        url = bozemanFlySupply + arg
        report = utils.gallatin.bozemanFlySupplyReport(url)
        print(report)
    elif userInput == 2:
        url = riverEdge + arg + "-river-fishing-report"
        utils.gallatin.riversEdgeReport(url)
    else:
        print(f"Unexpected input... Try again.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('arg', type=str, help='Which River do you want the fishing report for?')
    args = parser.parse_args()
    
    main(args.arg)