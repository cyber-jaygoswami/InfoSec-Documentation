from django.shortcuts import render, redirect
from .forms import UploadFile
import os
from django.contrib import messages
from .models import PdfFile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def downloadPage(request):
    data = PdfFile.objects.all()
    context = {'data':data}
    return render(request, 'cheatsheets/downloadPage.html',context)

@login_required(login_url='login')
def uploadPage(request):
    form = UploadFile()
    if request.method == "POST":
        pass
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('downloadPage')
        

    context = {'form': form}
    return render(request, 'cheatsheets/uploadPage.html', context)
