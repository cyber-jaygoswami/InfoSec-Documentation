from django.urls import path
from . import views
urlpatterns = [
    path("",views.downloadPage,name="downloadPage"),
    path("upload",views.uploadPage,name="uploadPage"),
]