# cont_us/templatetags/custom_filters.py
from django import template
from job.models import catagory,Phone_number

register = template.Library()

@register.filter(name='catagory_list')
def catagory_list(value):
    catag = catagory.objects.filter(Enable=1).all().order_by('position')
    return catag


@register.filter(name='latest_phone_number')
def latest_phone_number():
    latest_phone = Phone_number.objects.order_by('-timestamp').first()
    return latest_phone.phone if latest_phone else None
