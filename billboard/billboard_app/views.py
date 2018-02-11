# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Messages 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index_page(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "registration.html")

def board_page(request):
    collect_datas = Messages.objects.all()

    for element in collect_datas:
        print element.title
        print element.content
        print element.author
        print element.date
    print len(collect_datas)
    return render(request, "board.html", context={'datas':collect_datas, 'size':len(collect_datas)})

@csrf_exempt
def add_message_DB(request):
    if request.is_ajax():
        resp = {'status':'success'}

        print request.POST.get('title')
        print request.POST.get('content')
        print request.POST.get('author')

        msg = Messages (title=request.POST.get('title'), content=request.POST.get('content'), author=request.POST.get('author'))

        msg.save()
    else:
        resp = {'status':'error'}

    return HttpResponse(resp)


    
