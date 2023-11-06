#chapter-9 using pydantic models inside a function
from fastapi import FastAPI
from pydantic import BaseModel

class profile(BaseModel):
    name:str
    email:str
    age:int
class Product(BaseModel):
    name:str
    price:int
    discount:int
    discounted_price:float
        
app = FastAPI()

@app.get('/user/admin')
def getadmin():
    return 'this is profile page for admin'
#request body is used when we want to post data and get some reponse

@app.post('/addproduct')
def addproduct(product: Product):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return product
