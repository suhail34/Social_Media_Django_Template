from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth

@login_required(login_url='signin')    
def logout(request):
    auth.logout(request)
    return redirect('signin')
