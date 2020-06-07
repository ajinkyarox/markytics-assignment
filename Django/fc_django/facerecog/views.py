# pages/views.py
import os
import base64
from django.http import HttpResponse
from .models import Form,SubIncidents
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from os import path
import json
import re
from re import search
import datetime,calendar
import time
from datetime import date
from django.shortcuts import render
import sys
"""from . import forms
sys.path.append(".")"""
from facerecog.forms import Form

def view(request):
    form=Form()
    return render(request,'form.html',{'form':form})

@csrf_exempt
def post(request):



    response={'status':'Failure'}
    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)
        if request.method=="POST":
            response={'status':'Success'}
            fm=Form()
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            print(body_data)
            fm.location=body_data['location']
            fm.indes = body_data['indes']
            fm.dtinc = body_data['date']+body_data['time']
            fm.incloc = body_data['incloc']
            fm.insev = body_data['insev']
            fm.suscau = body_data['suscau']
            fm.imactk = body_data['imactk']
            fm.repby=body_data['repby']
            fm.save()
            sb=SubIncidents()
            print('d')
            if body_data['subincty']['env'].strip()!=None and body_data['subincty']['env'].strip()!='':
                sb.env=str(Form.objects.get(repby=body_data['repby']))
            if body_data['subincty']['inj'].strip()!=None and body_data['subincty']['inj'].strip()!='':
                sb.inj=str(Form.objects.get(repby=body_data['repby']))
            if body_data['subincty']['pd'].strip()!=None and body_data['subincty']['pd'].strip()!='':
                sb.pd=str(Form.objects.get(repby=body_data['repby']))
            if body_data['subincty']['veh'].strip()!=None and body_data['subincty']['veh'].strip()!='':
                sb.veh=str(Form.objects.get(repby=body_data['repby']))
            sb.save()
            print(request)
    except Exception as e:
        response={'status':'Failure'+str(e)}
    print(response)
    return JsonResponse(response,safe=False)
