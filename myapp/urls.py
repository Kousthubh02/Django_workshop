
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plot/', views.plot_view, name='plot'),
    # path('',views.home)
]
