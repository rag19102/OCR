from django.urls import path
from . import views
from django.core.files.storage import FileSystemStorage
urlpatterns = [
   path('',views.home)
]
