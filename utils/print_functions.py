import random

# Initial message sent to users when they first text the service 
def hello_msg() -> str:
    msg = '''
        You have been selected for beta testing on the first SMS based fishing report service for rivers in Southern Montana. 
        This service is still in beta, as I work out issues and get other rivers and shops functional.\n
        Rivers currently supported:
        Yellowstone River and Gallatin River.\n
        Fly Shops currently supported:
        Montana Anglers (Gallatin, Yellowstone)
        Bozeman Fly Supply (Gallatin, Yellowstone)
        Rivers Edge (Gallatin, Yellowstone)\n
        Current usage:
        river flyshop
        E.X. Gallatin Montana Anglers\n 
        - This is will return the latest fishing report from Montana Anglers for the Gallatin.
        '''
    return msg

# Data Message sent to users after each report
def sms_rates_msg() -> str:
    return "\nMsg and Data rates may apply.\n"

#Passive aggressive message sent to registered users when they ask for help
def help_msg() -> str:
    msg = ("\n So you need help...\n"
           "It's pretty simple honestly.\n"
           "Usage: river flyshop\n"
           "EX: Gallatin Bozeman Fly Supply\n"
           )
    return msg

# Message sent to users when they send an invalid request
def handle_invalid_requests_msg() -> str:
    msg = ("\nCould not process request...\n"
           "Usage: river flyshop\n"
           "EX: Gallatin Bozeman Fly Supply\n"
           )
    return msg

# Random message sent to users when they send an invalid request
def random_msg() -> str:
    statements = [
    "\nOi! Fuck off mate! Im still working! I cant have my little elves work 24/7\n",
    "\nTry again later... Im out fishing.\n",
    "\nCould not process... maybe if you were better at fishing you wouldn't have to use this service...(Just Kidding I very much appriciate your support)\n",
    "\nidk what you want dude. Talk to Matt hes my master.\n",
    "\nI'm out fishing... I'll hit you back later\n",
    "\nSometimes you just need to figure it out for yourself...\n",
    "\nIf you're looking for help, you're barking up the wrong fucking tree. Go ask someone else.\n",
    "\nI'm too busy sorting out a clusterfuck to deal with your nonsense. Try later.\n"
    ]   
    return  random.choice(statements)

# Number not registered
def unregistered_number() -> str:
    msg = ("\nOur records show you're number is not registered with the owner of this service.\n"
           "To gain early access to this service, please contact Matt.\n"
           "If you don't know Matt... Find someone who does lol\n"
           "Good luck and tight lines!\n"
           )
    return msg
