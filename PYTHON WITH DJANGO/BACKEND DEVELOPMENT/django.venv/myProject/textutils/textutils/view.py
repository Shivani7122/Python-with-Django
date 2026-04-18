#This file is created by me!!
from django.http import HttpResponse

#   ---------------   PERSONAL NAVIGATOR  ----------------
# def index(request):
#     return HttpResponse('''<h1>Hello Shivani!!</h1> <a href="https://www.youtube.com/">Youtube</a> ''')

# def about(request):
#     return HttpResponse("About hello Shivani")


#-------------  PIPELINING -----------------
def index(request):
    return HttpResponse('''<h1>Home</h1> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/newlineremove">Remove NewLine</a><br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/removepunc">Remove Punctuation</a><br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/capitalizeFirst">Capitalize First</a><br></br><a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/spaceremove">Remove Space</a><br></br><a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/charcount">Count Characters</a><br></br>''')

#---- Remove Punctuation -----
def removepunc(request):
    return HttpResponse('''remove punctuation !!<br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/">Back</a>''')

def capfirst(request):
    return HttpResponse('''Capitalize First.<br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/">Back</a>''')

def remline(request):
    return HttpResponse('''Remove Newline <br></br>  <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/">Back</a>''')

def charcnt(request):
    return HttpResponse('''Count Character <br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/">Back</a>''')

def spcrem(request):
    return HttpResponse('''Remove Space <br></br> <a href="https://congenial-disco-5gq5jx9jwpgrf7rqg-8000.app.github.dev/">Back</a>''')

