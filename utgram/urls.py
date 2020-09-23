
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

from posts import views as posts_views


def hello_world(request):
    return HttpResponse('''
        <h1>Hola Mundo!</h1>
        <h3>Hola desde django</h3>
        ''')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello-world/',hello_world),

    # Posts views
    path('feed/', posts_views.list_post)
]
