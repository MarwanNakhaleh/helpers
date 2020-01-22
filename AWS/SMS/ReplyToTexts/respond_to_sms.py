from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # get the text from the incoming message
    body = request.values.get('Body', None)
    print("{} said '{}'".format(str(request.values['From']), body))
    reply_message = ""
    if "10" in body or "9" in body or "8" in body:
        reply_message = "Hell yeah bro! Get that paper!"
    elif "7" in body or "6" in body or "5" in body or "4" in body:
        reply_message = "Hey man, progress is progress. Keep up the good work!"
    elif "3" in body or "2" in body or "1" in body or "0" in body:
        reply_message = "Well, get up off your ass and do it G. February is FAST approaching"
    else:
        reply_message = "Uhhh, that's not a valid response. Give it another try"

    resp = MessagingResponse()

    resp.message(reply_message)

    return str(resp)

@app.route("/fail", methods=['GET', 'POST'])
def failure():
    print("unable to send message")

if __name__ == "__main__":
    app.run(debug=True)