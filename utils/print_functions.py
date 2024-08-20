import random

def print_hello_msg() -> str:
    print_msg = '''
        Welcome to MTFR, the first SMS based fishing report service for
        Rivers in Southern Montana. This service is still in beta, as we work out issues. 
        
        Rivers currently supported:
        Madison River (Upper and Lower), Yellowstone River, Gallatin River,
        and the Missouri River. \n \n

        Fly Shops currently supported:
        Montana Anglers (Gallatin, Madison, Yellowstone, Missouri)\n
        Bozeman Fly Supply (Gallatin, Madison, Yellowstone, Missouri)\n
        YellowDog Fly Fishing (Gallatin, Madison, Yellowstone, Missouri)\n
        Rivers Edge (Gallatin, Madison, Yellowstone, Missouri)\n
        Dan Bailey's (Yellowstone)\n
        Yellowstone Anglers (Yellowstone)\n
        Headhunters Fly Shop (Missouri)\n

        Current usage:
        river flyshop\n
        E.X. Gallatin Montana Anglers\n 
            - This is will return the latest fishing report from Montana Anglers for the Gallatin.\n
        '''
    return print_msg

def print_sms_rates() -> str:
    return "\nMsg and Data rates may apply.\n"

def handle_invalid_requests() -> str:
    message = ("\nCould not process request...\n"
               "Usage: river flyshop\n"
               "EX: Gallatin Bozeman Fly Supply\n"
               )
    return message

def random_message_return() -> str:
    statements = [
    "Oi! Fuck off mate! Im still working! I cant have my little elves work 24/7",
    "Try again later... Im out fishing.",
    "could not process... maybe if you were better at fishing you wouldn't have to use this service...(Just Kidding I very much appriciate your support)",
    "idk what you want dude. Talk to Matt hes my master."
    ]   
    
    return  random.choice(statements)

