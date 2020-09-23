
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('''
        <h1>Hello World!</h1>
        <h3>Hola desde django</h3>
        ''')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello-world/',hello_world)
]
