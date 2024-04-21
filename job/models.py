from django.db import models
from django.db.models.signals import pre_save
from bharat_print.utils import unique_slug_generator
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from tinymce.models import HTMLField

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=999)
    heading2 = models.CharField(max_length=999)
    enable = models.BooleanField(default=False)
    position = models.IntegerField(blank=True, null=True, unique=True)
    text = models.TextField(max_length=9999, null=True, blank=True)
    IMG = models.ImageField(upload_to='carousel/img1', null=True, blank=True)
    link_lable1 = models.CharField(max_length=9999, null=True, blank=True)
    link1 = models.CharField(max_length=9999, null=True, blank=True)
    link_lable2 = models.CharField(max_length=9999, null=True, blank=True)
    link2 = models.CharField(max_length=9999, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)
    def __str__(self):
        return str(self.title)

def RandSLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(RandSLUG, sender=Carousel)


class Client_review(models.Model):
    title = models.CharField(max_length=999)
    text = models.TextField(max_length=9999)
    name = models.CharField(max_length=9999)
    designation = models.CharField(max_length=9999)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=999, blank=True, null=True)
    def __str__(self):
        return str(self.title)
def Client_reviewSLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(Client_reviewSLUG, sender=Client_review)




class catagoryManager(models.Manager):
    def get_next_position(self):
        return self.count() + 1
class catagory(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    Enable = models.BooleanField(default=False)
    position = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    objects = catagoryManager()
    def __str__(self):
        return str(self.title)
def catagorySLUG(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.position:
        instance.position = int(catagory.objects.get_next_position()) + 1
pre_save.connect(catagorySLUG, sender=catagory)

def prodsignal_catagory_post_save(sender, instance, *args, **kwargs):
    if not instance.position:
        instance.position = int(catagory.objects.get_next_position()) + 1

post_save.connect(prodsignal_catagory_post_save, sender=catagory)





class ProductManager(models.Manager):
    def get_next_position(self):
        return self.count() + 1

class products(models.Model):
    image = models.ImageField()
    Enable = models.BooleanField(default=True)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=999)
    description = models.TextField(max_length=12000)
    overview = models.TextField(max_length=12000)
    price = models.DecimalField(max_digits=99999, decimal_places=2)
    catalogue = models.FileField(upload_to="catalogue/")
    phone = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    table_head = models.CharField(max_length=999, default="Technical Specification", blank=True, null=True)
    objects = ProductManager()
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

def prodsignal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.position:
        instance.position = int(products.objects.get_next_position()) + 1
pre_save.connect(prodsignal, sender=products)

def prodsignalpost_save(sender, instance, *args, **kwargs):
    if not instance.position:
        instance.position = int(products.objects.get_next_position()) + 1
post_save.connect(prodsignalpost_save, sender=products)





class Specification(models.Model):
    value = models.CharField(max_length=100, blank=True, null=True)
    Prod = models.ForeignKey(products, on_delete=models.PROTECT)

    def __str__(self):
        return f"""{self.value}--{self.Prod}"""


# project
class projectManager(models.Manager):
    def get_next_position(self):
        return self.count() + 1

class Project(models.Model):
    image_1 = models.ImageField()
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    image_4 = models.ImageField(blank=True, null=True)

    title         = models.CharField(max_length=100)
    description_1 = models.TextField(max_length=12000)

    Enable   = models.BooleanField(default=False)
    index = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    slug     = models.SlugField(max_length=100, blank=True, null=True)

    objects  = projectManager()

    def __str__(self):
        return str(self.title)


def project_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.position:
        instance.position = int(Project.objects.get_next_position()) + 1
pre_save.connect(project_signal, sender=Project)

def project_signalpost_save(sender, instance, *args, **kwargs):
    if not instance.position:
        instance.position = int(Project.objects.get_next_position()) + 1
post_save.connect(project_signalpost_save, sender=Project)





# Service
class ServiceManager(models.Manager):
    def get_next_position(self):
        return self.count() + 1

class Service(models.Model):
    image = models.ImageField()
    icon  = models.ImageField()

    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=12000)

    Enable   = models.BooleanField(default=False)
    index    = models.BooleanField(default=False)

    position = models.IntegerField(blank=True, null=True)
    slug     = models.SlugField(max_length=100, blank=True, null=True)

    objects  = ServiceManager()

    def __str__(self):
        return str(self.title)


def Service_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.position:
        instance.position = int(Service.objects.get_next_position()) + 1
pre_save.connect(Service_signal, sender=Service)

def Service_signalpost_save(sender, instance, *args, **kwargs):
    if not instance.position:
        instance.position = int(Service.objects.get_next_position()) + 1
post_save.connect(Service_signalpost_save, sender=Service)




# Service
class Top_contentManager(models.Manager):
    def get_next_position(self):
        return self.count() + 1

class Top_content(models.Model):
    image = models.ImageField()
    icon  = models.ImageField()

    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=12000)


    position = models.IntegerField(blank=True, null=True)
    slug     = models.SlugField(max_length=100, blank=True, null=True)

    objects  = Top_contentManager()

    def __str__(self):
        return str(self.title)


def Top_content_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.position:
        instance.position = int(Top_content.objects.get_next_position()) + 1
pre_save.connect(Top_content_signal, sender=Top_content)

def Top_content_signalpost_save(sender, instance, *args, **kwargs):
    if not instance.position:
        instance.position = int(Top_content.objects.get_next_position()) + 1
post_save.connect(Top_content_signalpost_save, sender=Top_content)




class Blogpost(models.Model):
    sr_no       = models.AutoField
    title       = models.CharField(max_length=50)
    photo       = models.ImageField()
    artical     = HTMLField()
    slug        = models.CharField(max_length=50,blank=True,null=True)
    timestamp	= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering=['-timestamp']


def Blogpost_slug_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(Blogpost_slug_pre_save,sender=Blogpost)




class Blogpost(models.Model):
    sr_no       = models.AutoField
    title       = models.CharField(max_length=50)
    photo       = models.ImageField()
    artical     = HTMLField()
    slug        = models.CharField(max_length=50,blank=True,null=True)
    timestamp	= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering=['-timestamp']


def Blogpost_slug_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(Blogpost_slug_pre_save,sender=Blogpost)




class Phone_number(models.Model):
    phone = models.CharField(max_length=999)
    timestamp	=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)
