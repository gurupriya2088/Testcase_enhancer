import json
import requests
import elasticsearch
import re,os
import textract
from flask import Flask,flash, render_template, request,jsonify,redirect,url_for, send_from_directory
from werkzeug import secure_filename

dl='.',',','!','\n','\t',' ','/',':',';'
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

dict1={'skill':["java","python","c","c++"]}
e={}
l=[]
g={}

s={}
a=[]
f={}
so={}

@app.route('/', methods=['GET', 'POST'])
def loginn():
   
    return render_template('loginn.html')
@app.route('/upload_file' ,methods=['GET', 'POST'])
def upload_file():
     if request.method == 'POST':
      	 es = elasticsearch.Elasticsearch(['http://localhost:9200/'], verify_certs=True)

         if not es.ping():
            flash(u'*db is down')
            return redirect( url_for('loginn'))
         if request.form['username'] == 'user' and request.form['password'] == 'user':
            return render_template('up.html')
            
         elif request.form['username'] == 'hr' and request.form['password'] == 'hr':
             
             return redirect( url_for('search'))
         else:
            error="invalid credentials"
            flash(u'*Invalid credentials', 'error')
            return redirect( url_for('loginn',error=error))
            

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
  if request.method == 'POST':
      
            errors = False
            a=[]
            global name,eid
            name = request.form['name']
            if name=='':
                flash(u'*Invalid credentials')
                errors=True

            dob = request.form['dob']
            if dob=='':
                flash(u'*Invalid credentials')
                errors=True
            email = request.form['email']
            if email=='':
                flash(u'*Invalid credentials')
                errors=True
            eid = request.form['eid']
            if eid=='':
                flash(u'*Invalid credentials')
                errors=True
            email_wd = email.split("@")[0]  
            global g
            g={ 'name' : name ,
	       'dob'  : dob,
                'email': email,
                'eid' : eid}
                            
     	    f=request.files['file']
            if f=='':
                flash(u'*Invalid credentials')
                errors=True
            
                       
            extension=f.filename.split(".")[1]
            fname= name+"_"+str(email_wd)+"."+extension
            g.update({'filename' : fname})
            

           
            f.save(os.path.join(os.path.abspath(os.curdir),fname))
            
            
            text=textract.process(os.path.join(os.path.abspath(os.curdir),fname))
            print (text)
            textdata=text.lower()
            
            
            
            s={
               
                    
                "analyzer":"example_1",
                "text":textdata
                     
               }

           
            
            
      
            target_url='http://localhost:5001/uploader_s'
           
            
            
            
           
           
            r = requests.post(target_url,data=json.dumps(s))
            
            
                
            
            global e
            sk= json.loads(r.text)
            e={}
            for k in sk["tokens"]:
                 e.update({k["token"] : k["token"]})
            
          
            
           
#f is a dict
      
   



      
      
  return render_template('result.html',result=e, k=name) 
@app.route('/sample', methods = ['POST'])
def sample():
	if request.method == 'POST':
            l= request.form.getlist('check')
            e=dict((k,0) for k in l)
                     
	    return render_template('disp.html',result=e,k=name) 
              
@app.route('/load', methods = ['POST'])
def load():
	
	if request.method == 'POST':
		
		   global f
		   
		   for i in request.form.keys():
		       
		       f.update({i : request.form[i]})
		       
		   
		   g.update({'skill_rating': f })
		   global l
		   for k in f:
		      l.append(k)
		   l=list(set(l))
		   g.update({'skills':l})
                   
		   target_url='http://localhost:5001/load_s'
		   r = requests.post(target_url,data=json.dumps(g))
	   
           
           
        return render_template('parse.html',parse=f,k=name)


@app.route('/samp', methods = ['POST'])
def samp():
	if request.method == 'POST':
		text = request.form.get('name').split(",")
                y=0
                for k in text:
                    e[k.lower()]=y
                vs={}
                a=requests.post("http://localhost:9200/sample/_close")
                b=requests.post("http://localhost:9200/sample/_open")
                with open("/etc/elasticsearch/myfile.txt" ,"a+") as fp:
                      s=fp.read()
                      for k in s.split():
                           vs.update({k : k})
                      for y in text:
                           if y not in vs.keys():
                               fp.write(y)
                               fp.write("\n")
                               
                                  
                fp.close()       
		
                target_url='http://localhost:5001/load_s'
                
                r = requests.post(target_url,data=json.dumps(e))
               
                
                
                     
	return render_template('result.html',result=e ,k=name)
@app.route('/stats',methods=['GET'])
def stats():
    return render_template('KIB.html')
@app.route('/search', methods = ['GET'])
def search():
   if request.method == 'GET':
        
        n="HR"
	h={
		"aggs" : {
        	"skills_aggs" : {
		"terms" : { "field" : "skills.keyword" }
        			}
    			 }
	   }
        target_url='http://localhost:5001/search_s'
	r = requests.post(target_url,data=json.dumps(h))
	second=json.loads(r.text)
	
   return render_template("search.html",sec=second,k=n)
@app.route('/name/<key>', methods = ['GET','POST'])
def name(key):
   if request.method == 'GET':
        n="HR"
	k={
        "query" : {
        "term" : {"skills":key} 
                   }
          }

        target_url='http://localhost:5001/name_s'
	r = requests.post(target_url,data=json.dumps(k))
	third=json.loads(r.text)
	
   return render_template("name.html",t=third,a=key,k=n)
@app.route('/fname/<key>', methods = ['GET'])
def fname(key):
   if request.method == 'GET':
	
      return send_from_directory(os.path.abspath(os.curdir), key)


      
      
if __name__ == '__main__':
   app.run(debug = True)
