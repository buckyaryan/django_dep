from django.contrib import admin
from start_app.models import Topic, Webpage, Access, UserInfo, UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Access)
admin.site.register(Webpage)
admin.site.register(UserInfo)
admin.site.register(UserProfileInfo)