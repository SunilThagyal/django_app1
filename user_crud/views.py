from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .config import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model,logout

# import pprint
# Create your views here.
def index(request):
     students = Student.objects.all()
     context = {
          'students': students
     }
     return render(request, 'index.html', context)

def create(request):
     if request.method == "GET":
          return render( request, "create.html" )
     else:
          data = {
               'first_name' : request.POST.get('first_name'),
               'last_name' : request.POST.get('last_name'),
               'city' : request.POST.get('city'),
               'phone_number' : request.POST.get('phone'),
          }
          Student.objects.create(**data)
          return redirect('index')
def delete(request, id):
     student = get_object_or_404(Student, id=id)
     student.delete()
     return redirect('index')

def update(request,id):
     student = get_object_or_404(Student,id=id)
     if(request.method == 'GET'):
          return render(request, 'update.html',{'student':student})
     else:
          student.first_name = request.POST['first_name']
          student.last_name = request.POST['last_name']
          student.city = request.POST['city']
          student.phone_number = request.POST['phone']
          student.save()
          return render(request, 'update.html',{'student':student})

def signup(request):
     if(request.method == "GET"):
          context = {'states': states}
          return render(request, 'Auth/signup.html',context)
     else:
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['first_name']+'60'
          phone = request.POST['phone']
          email = request.POST['email']
          password = request.POST['password']
          address = request.POST['address']
          address2 = request.POST['address2']
          city = request.POST['city']
          state = request.POST['state']
          user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
          
def login_view(request):
    if request.method == "GET":
        return render(request, 'Auth/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Attempt to fetch the user by email to get the username
        User = get_user_model()
        try:
            user_obj = User.objects.get(email=email)
            # Use Django's authenticate() function to verify the username/password
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # Authentication failed
                return HttpResponse('Password is incorrect')
        except User.DoesNotExist:
            # No user was found with this email address
            return HttpResponse('Login failed, user does not exist')
        
def logout_view(request):
    logout(request)
    return redirect(('login')) 