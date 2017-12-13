from flask import Flask, render_template, request
from stackapi import StackAPI
import requests

app = Flask('Stack Overflow OAuth')
SITE = StackAPI('stackoverflow')

@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.to_dict()
      print(result['Name'])
      r = requests.get("https://api.stackexchange.com/2.2/users/"+result['Name']+"/posts?order=desc&sort=activity&site=stackoverflow")
      print(r.json())
      return render_template("renderPosts.html", result = r.json())



@app.route("/")
def hello():return render_template('stack.html')

@app.route("/other")
def other():return "Other !"
