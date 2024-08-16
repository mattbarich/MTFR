#
# Author: Matt Barich
#

# Import dependancies
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

# Import helper functions
import utils.functions
import utils.gallatin
import utils.yellowstone

# Global Variables
gallatin_urls = {
    "bozeman fly supply": "https://www.bozemanflysupply.com/river-report/gallatin",
    "bfs": "https://www.bozemanflysupply.com/river-report/gallatin",
    "rivers edge": "https://theriversedge.com/pages/gallatin-river-fishing-report",
    "montana anglers": "https://www.montanaangler.com/montana-fishing-report/gallatin-river-fishing-report",
    "yellowdog": "https://www.yellowdogflyfishing.com/pages/gallatin-river-fishing-report"
}

yellowstone_urls = {
    "bozeman fly supply" : "https://www.bozemanflysupply.com/river-report/yellowstone",
    "bfs" : "https://www.bozemanflysupply.com/river-report/yellowstone",
    "rivers edge" : "https://theriversedge.com/pages/yellowstone-river-fishing-report",
    "montana anglers" : "https://www.montanaangler.com/montana-fishing-report/yellowstone-river-fishing-report",
    "yellowdog" : "https://www.yellowdogflyfishing.com/pages/yellowstone-river-fishing-reports"
}

gallatin_report_functions = {
    "bozeman fly supply": utils.gallatin.bozemanFlySupplyReport,
    "bfs" : utils.gallatin.bozemanFlySupplyReport,
    "rivers edge": utils.gallatin.riversEdgeReport,
    "montana anglers": utils.gallatin.montanaAnglersReport,
    "yellowdog": utils.gallatin.yellowDogReport
}

yellowstone_report_functions = {
    "bozeman fly supply": utils.yellowstone.bozemanFlySupplyReport,
    "rivers edge": utils.yellowstone.riversEdgeReport,
    "montana anglers": utils.yellowstone.montanaAnglersReport,
    "yellowdog": utils.yellowstone.yellowDogReport
}

# Initalize App
app = Flask(__name__)


#Default Route (May not need once connected to Twilio)
@app.route("/", methods=['GET', 'POST'])
def home():
    incoming_sms = request.form.get('Body')
    incoming_sms = str(incoming_sms).lower()
    if incoming_sms != 'hello':
        return utils.functions.handle_invalid_requests()
    
    return utils.functions.print_hello_msg()

@app.route("/sms", methods=['GET', 'POST'])
def test():
    from_number = request.form['From']
    incoming_sms = request.form['Body'].strip().lower()

    resp = MessagingResponse()

    if incoming_sms == "hello":
        response_msg = f"Hello {from_number}!!\n"
        resp.message(response_msg)
    else:
        response_msg = utils.functions.random_message_return()
        resp.message(response_msg)

    return str(resp)
    
def processMessage(message: str) -> str:
    # Check if the message contains "gallatin"
    if "gallatin" in message:
        # Iterate through the base_urls dictionary to find a matching keyword
        for key in gallatin_urls:
            if key in message:
                url = gallatin_urls[key]
                report_function = gallatin_report_functions[key]
                report = report_function(url)
                return report
        
        # If no matching keyword is found, return a default message
        return utils.functions.handle_invalid_requests()
    
    elif "yellowstone" in message:
        for key in yellowstone_urls:
            if key in message:
                url = yellowstone_urls[key]
                report_function = yellowstone_report_functions[key]
                report = report_function(url)
                return report
        return utils.functions.handle_invalid_requests()
    
    return utils.functions.handle_invalid_requests()


