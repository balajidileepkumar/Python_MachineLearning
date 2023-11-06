from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    #return HttpResponse('helloworld')
    #return render(request, 'generator/home.html')
    return render(request, 'generator/home.html', {"user1":"Balaji","user2":"vamsi","user3":"deepak","user4":"sandhiya"})#render data to template

def password(request):

    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = request.GET.get('uppercase')
    print(uppercase)
    if(uppercase):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specialchars = request.GET.get('specialchars')
    print(specialchars)
    if(specialchars):
        characters.extend('@#$%^&*!')
    numbers = request.GET.get('numbers')
    print(numbers)
    if(numbers):
        characters.extend('0123456789')

    passwordlength = int(request.GET.get('length'))
    print(passwordlength)
    for i in range(0,passwordlength):
        password+= random.choice(characters)

    return render(request,'generator/password.html',{'password':password})