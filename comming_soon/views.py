from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    """Render HTTML page"""
    #return HttpResponse("Hello world")
    return render(request, 'pages/comming_soon.html')

