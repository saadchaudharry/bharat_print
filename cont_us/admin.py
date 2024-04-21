from django.contrib import admin
from .models import ContactUs,Client,team,social_media

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(social_media)
admin.site.register(Client)
