#chapter-9 using request body with pydantic data models
from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name:str
    email:str
    age:int
    
        
app = FastAPI()

@app.get('/user/admin')
def getadmin():
    return 'this is profile page for admin'
#request body is used when we want to post data and get some reponse

#lets say we want to pass our data for a payment gateway page

#@app.post('/adduser')
#def adduser():
#    return f'user data'
#output - {"detail":"Method Not Allowed"}    

@app.post('/adduser')
def adduser(profile:Profile):
    return f'user data for profile : {profile.name}, age is {profile.age} and email is {profile.email}'
#output - "user data for profile : b, age is 10 and email is abc@gmail.com"
  

#"user data for profile : b, age is 10 and email is abc@gmail.com"
