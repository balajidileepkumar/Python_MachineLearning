#including query parameters in endpoints
from fastapi import FastAPI
app = FastAPI()

@app.get('/user/{username}')
def profile(username:str):
    return f'profile of user {username}'
    
@app.get('/products')
def products(id):
    return f'product with id : {id}'
    
#call query parameter like

#https:localhost:8000/products?id=10 --?id is the way to call the query parameter