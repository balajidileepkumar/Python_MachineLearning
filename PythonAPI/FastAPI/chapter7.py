#chapter 7 required query parameters
from fastapi import FastAPI
app = FastAPI()

#path parameter
@app.get('/user/{username}')
def getusername(username:str):
	return f'this is a profie page for user {username}'
 
#path and query parameter 
#remove the default value to make it required parameter
#@app.get('/products')
#def getproduct(id:int=1,price:int=5):
#    return f'this is a product with id : {id} and price :{price}'

#validate business logic
@app.get('/products')
def getproduct(id:int=None,price:int=None):
    return f'this is a product with id : {id} and price :{price}'
#http://localhost:8000/products?id=10
@app.get('/user/{userid}/comments')
def getcommentfromuser(userid:int=1, commentid:int=10):
    return f'this is blog comment with user id : {userid} and comment with comment id: {commentid}'
    
    
