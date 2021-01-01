from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from photoGallary.models import photo
from photoGallary.api.serializers import photoSerializer


@api_view(['GET', ])
def get_detail(request, pk):
    """Get person details """
    try:
        person_data = photo.objects.get(id=pk)
    except person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = photoSerializer(person_data)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=404)


@api_view(['GET', ])
def get_all(request):
    """Get person details """
    try:
        person_data = photo.objects.all()
    except photo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = photoSerializer(person_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=404)

