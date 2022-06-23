from django.shortcuts import render, redirect
from .models import Prompt
from .forms import PromptForm
from django.contrib import messages

# Create your views here.
def home(request):
    project = Prompt.objects.all()
    context = {'project':project}
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            messages.success(request, "Article added successfully!!")
            form.save()            
            return redirect('/')
    return render(request, 'summary/add.html')

def view(request,pk):
    project = Prompt.objects.get(id=pk)
    context = {'project':project}

    return render(request, 'summary/project.html', context)

def edit(request,pk):
    project = Prompt.objects.get(id=pk)
    form = PromptForm(instance=project)

    if request.method == 'POST':
        form = PromptForm(request.POST, instance=project)
        if form.is_valid():
            messages.success(request, "Article modified successfully!!")
            form.save()
            return redirect('/')

    context = {'form':form}            
    return render(request, 'summary/edit.html', context)


def delete(request,pk):
    project = Prompt.objects.get(id=pk)
    context = {'project':project}
    if request.method == 'POST':
        messages.success(request, "Article deleted successfully!!")
        project.delete()
        return redirect('/')
    return render(request, 'summary/delete.html', context)