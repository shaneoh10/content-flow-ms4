from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("posts/", include("posts.urls")),
    path("tokens/", include("tokens.urls")),
    path("profiles/", include("profiles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "content_flow.views.error_404"
handler500 = "content_flow.views.error_500"
