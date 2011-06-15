from django.contrib import admin

from reversion.admin import VersionAdmin

from userprofile.models import UserProfile

class UserProfileAdmin(VersionAdmin):
	pass
admin.site.register(UserProfile, UserProfileAdmin)
