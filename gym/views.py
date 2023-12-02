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

def blog(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')

def gym_schedule(request):
    return render(request, 'gym_schedule.html')

@csrf_exempt
def join_gym(request):
    print("hello")
    if request.method == 'POST':
        # Get form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        membership = request.POST.get('membership')
        password = request.POST.get('pass')
        print(name,email,phone,membership, password)
        member = Member(name=name, email=email, phone=phone, membership=membership, password=password)
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




@csrf_exempt
def validate_login(request):
    if request.method == 'POST':
        # Get form data from the POST request
        password = request.POST.get('pass')
        email = request.POST.get('email')
        data = Member.objects.filter(email=email, password=password).first()
        if data:
            print("loginn success data fetched okk")
            print(email,password)
            res={'message':'ok'}
            return JsonResponse(res)
        response_data = {'message': 'notok'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"message":"method not allowed"})