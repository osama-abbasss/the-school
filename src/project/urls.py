from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('accounts.urls', namespace='account')),
    path('file/', include('files.urls', namespace='files')),
    path('group/', include('groups.urls', namespace='groups')),
    path('post/', include('posts.urls', namespace='posts')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
