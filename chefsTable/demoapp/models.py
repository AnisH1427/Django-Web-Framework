from django.db import models
from django.contrib import admmin
from . import views

# Create your models here.
urlpatterns = [
    path('',views.hello,),
    
]