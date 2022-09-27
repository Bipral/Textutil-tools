

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    '''We Got the text'''
    djtext = request.POST.get('Text','Default')
    removepun = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('capitalize','Off')
    remln = request.POST.get('removeline','Off')
    remsp = request.POST.get('removespace','Off')
    chcnt = request.POST.get('charcount','Off')


    if removepun == "on":
        punctuations = '''!()-+[]{};:`'"\,<>./?@#$%^&*=|_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuation' , 'Analyzed_text' : analyzed}
        return render(request, 'Analyze.html', params)

    elif fullcaps == "on":
        capital = ""
        for char in djtext:
            capital = capital + char.upper()
        params = {'purpose' : 'Capitalized Text' , 'Analyzed_text' : capital }
        return render(request,'Analyze.html',params)

    elif remln == 'on':
        remove_line = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                remove_line = remove_line + char
        params = {'purpose':'newline removed','Analyzed_text':remove_line}
        return render(request,'Analyze.html',params)

    elif remsp == "on":
        sprem = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                sprem = sprem + char
        params = {'purpose':'Extra Space Removed','Analyzed_text':sprem}
        return render(request,'Analyze.html',params)

    elif chcnt == "on":
        count = 0
        for char in djtext:
            count = count + 1
        params = { 'purpose': 'Charecter counted','Analyzed_text':count }
        return render(request,'Analyze.html',params)

    else:
        return HttpResponse("Error:Choose one of those Checkbox")

def capitalize(request):
    return HttpResponse(''' <h1> Capitalize first letter </h1> <a href = "http://127.0.0.1:8000/"> Back to Home </a> ''')

