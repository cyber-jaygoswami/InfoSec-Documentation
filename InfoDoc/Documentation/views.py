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
        from django.utils.safestring import mark_safe
        link = '''<a href="/tool-name"> Here</a>'''
        messages.info(request,mark_safe("Enter tool name in search bar :: For tool names click " + link ) )
        return redirect('homePage')
    try:

        content = Description.objects.get(tool_name=search_query)
        # print(content.id)
        commands = Command.objects.filter(tool=content.id)
        # print(commands)
        context = {'content': content, 'commands': commands}
        return render(request, 'Documentation/content.html', context)
    except:
         # return HttpResponse("Tool not available ")
        from django.utils.safestring import mark_safe
        link = '''<a href="/tool-name"> Here</a>'''
        messages.info(request,mark_safe("Tool not available :: For tool names click " + link ) )
        return redirect('homePage')


def getToolName(request):
    tools = Description.objects.all()
    # print(tools)
    context = {'tools':tools}
    return render(request,"Documentation/tool-name.html",context)