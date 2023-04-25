# Use flask
from flask import Flask
from threading import Thread
from flask import render_template

#define flask app
app = Flask('')


#create route for home page
@app.route('/')
def main():
  return render_template('index.html')


#Run our flask app in a thread so that the bot and website can run simultaneously.
def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()
