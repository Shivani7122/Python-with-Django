#This file is created by me!!
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Hello Shivani!!</h1> <a href="https://www.youtube.com/">Youtube</a> ''')

def about(request):
    return HttpResponse("About hello Shivani")