from django.shortcuts import render, redirect
from ..models.Profile import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def settings(request):
    
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        return redirect('settings')
    
    return render(request, 'setting.html', {'user_profile':user_profile})
