from django.shortcuts import render
from .models import photo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='loginPage')
def homepage(request):
    """Render HTTML page"""
    # context = {}
    #context['data'] = photo.objects.all()
    response = requests.get('http://www.scloud24.com/api/photogallary/v1/getall/')
    context = response.json()
    # if request.method == 'POST':
    #     value = request.POST.get('value')

    return render(request, 'gallery.html', {'data': context})
