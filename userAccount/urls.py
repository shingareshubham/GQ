from django.urls import path
from .views import (
    login_view,
    register_view,
    logout_user,
)


urlpatterns = [
    path('login/', login_view, name='loginPage'),
    path('register/', register_view, name='registerPage'),
    path('logout/', logout_user, name="logoutPage"),
]
