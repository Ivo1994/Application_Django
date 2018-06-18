from django.urls import path
from . import views

urlpatterns = [
    # /dashboard/
    path('', views.index, name='index')
]