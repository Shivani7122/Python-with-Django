# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #check box values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    lowercase = request.GET.get('lowercase','off')
    newlineremove = request.GET.get('newlineremove','off')
    extraspaceremove = request.GET.get('extraspaceremove','off')
    charcount = request.GET.get('charcount','off')
    #Check which Checkbox is ON
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
    elif(newlineremove=="on"):
        analyzed=""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    elif(extraspaceremove=="on"):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1]== " "):
                analyzed = analyzed + char  
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    elif(charcount=="on"):
        analyzed=("No. of characters in the given string is "+str(len(djtext)))        
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
    

