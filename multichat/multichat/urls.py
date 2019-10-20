from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.decorators.csrf import csrf_exempt
from chat.views import index


urlpatterns = [
    path('', index),
    path('accounts/login/', csrf_exempt(login)),
    path('accounts/logout/', logout),
    path('admin/', admin.site.urls),
]
