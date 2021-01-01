from django.shortcuts import render
from .models import photo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='loginPage')
def homepage(request):
    """Render HTTML page"""
    context = photo.objects.all()
    return render(request, 'gallery.html', {'data': context})
