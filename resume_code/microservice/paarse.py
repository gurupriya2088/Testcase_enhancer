import json

import os
import json
import requests
from flask import Flask, render_template, request,jsonify
from werkzeug import secure_filename

dl='.',',','!','\n','\t',' ','/'
app = Flask(__name__)



with open("config.json") as fd:
        
	T=json.load(fd)


@app.route('/uploader_s',methods=["POST","GET"])
def uploader_s():
  if request.method == "POST":
     header={"Content-Type":"application/json"}
     a=requests.post("http://localhost:9200/sample/_analyze",data=request.data,headers=header)
    
     return a.text



@app.route('/load_s', methods = ['POST'])
def load_s():
   global T
   if request.method == 'POST':
       header={"Content-Type":"application/json"}
       j=json.loads(request.data)
       url="http://localhost:9200/items/item/"+j["eid"]
       print (url)
       a=requests.put(url=url,data=request.data,headers=header)
       
       return a.text



@app.route('/search_s', methods = ['POST'])
def search_s():
  if request.method == 'POST':
      header={"Content-Type":"application/json"}
      a=requests.post("http://localhost:9200/items/item/_search",data=request.data,headers=header)
      
  return a.text
@app.route('/name_s', methods = ['POST'])
def name_s():
  if request.method == 'POST':
      header={"Content-Type":"application/json"}
      
      a=requests.post("http://localhost:9200/items/item/_search",data=request.data,headers=header)
      requests.post("http://localhost:9200/sample/_close")
      requests.post("http://localhost:9200/sample/_open")
  return a.text

if __name__ == '__main__':
   app.run(port = 5001)

