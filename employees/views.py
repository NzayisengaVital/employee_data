from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Abakozi, Umushahara
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'employees/index.html')

def all_workers(request):
    list_employees = Abakozi.objects.all()
    
    return render(request, 'employees/all_workers.html', {'list_employees': list_employees})

def add_worker(request):
    if request.method == 'POST':
       Abakozi.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            akazi=request.POST.get('akazi'),
            itariki=request.POST.get('itariki') or None ,
        )

       

       return redirect('all_workers')
    
    return render(request, 'employees/add_worker.html')

def detail(request, id):
    details = Umushahara.objects.filter(umukozi_id = id)
    return render(request, 'employees/detail.html', {'mydetails':details})

#def injira(request):
    return render(request, 'employees/injira.html')
#def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Hello🙋‍♂️, Admin')
            return redirect('home')
        else:
            messages.error(request, 'Invalid user name or password')


    return render(request, 'employees/login.html')
       
        
