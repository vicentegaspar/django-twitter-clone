from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet

# Register your models here.

# unregister groups
admin.site.unregister(Group)


# mix profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User

    # Just display usernames on admin page
    fields = ["username"]
    inlines = [ProfileInline]


# unregister inital user
admin.site.unregister(User)
# Re register user and useradmin and pprofile
admin.site.register(User, UserAdmin)
admin.site.register(Tweet)
