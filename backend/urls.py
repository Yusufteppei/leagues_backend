from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('auth/jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('leagues/', include('leagues.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
