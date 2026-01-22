from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testApp.urls')),
]

# debug_toolbarの設定
# settings.pyで 'debug_toolbar' を INSTALLED_APPS から外している場合、
# ここで import しようとするとエラーになるのを防ぐため、try-except を使います。
if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass