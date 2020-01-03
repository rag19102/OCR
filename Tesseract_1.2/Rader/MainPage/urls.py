from django.urls import path
from . import views
from django.core.files.storage import FileSystemStorage
urlpatterns = [
   path('',views.home),
   path('upload', views.Upload, name="UploadFile"),
   path('Dashboard', views.Dashboard),
   path('Result', views.Result)
]
