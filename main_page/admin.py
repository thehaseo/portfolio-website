from django.contrib import admin
from .models import Projects, Technologies, RecievedMessages
# Register your models here.


admin.site.register(Projects)
admin.site.register(Technologies)
admin.site.register(RecievedMessages)