from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # user  management
    path('accounts/', include('allauth.urls')),
    # app development
    path('', include('store.urls')),
]
