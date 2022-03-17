import imp
from django.http import HttpResponse, JsonResponse
from dataclasses import dataclass
from pydoc import render_doc
from django.shortcuts import render
from django.template import Template, Context
from core.erp.models import *

# Create your views here.

def myfirstview(request):

    data = {
        'name' : 'Manuel',
        'categories': Category.objects.all()
    }

    return render(request,'index.html', data)