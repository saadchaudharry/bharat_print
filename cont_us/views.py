from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView
from django.urls import reverse_lazy

from .form import ContactUS_form
from .models import team, Client, ContactUs

from job.models import Carousel,Top_content, Client_review,catagory,products,Specification,Project,Service,Blogpost

from itertools import chain
import json
import random

# Create your views here.


def index(request):
   service = Service.objects.filter(Enable=1).order_by('position')
   top_content = Top_content.objects.order_by('position')
   context = {'service':service,'top_content':top_content}

   return render(request, 'index.html', context)


def about(request):
    context={}
    return render(request, 'about.html', context)



def services(request):
    service = Service.objects.filter(Enable=1).order_by('position')
    top_content = Top_content.objects.order_by('position')

    context = {'service':service,'top_content':top_content}

    return render(request, 'services.html', context)



def Clients(request):
    Clients = Client.objects.all()
    context = {'Clients': Clients}
    return render(request, 'clients.html', context)

class cont(CreateView):
    model = ContactUs
    form_class = ContactUS_form
    template_name = 'contact.html'
    success_url = reverse_lazy('cont')

    def get_context_data(self, *args, **kwargs):
        context = super(cont, self).get_context_data(*args, **kwargs)
        return context






def Allcatagory(request):
    catag = catagory.objects.filter(Enable=1).all().order_by('position')
    prod  = products.objects.filter(Enable=1).all().order_by('position')
    context={'catag':catag,'data':prod,'catagory_slug':''}
    return render(request,'shop_list.html',context)


def catagoryProd(request,catagory_slug):
    catag = catagory.objects.filter(Enable=1).all().order_by('position')
    prod  = products.objects.filter(Enable=1).all().order_by('position')
    if catagory_slug:
        cata = get_object_or_404(catagory,slug=catagory_slug)
        prod = prod.filter(catagory=cata,Enable=1).all().order_by('position')

    context={'catag':catag,'data':prod,'catagory_slug':catagory_slug}
    return render(request,'shop_list.html',context)


def product(request,slug):
    obj = products.objects.get(slug=slug)
    spec= Specification.objects.filter(Prod=obj).all()
    form_class = ContactUS_form

    context={"object":obj,'spec':spec,'form':form_class}
    return render(request,'product_detail.html',context)

def Project_list(request):
    Proj = Project.objects.filter(Enable=1).order_by('position')
    for proj in Proj:
        image_fields = (
            ('image_1', proj.image_1),
            ('image_2', proj.image_2),
            ('image_3', proj.image_3),
            ('image_4', proj.image_4),
        )
        items = [
            {"url": f"/media/{value}", "type": "image"}
            for name, value in image_fields
            if value
        ]
        proj.json_data = json.dumps({
            "items": items,
            "group": proj.slug
        })
    context = {'Proj': Proj}
    return render(request, 'project_list.html', context)



class Bloglist(ListView):
    queryset = Blogpost.objects.all()
    template_name = 'Blog_list.html'

class Blogdetail(DetailView):
    queryset = Blogpost.objects.all()
    template_name = 'Blog_detail.html'

