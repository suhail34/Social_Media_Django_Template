from django.contrib import admin
from .models.Profile import Profile
from .models.Post import Post
from .models.LikePost import LikePost
from .models.FollowersCount import FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
