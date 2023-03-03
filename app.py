import flask 
from flask import Flask, redirect, render_template, request
from flask_socketio import send, SocketIO
      
app = Flask('Discord Streaming Status')
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def home():
    succes = None
    if request.method == "POST":
        data = request.form
        name = data["sname"]
        url = data["surl"]
        data = [name, url]
        socketio.emit("stream", data)
        return render_template("succes.html", name=name)
    if request.method == "GET":
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
