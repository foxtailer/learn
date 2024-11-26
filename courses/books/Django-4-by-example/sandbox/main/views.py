from django.shortcuts import render

# Create your views here.
def index(request):
    y = request.GET.get('y')
    z = request.GET.get('z')
    return render(request,
                  'main/index.html',
                  {'x': '@',
                   'y': y,
                   'z': z})
    #####################
    