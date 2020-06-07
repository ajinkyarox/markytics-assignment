# pages/views.py
import os
import base64
from django.http import HttpResponse
from .models import Form
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



