from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('finance.urls')),
    path('api/v1/', include('transactions.urls')),
    path('api/v1/', include('budgets.urls')),

    path('admin/', admin.site.urls),
]
