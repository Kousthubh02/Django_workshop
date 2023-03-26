from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import seaborn as sns
import seaborn.apionly as sns_api
import django_seaborn as sns_django
import pandas as pd

def home(request):
    return render(request,"index.html")
