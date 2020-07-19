from twilio.rest import TwilioRestClient
from flask import Flask, request, url_for,render_template
account_sid = 'AC82c98802f4fcda4125a33eb179dfa110'
auth_token = '8951389fc0227b775509541e0ee21e58'
client = TwilioRestClient(account_sid, auth_token)
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('watsapp.html')

@app.route("/data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        number = request.form["num"]
        message=request.form["msg"]
        message = client.messages.create(body=message,from_='+12013080312',to=number)
    return message.sid
if __name__ == '__main__':
    app.run()
