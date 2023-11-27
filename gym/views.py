from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Member, Contacts

def home(request):
    return render(request,"index.html")

def carrers(request):
    return render(request, 'carrers.html')

def pricing(request):
    return render(request, 'pricing.html')

def classes(request):
    return render(request, 'classes.html')

def thanks(request):
    return render(request, 'thanks.html')

@csrf_exempt
def join_gym(request):
    print("hello")
    if request.method == 'POST':
        # Get form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        membership = request.POST.get('membership')
        print(name,email,phone,membership)
        member = Member(name=name, email=email, phone=phone, membership=membership)
        member.save()
        print("data addedd succesfully")
        response_data = {'message': 'Form submitted successfully!'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"status":"failed"})
    
@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        # Get form data from the POST request
        email = request.POST.get('email')
        contact_us = Contacts(email=email)
        contact_us.save()
        print("data addedd succesfully in contact us table")
        response_data = {'message': 'Form submitted successfully!'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"status":"failed"})
