from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Home page")
    return render(request, 'main/index.html')

def about(request):
    print(str(request))
    return HttpResponse("About page")