from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    # Django admin
    path('asdfowuercxvkjchvsodf-admin/', admin.site.urls),
    # user  management
    path('accounts/', include('allauth.urls')),
    # app development
    path('', include('store.urls')),
    path('books/', include('books.urls')),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  Media static
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar
if settings.DEBUG:
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

admin.site.site_header = 'ShadStore Management'
admin.site.index_title = 'Book Store Management'
admin.site.site_title = 'ShadStore'
