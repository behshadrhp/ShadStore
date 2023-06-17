from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # user  management
    path('accounts/', include('django.contrib.auth.urls')),
    # app development
    path('accounts/', include('accounts.urls')),
    path('', include('store.urls')),
]
