from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views import static
from basicbank import views
from django.views.static import serve
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('admin/', admin.site.urls),
    path('', include('basicbank.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

