from django.contrib import admin
from conferences.models.profiles import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = (
        "id",
        "first_name", 
        "last_name",
    )
