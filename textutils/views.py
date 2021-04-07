
# views.py
# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check Checkbox values
    remove_punc = request.POST.get('remove_punc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    char_count = request.POST.get('char_count','off')
    #Check whick checkbox is on
    if remove_punc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed }
        djtext = analyzed
        

    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines','analyzed_text': analyzed }
        
        djtext = analyzed
        
    
    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Spaces','analyzed_text': analyzed }
        
        djtext = analyzed
        
        
    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text': analyzed }
        djtext = analyzed

    if(remove_punc!='on' and newlineremover !='on' and extraspaceremover != 'on' and fullcaps!='on'):
        return HttpResponse("Error.  Please select any option and try again.")

    return render(request,'analyze.html', params)
    

