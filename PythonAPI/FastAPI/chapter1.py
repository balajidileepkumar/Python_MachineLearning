#Basic Fast API App
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
	return 'Hello World'
    
#@app.get('/property')
#def property():
#    return 'This is a property page'
 
