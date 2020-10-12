#i have created this file--ravi

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ex1(request):
    s='''<h2>Navigation Bar<br></h2>
    <a href="https://www.facebook.com">Facebook</a><br>
    <a href="https://www.Hindustantimes.com">News</a><br>
    <a href="https://www.flipcart.com">Flipcart</a><br>
    <a href="https://www.youtube.com">Youtube</a><br>
    <a href="https://www.google.com">Google</a><br>'''
    return HttpResponse(s)
def analyze(request):
    #get the text
    djtext= request.POST.get('text','default')
    # check checkbox value
    removepunc= request.POST.get('removepunc','off')
    fullcaps=request.POST.get("fullcaps",'off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','Analyzed_text':analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'Analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'Analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed=analyzed+char
        params = {'purpose': 'Removed extra spaces', 'Analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(charcount=='on'):
        analyzed= ""
        count=0;
        for char in djtext:
            if char != " " or char == " ":
                count += 1
                analyzed = count
        params = {'purpose': 'Char Count', 'Analyzed_text': analyzed}
        #djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps !="on" and charcount !="on"):
            return HttpResponse("Please select any operation and try again..")

    else:
        return render(request, 'analyze.html', params)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

#def removepunc(request):
    #return HttpResponse("remove punc")

#def capfirst(request):
    #return HttpResponse("capitalize first")

#def newlineremove(request):
    #return HttpResponse("first remove new line <a href='/'>Back</a>")

#ef spaceremover(request):
    #return HttpResponse("space remover <a href='/'>Back</a>")

#def charcount(request):
    #return HttpResponse("charcount")

