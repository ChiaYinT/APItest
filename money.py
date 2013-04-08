import json
import httplib, urllib
import hashlib
import base64
import simplejson

def test():
    token=login()
    addAccount(token)

def basic(url, content,method='POST'):
    print(url)
    headers = {'Content-type': "application/json", "Accept": "application/json"}
    conn = httplib.HTTPSConnection("www.blink.com.tw:11741")
    conn.request(method, url, content, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    return data

def login(): 
    url = "/users/sign_in"
    password = 'abc123'
    password = base64.b64encode(hashlib.sha1(password).digest())
    content = json.dumps({'username':'Money2', 'password': password})
    data=basic(url,content)
    data = simplejson.loads(data)
    token = data['token']
    return token

def logout(token):
    url = "/users/sign_out"
    content = json.dumps({'token': token})
    basic(url, content, "DELETE")

def forget():
    url = "/users/password"
    content = json.dumps({'username':'JillTsai', 'email': 'dododog168@hotmail.com'})
    data=basic(url,content)

def regist():
    url = "/users"
    password = 'abc123'
    password = base64.b64encode(hashlib.sha1(password).digest())
    content = json.dumps({'username': 'Money2', 'password':password,
                          'email': 'bn7894@cjpeg.com'})
    data=basic(url,content)

def phone_code(token):
    url = "/users"
    content =json.dumps( {'token': token, 'phone_code': '4EE.U3S'})
    data = basic(url,content,"PUT")
    
def addAccount(token):
    url = "/accounts"
    content = json.dumps({'token': token,
                          'name': 'Test Bank',
                          'amount': 10010000,
                          'currency': 'TWD',
                          'type':'Bank',
                          'date_at':'2012-07-17 20:31:54 +0800'})
    data=basic(url,content)
'''
def forget():
    url = ""
    content = json.dumps({})
    data=basic(url,content,"")
'''

test()
