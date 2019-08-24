from flask import Flask, request
import datetime
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

from flask import Response
app = Flask('FirstApplication')

@app.route("/", methods = ["GET","POST"])
def welcome():
    return "welcome to python"


@app.route("/currentdate", methods = ["GET"])
#@auth.login_required
def datetimenow():
    #print("HI")
    print(request, type(request))
    print(request.args.get("a"),request.url,request.method)
    return Response("currenttime: " + datetime.datetime.now().strftime("%Y-%m-%d"), status=200, mimetype='application/json')
    #return "currenttime: " + datetime.now().strftime("%Y-%m-%d")
    
@app.route("/getdate/<int:key>/", methods=['GET'])
def olderdate(key):
    olderdate = datetime.date.today() - datetime.timedelta(days=key)
    #The return type must be a string, tuple, Response instance, or WSGI callable
    print(olderdate.strftime("%Y-%m-%d")) 
    return olderdate.strftime("%Y-%m-%d")
    #return ("old date", olderdate.strftime("%Y-%m-%d"))

@app.route("/getolderdate/<int:key>/", methods=['GET'])
def olderdate_1(key):
    olderdate = datetime.date.today() - datetime.timedelta(days=key)
    #The return type must be a string, tuple, Response instance, or WSGI callable
    print(olderdate.strftime("%Y-%m-%d")) 
    return olderdate.strftime("%Y-%m-%d")
    return ("old date", olderdate.strftime("%Y-%m-%d"))
    
app.run("127.0.0.1","8090")
