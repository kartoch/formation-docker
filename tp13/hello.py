import click
from flask import Flask
 
app = Flask(__name__)

@app.route('/healthz')
def health():
    return {'message': 'Healthy'} 

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello world</title>
  </head>
  <body>
     Hello World !!!!<br/>
     <img src="static/flask.png"> 
  </body>
</html>
"""
