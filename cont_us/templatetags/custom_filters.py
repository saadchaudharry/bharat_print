# cont_us/templatetags/custom_filters.py
from django import template
from job.models import catagory,Phone_number
from cont_us.models import social_media
register = template.Library()

@register.filter(name='catagory_list')
def catagory_list(value):
    catag = catagory.objects.filter(Enable=1).all().order_by('position')
    return catag
    
@register.filter(name='latest_phone_number')
def latest_phone_number(value):
    latest_phone = Phone_number.objects.order_by('-timestamp').first()
    return latest_phone.phone if latest_phone else None

@register.filter(name='get_social_media')
def get_social_media(value):
    social = social_media.objects.all()
    return social
