from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from ..models.Profile import Profile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                # Log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                # create a Profile object for the new user
                user_modal = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_modal, id_user=user_modal.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
