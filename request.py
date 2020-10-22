# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 01:05:50 2020

@author: mohssine
"""

from urllib import request, parse
import json

# Data dict
def send(data):
    url = "https://byte-happy.herokuapp.com/addAccident"
    # Dict to Json
    # Difference is { "test":10, "test2":20 }
    data = json.dumps(data)
    # Convert to String
    data = str(data)
    # Convert string to byte
    data = data.encode('utf-8')
    # Post Method is invoked if data != None
    req =  request.Request(url, data=data)
    req.add_header('Content-Type','application/json;charset=utf-8')
    # Response
    resp = request.urlopen(req)
    print(resp.read())


