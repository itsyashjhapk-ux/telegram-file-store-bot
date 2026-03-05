from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/access/<file_id>")
def access(file_id):
    # Your redirect link logic
    return redirect(f"https://linkshotify.com/{file_id}")
