# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    #Analyze the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)
    

