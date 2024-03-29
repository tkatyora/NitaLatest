from django.shortcuts import render , redirect
from django.contrib.auth.models import Group
from .forms import CreateUser ,GeneralUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth import authenticate , login,logout
from .models import NitacagraUsers

# Create your views here.
AllUsers = NitacagraUsers.objects.all()

# registration view of General user
def signup(request):
   
    if request.method == 'POST':
        form = CreateUser(request.POST)
        # form2 = GeneralUserForm(request.POST)
        if form.is_valid():
            GeneralUser = form.save()
            username = form.cleaned_data.get('username') 
            message = 'Account for'+username+'have been succesfully created'
            messages.success(request,message )
            login(request, GeneralUser)
            return redirect('dashboard')
        else:
            messages.warning(request,'Account not created \nPlease correct form1 errors' )
    else:
        form2 = GeneralUserForm()
        form = CreateUser()
       
        
    content={}
    content = {
        'form' : form,
        'form2' :form2
                }
    return render(request, 'Accounts/regester.html' , content)
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        if User is not None:
            login(request, User)
            print(request.user)
            #if LogInRole == 'admin':
            if username == 'takudzwa':
                messages.success(request, 'Log In Successfully As An Admin')
                return redirect('dashboard')
            #if LogInRole == 'murimi':
            elif username == 'Gracious':
                messages.success(request, f'Hie {username} Welcome to MurimiVangu Enjoy Today')
               
            else:    
                messages.success(request, 'Log In Successfully As A customer')
                #customer dashboard
               
        else:
            message = 'Sory Wrong Username or Paasword'
            messages.warning(request, message)
    return render(request, 'Accounts/login.html' )


def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')





