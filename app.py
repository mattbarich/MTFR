#
# Author: Matt Barich
#

# Import dependancies
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import logging
from datetime import datetime

# Import helper functions
import utils.print_functions
import utils.gallatin
import utils.yellowstone
from config import Config

app = Flask(__name__)
config = Config()

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(level, from_number, message, extra_info=''):
    log_message = f"Phone Number: {from_number} | Message: {message} | route accessed: {extra_info}"
    if level == 'info':
        logging.info(log_message)
    elif level == 'warning':
        logging.warning(log_message)
    elif level == 'error':
        logging.error(log_message)


#Default Route (May not need once connected to Twilio)
@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        incoming_sms = request.form.get('Body').strip().lower()
        from_number = request.form.get('From')

        log_message('info', from_number, incoming_sms, '/')

        if incoming_sms != 'hello':
            return utils.print_functions.handle_invalid_requests_msg()
    
        return utils.print_functions.hello_msg()
    except Exception as e:
        log_message('error', 'Unknown', 'Error in home route', str(e))
        return jsonify({"error": "An error occurred, please try again later"}), 500

@app.route("/sms", methods=['GET', 'POST'])
def test():
    from_number = request.form['From']
    incoming_sms = request.form['Body'].strip().lower()
    log_message('info', from_number, incoming_sms, '/sms')

    resp = MessagingResponse()    
    try:
        if incoming_sms == "hello" and from_number in config.approved_phone_numbers:
            response_msg = (
                f"Welcome {config.approved_phone_numbers[from_number]}!!\n"
                + utils.print_functions.hello_msg() 
                + utils.print_functions.sms_rates_msg()
            )
            resp.message(response_msg)
        
        elif incoming_sms == "help" and from_number in config.approved_phone_numbers:
            response_msg = (utils.print_functions.help_msg() 
                            + utils.print_functions.sms_rates_msg()
                            )
            resp.message(response_msg)

        elif from_number in config.approved_phone_numbers:
            response_msg = process_message(incoming_sms)
            resp.message(response_msg)

        else:
            response_msg = utils.print_functions.unregistered_number() + utils.print_functions.sms_rates_msg()
            resp.message(response_msg)

        return str(resp)
    except Exception as e:
        log_message('error', from_number, 'Error in home route', str(e))
        resp.message(utils.print_functions.handle_invalid_requests_msg() + utils.print_functions.sms_rates_msg())
        return str(resp), 500
    
def process_message(message: str) -> str:
    # Check if the message contains "gallatin"
    if "gallatin" in message:
        # Iterate through the base_urls dictionary to find a matching keyword
        for key in config.gallatin_urls:
            if key in message:
                url = config.gallatin_urls[key]
                report_function = config.gallatin_report_functions[key]
                report = report_function(url)
                return report + utils.print_functions.sms_rates_msg()
        
        # If no matching keyword is found, return a default message
        return utils.print_functions.help_msg + utils.print_functions.sms_rates_msg()
    
    elif "yellowstone" in message:
        for key in config.yellowstone_urls:
            if key in message:
                url = config.yellowstone_urls[key]
                report_function = config.yellowstone_report_functions[key]
                report = report_function(url)
                return report + utils.print_functions.sms_rates_msg()
        return utils.print_functions.handle_invalid_requests_msg() + utils.print_functions.sms_rates_msg()
    
    elif "madison" in message:
        return f"Still working on getting upper and lower madison reports working..." + utils.print_functions.sms_rates_msg()   
        #if "upper" in message:
         #   return "Upper madison requested"
        #elif "lower" in message:
        #    return "lower madison requested"
        #else:
         #   return utils.print_functions.handle_invalid_requests_msg()
    
    elif "missouri" in message:
        return f"Still working on getting missouri river reports working..." + utils.print_functions.sms_rates_msg()
    
    return utils.print_functions.random_msg() + utils.print_functions.handle_invalid_requests_msg () + utils.print_functions.sms_rates_msg()



