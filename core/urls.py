from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('finance.urls')),
    path('api/v1/', include('transactions.urls')),
    path('api/v1/', include('budgets.urls')),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('', admin.site.urls),
]
