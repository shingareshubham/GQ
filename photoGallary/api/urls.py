from django.urls import path
from photoGallary.api.views import (
    get_detail,
    get_all,
)

urlpatterns = [
    path('get/<int:pk>/', get_detail),
    path('getall/', get_all),
]
