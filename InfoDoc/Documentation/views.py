from django.shortcuts import render, redirect

from .models import Description, Command
from django.shortcuts import HttpResponse
from django.contrib import messages
# Create your views here.


def homePage(request):
    return render(request, 'Documentation/index.html')


def aboutPage(request):
    return render(request, 'Documentation/about.html')


def getContent(request):
    search_query = request.GET.get('search_query')
    # print(search_query)
    if search_query == "":
        messages.info(request,"Enter tool name in search bar ")
        return redirect('homePage')
    try:
        
        content = Description.objects.get(tool_name=search_query)
        # print(content.id)
        commands = Command.objects.filter(tool=content.id)
        # print(commands)
        context = {'content': content,'commands':commands}
        return render(request, 'Documentation/content.html', context)
    except:
         # return HttpResponse("Tool not available ")
        messages.info(request,"Tool not available ")
        return redirect('homePage')
