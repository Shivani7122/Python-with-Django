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
    fullcaps = request.GET.get('fullcaps','off')
    lowercase = request.GET.get('lowercase','off')
    print(removepunc)
    print(fullcaps)
    print(lowercase)
    print(djtext)
    #Analyze the text
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changes to UpperCase', 'analyzed_text': analyzed}
        return render(request,'analyze.html', params)
    elif(lowercase == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose':'Change to LowerCase', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
    

