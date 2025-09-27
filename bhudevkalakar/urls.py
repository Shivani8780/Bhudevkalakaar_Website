from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from old_project.old_admin import old_admin_site

urlpatterns = [
    # New project admin
    path('admin/', admin.site.urls),

    # Main site URLs
    path('', include('main.urls')),

    # Old project admin under /old-admin/
    path('old-admin/grappelli/', include('grappelli.urls')),
    path('old-admin/admin/', old_admin_site.urls),  # ✅ custom admin
    path('old-admin/', include('old_project.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
