""" UTgram URls """

from django.contrib import admin
from django.urls import path


from posts import views as posts_views


urlpatterns = [
    # path('admin/', admin.site.urls),


    # Posts views
    path('feed/', posts_views.list_post)
]
