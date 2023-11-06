#chapter 2 using path parameters
from fastapi import FastAPI
app = FastAPI()

#default path is /user/admin so this should be on top to avoid calling /user/{username}    
@app.get('/user/admin')#keep static routes like this before dynamic routes
def getadmin():
    return 'This is admin page'
    
@app.get('/user/{username}')
def getuser(username:str):
	return f'user is {username}'
