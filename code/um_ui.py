# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:24:03 2018

@author: swathisri.r
"""

import flask
from flask import render_template,redirect
app= flask.Flask(__name__)


@app.route('/test')
def test():
    return render_template('def.html')
@app.route('/home')
def home():
     return redirect('http://127.0.0.1:9171/test',302)
 
    
if __name__=='__main__':
   #run_simple('0.0.0.0', 8080, server, use_reloader=True, use_debugger=True)
   app.run(port=9118,debug=True)

