from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def index(request):
    if request.method == "POST":
        link = request.POST.get('link')
        if not link:
            messages.error(request, "please type your link")
            return redirect('index')
        short_link = Short_link.objects.create(link=link)
        return redirect(f'/link/{short_link.short}/')
    return render(request, 'core/index.html')

def short_link(request, slug):
    try:
        new_link = Short_link.objects.get(short=slug)
    except Short_link.DoesNotexist:
        return redirect('index')
    return render(request, 'core/short-link.html', {'link':new_link})

def get_link (request, slug):
    try:
        new_link = Short_link.objects.get(short=slug)
        return redirect(f'{new_link.link}')
    except Short_link.DoesNotexist:
        return redirect('index')