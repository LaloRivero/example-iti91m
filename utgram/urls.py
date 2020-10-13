""" UTgram URls """

from django.contrib import admin
from django.urls import path

# Static files config
from django.conf import settings
from django.conf.urls.static import static

from posts import views as posts_views
from users import views as users_views


urlpatterns = [

    # Django
    path('admin/', admin.site.urls),

    # Posts views
    path('posts/feed/', posts_views.list_post, name='feed'),

    # Users views
    path('login/', users_views.login_view, name='login' ),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.signup, name='signup'),
    path('me/profile',users_views.update_profile, name='update_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
