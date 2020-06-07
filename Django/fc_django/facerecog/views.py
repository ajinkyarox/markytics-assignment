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

        if request.method=="POST":
            response={'status':'Success'}

            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            from .models import Form
            fr=None
            try:
                fr=Form.objects.get(location=body_data['location'],indes=body_data['indes'],insev=body_data['insev'],repby=body_data['repby'])
            except Exception as e:
                print(str(e))

            if fr==None:
                fm = Form()
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
                obj=body_data['subincty']
                print(obj)
                if obj[0]=='on':
                    sb.env=Form.objects.get(location=body_data['location'],indes=body_data['indes'],insev=body_data['insev'],repby=body_data['repby']).id
                if obj[1]=='on':
                    sb.inj=Form.objects.get(location=body_data['location'],indes=body_data['indes'],insev=body_data['insev'],repby=body_data['repby']).id
                if obj[2]=='on':
                    sb.pd=Form.objects.get(location=body_data['location'],indes=body_data['indes'],insev=body_data['insev'],repby=body_data['repby']).id
                if obj[3]=='on':
                    sb.veh=Form.objects.get(location=body_data['location'],indes=body_data['indes'],insev=body_data['insev'],repby=body_data['repby']).id
                sb.save()
                print(request)
            else:
                response = {'status': 'Failure-Record already exists.'}
    except Exception as e:
        response={'status':'Failure:Exception-'+str(e)}
    print(response)
    return JsonResponse(response,safe=False)
