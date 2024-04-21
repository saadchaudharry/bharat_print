from django.db import models
from bharat_print.utils import unique_slug_generator
from django.db.models.signals import pre_save

from django.conf import settings
from django.core.mail import send_mail
# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=999)
    email = models.EmailField()
    phone = models.CharField(max_length=999)
    msG = models.TextField(max_length=9999, verbose_name='message')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


def ContactUssignal(sender, instance, *args, **kwargs):
    subject = 'ENQUIRE FROM YOUR WEBSITE '
    message = f'''
                Name : {instance.name}
                Email : {instance.email}
                Phone : {instance.phone}
                Message :
                {instance.msG}.
        '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saadchaudhary646@gmail.com','Interiorneom@gmail.com ','maazchaudhary646@gmail.com']
    send_mail(subject, message, email_from, recipient_list)


pre_save.connect(ContactUssignal, sender=ContactUs)


class team(models.Model):
    name = models.CharField(max_length=999)
    designation = models.CharField(max_length=999)
    phone = models.CharField(max_length=999, blank=True, null=True)
    Email = models.CharField(max_length=999, blank=True, null=True)

    thumbnail = models.ImageField(upload_to="licenses")
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team member'


class Client(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="Gallary")
    index = models.BooleanField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'



class social_media(models.Model):
    name = models.CharField(max_length=999)
    thumbnail = models.ImageField(upload_to="social_media")
    url = models.CharField(max_length=999)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'social media'
        verbose_name_plural = 'social medias'





