from django.urls import path

from . import views

urlpatterns = [
    path("fileupload/", views.uploadfile, name="fileupload"),
    path("analyse/",views.openaioutput,name="openaioutput"),
    path("result/",views.jobs_suggested,name="jobs_suggested")
]
