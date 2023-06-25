from django.urls import path

from . import views

urlpatterns = [
    path("fileupload/", views.uploadfile, name="fileupload"),
    path("analyse/",views.openaioutput,name="openaioutput"),
]
