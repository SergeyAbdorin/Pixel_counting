from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.urls import include
from django.contrib import admin
from django.urls import path

handler404 = "backend.views.page_not_found"
handler500 = "backend.views.server_error"

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path("", include("backend.urls"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
