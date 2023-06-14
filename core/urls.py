from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # user  management
    path('account/', include('django.contrib.auth.urls')),
    # app development
    path('account/', include('account.urls')),
    path('', include('store.urls')),
]
