from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
]

urlpatterns += staticfiles_urlpatterns()
