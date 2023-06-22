from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .functions.functions import read_file
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializer import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the FileUpload index")

def uploaded_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            read_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        return render(request,'FileUpload/FileUpload.html',{'form':form})
    
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request,'FileUpload/FileUpload.html',{'form':form})
    
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