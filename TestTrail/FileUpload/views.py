from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .functions.functions import identify_skills, calculate_cosine_similarity
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializer import *
from pathlib import Path
import os

directory = os.getcwd()
pardir = os.path.abspath(os.path.join(directory, os.pardir))

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the FileUpload index")

#def uploaded_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            pdf = request.FILES['file']
#            pdf_file = Document.objects.create(file=pdf)
#            pdf_path = pdf_file.file.path
#            #identify_skills(request.FILES['file'])
#            return render(request,'login.html',{'pdf_path':pdf_path})
#        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#            form = UploadFileForm()
#        return render(request,'FileUpload/FileUpload.html',{'form':form})
#    
#    if request.method == 'GET':
#        form = UploadFileForm()
#        return render(request,'FileUpload/FileUpload.html',{'form':form})

def uploadfile(request):
       
    if request.method == 'POST':
        
        #lastfile = Document.objects.last()
        filepath = pardir + '/media/files'
        filename = ''

        form = UploadFileForm(request.POST or None, request.FILES or None)

        context = {'filepath':filepath,
                   'form':form,
                   'filename':filename
        }

        if form.is_valid():
            form.save()

        return redirect('openaioutput')
    if request.method == 'GET':
        #lastfile = Document.objects.last()
        filepath = pardir + '/media/files'
        filename = ''

        form = UploadFileForm(request.POST or None, request.FILES or None)

        context = {'filepath':filepath,
                   'form':form,
                   'filename':filename
        }
        
        return render(request,'FIleUpload/FIleUpload.html',context)

def openaioutput(request):
    if request.method == 'GET':
        current_user = request.user
        # Identify skills for the latest uploaded fileait
        output = identify_skills()
        skill_object = Skills.objects.create(user=current_user,name=Document.objects.last(),skill_list=output)
        skill_object.save()
        return redirect('jobs_suggested')

def jobs_suggested(request):
    if request.method == 'GET':
        output = calculate_cosine_similarity()
        job_object = JobRec.objects.create(user=request.user,user_skills=Skills.objects.last(),job_recs=output)
        job_object.save()
        return HttpResponse(output)
    
class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        detail = [ {"file":detail.file}
        for detail in Document.objects.all()]
        return Response(detail)
    
    def post(self,request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)