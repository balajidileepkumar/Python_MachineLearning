#chapter6
#using path parameter and query parameter together

from fastapi import FastAPI
app = FastAPI()

@app.get('/user/{username}')
def getuser(username:str):
    return f'profile of user {username}'

@app.get('/products')
def getproducts(id:int=1, price:float=1.0):
    return f'product with id : {id} and price :{price}'
    
@app.get('/profile/{userid}/comments')
def profile(userid:int, commentid:int):
    return f'profile with user id :{userid} and comment id : {commentid}'
	
