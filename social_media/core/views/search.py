from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.Profile import Profile
from ..models.Profile import User
from itertools import chain

@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username=username)
        
        username_profile = []
        username_profile_list = []
        
        for users in username_object:
            username_profile.append(users.id)
            
        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
            
        username_profile_list = list(chain(*username_profile_list))
        
    return render(request, 'search.html', {'user_profile':user_profile, 'username_profile_list':username_profile_list})