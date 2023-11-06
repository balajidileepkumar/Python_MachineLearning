#chapter -6
#providing default values to query parameters

from fastapi import FastAPI
app = FastAPI()

@app.get('/user/{username}')
def getuser(username:str):
    return f'user details of user {username}'
   
@app.get('/products')
def getproducts(id:int=1, price:int=1):
	return f'product with product id : {id} and price :{price}'
#call the endpoint like http://localhost:8000/products
#call the endpoint like http://localhost:8000/products?id=5&price=20