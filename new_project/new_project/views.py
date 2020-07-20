#This is the code i created
# my name is sahil ahuja
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyse(request):
    djtext=request.POST.get('text','default')
    last=djtext
    remove_punctuations=request.POST.get("remove punctuations",'off')
    upper_case=request.POST.get("upper_case","off")
    title_case=request.POST.get("title_case","off")
    new_line_remover=request.POST.get("new_line_remover","off")
    character_counter=request.POST.get("character_counter","off")
    analysed=""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    count=0
    if remove_punctuations!='off':
       analysed=""
       for char in djtext:
          if char not in punctuations:
              analysed=analysed + char
       params={'purpose':'Remove Punctuations','analysed_text':analysed}
       djtext=analysed
       # return render(request,'analyse.html',params)

    if upper_case!='off':
        analysed=""
        analysed=djtext.upper()
        params = {'purpose':'Upper Case','analysed_text': analysed}
        djtext = analysed

       # return render(request, 'analyse.html', params)

    if title_case!='off':
        analysed=""
        analysed=djtext.capitalize()
        params = {'purpose': 'Title Case', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)

    if new_line_remover!="off":
        analysed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analysed=analysed+char
        params = {'purpose': 'New Line Remover', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)

    if character_counter!='off':
        for char in djtext:
            if char!=' ':
                count=count+1

        params={'purpose':'Character Count','analysed_text':count}
        #return render(request,'analyse.html',params)
    if (remove_punctuations!='on' and new_line_remover!='on' and character_counter!='on' and title_case!='on' and upper_case!='on'):
        return HttpResponse(last)

    return render(request,'analyse.html',params)