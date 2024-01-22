# I have created this file - Shagun
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Shagun','place':'Mars'}
    return render(request,'index.html',params)

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcount = request.POST.get('charcount','off')
   
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
           if char not in punctuations:
               analyzed = analyzed+char
        params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'change to upper','analyzed_text':analyzed}
        djtext = analyzed    

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'remove extra spaces','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'remove new line','analyzed_text':analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")    
         
    return render(request,'analyze.html',params)    

