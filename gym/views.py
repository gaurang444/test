from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def carrers(request):
    return render(request, 'carrers.html')
