from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmployeeProfile
from .forms import EmployeeProfileForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    
    
    if request.method == "POST":
        
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect("register")
        else:
            user = User.objects.create_user( username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            messages.info(request, 'you are registered successfully')
            return redirect("login")
    
    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "your user  successfully login")
            return redirect( "add_employee")
        else:
            messages.info(request, "username or password are invalid")
            return redirect("login")
    return render(request, "login.html")
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeProfileForm()

    return render(request, 'add_employees.html', {'form': form})


def update_employee(request, pk):
    employee = get_object_or_404(EmployeeProfile, pk=pk, user=request.user)

    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeProfileForm(instance=employee)

    return render(request, 'update_employee.html', {'form': form, 'employee': employee})
        
def delete_employee(request, pk):
    employee = get_object_or_404(EmployeeProfile, pk=pk, user=request.user)
    employee.delete()
    return redirect('employee_list')


def employee_list(request):
    employees = EmployeeProfile.objects.filter(user=request.user)
    return render(request, 'employee_list.html', {'employees': employees})

def new(request):
    return render(request, "new.html")