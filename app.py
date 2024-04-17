import os
import urllib.request
import json
import ssl

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
  temp = request.form.get('temp')
  temp = int(temp)/100
  data =   {
     "Inputs": { 
       "data": [
          {
           "day": 13,
           "mnth": 3,   
           "year": 2023,
           "season": 1,
           "holiday": 0,
           "weekday": 0,
           "workingday": 1,
           "weathersit": 6, 
           "temp": temp, 
           "atemp": 0.1,
           "hum": 0.5,
           "windspeed": 0.3
           }
          ]    
         },   
       "GlobalParameters": 1.0
      }
    body = str.encode(json.dumps(data)
    url = 'http://54dabd99-b27c-4ffd-9394-e2ababbf499c.australiasoutheast.azurecontainer.io/score'
    api_key = 'e6H0YTbuQdcVxzBvMebO35YpS9bZJaSx'
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    response = urllib.request.urlopen(req)
    result = response.read()
    ttt = result.decode('utf-8')
    t1 = ttt.find("[")
    t2 = ttt.find("]")
    ttt3 = ttt[t1+1:t2]
    print('Request for hello page received with name=%s' % ttt3)
    return render_template('hello.html', name = ttt3)
    # else:
    #   print('Request for hello page received with no name or blank name -- redirecting')
    #   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
