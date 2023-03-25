from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import seaborn as sns
import seaborn.apionly as sns_api
import django_seaborn as sns_django
import pandas as pd

def plot_view(request):
    data = pd.read_csv('path/to/data.csv')
    plot = sns.scatterplot(x='x_col', y='y_col', data=data)
    plot = sns_api.fig_to_dict(plot.figure)
    return render(request, 'plot.html', {'plot': plot})

def home(request):
    return render(request,"index.html")
