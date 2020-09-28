""" UTgram URls """

from django.contrib import admin
from django.urls import path

# Static files config
from django.conf import settings
from django.urls.static import static

from posts import views as posts_views


urlpatterns = [
    # path('admin/', admin.site.urls),


    # Posts views
    path('feed/', posts_views.list_post)
] + static(setting.MEDIA_URL, document_root=settings.MEDIA_ROOT)
