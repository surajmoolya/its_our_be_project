from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'homepage.html')
def summarize(request):
    if request.method=='POST':
     file=request.FILES.get('file')
     print(file)
    return HttpResponse(file.name)