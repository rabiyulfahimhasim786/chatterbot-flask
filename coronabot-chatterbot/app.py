from chatbot import chatbot

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


@app.route("/helloworld", methods = ['GET', 'POST'])
def hello():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})


@app.route("/responce", methods = ['GET', 'POST'])
def message():
    if(request.method == 'GET'):
  
        userText = request.args.get('msg')
        datas = str(chatbot.get_response(userText))
        message = [{'data': datas}]
        #return str(chatbot.get_response(userText))
        return jsonify({'response': message})

if __name__ == "__main__":
    app.run()