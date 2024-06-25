import sys
import argparse
import utils.gallatin


def main(arg):
    arg = arg.lower()
    if arg == "gallatin":
        print("Gallatin River requested")
    elif arg == "madison":
        userChoice = input("Upper or Lower? ")
        if userChoice.lower() == "upper":
            print("Upper Madison requested")
        elif userChoice.lower() == "lower":
            print("Lower Madison requested")
        else:
            print("You requested an option that is not available...")
            exit
    elif arg == "missouri":
        print("Missouri River requested")
    elif arg == "yellowstone":
        print("Yellowstone River Reported")
    else:
        print(f"No Fishing Report could be found... River Provided: {arg}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('arg', type=str, help='Which River do you want the fishing report for?')
    args = parser.parse_args()
    
    main(args.arg)