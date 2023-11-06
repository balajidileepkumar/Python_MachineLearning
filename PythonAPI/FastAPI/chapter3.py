#create path parameters

from fastapi import FastAPI
app = FastAPI()

#create a path  
@app.get('/movies')
def movies():
    return {'movielist':['movie1','movie2']}

#include a path parameter  #id specified without type
#@app.get('/property/{id}')
#def property(id):
#    return f'This is a property page {id}'

#include a path parameter  with type    
@app.get('/property/{id}')
def property(id:int):
    return f'This is a property page {id}'    

#include a path parameter  with type    
@app.get('/profile/{username}')
def profile(username:str):
    return f'This is a profile page for user : {username}'