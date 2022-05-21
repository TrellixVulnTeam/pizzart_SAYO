from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Massas

#class IndexPageViwer(TemplateView):
#    template_name='index.html'

def index(request):
    massa = Massas.objects.all()
    return render (request,'index.html',{
        'massa':massa
    })