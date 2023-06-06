from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .functions.functions import read_file

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
        return render(request,'upload.html',{'form':form})

