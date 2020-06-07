from django import forms

class Form(forms.Form):
    location = forms.CharField()
    indes = forms.CharField()
    dateinc = forms.CharField()
    timeinc=forms.CharField()
    incloc = forms.CharField()
    insev = forms.CharField()
    suscau = forms.CharField()
    imactk = forms.CharField()
    repby = forms.CharField()