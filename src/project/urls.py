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
    path('serach/', include('searches.urls', namespace='searches')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('covid-19/', include('covid_19.urls', namespace='covid'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
