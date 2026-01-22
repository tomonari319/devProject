from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testApp.urls')),
]

# DEBUGモードかつdebug_toolbarがインストールされている場合のみ読み込む
if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
    except (ImportError, RuntimeError):
        # debug_toolbarの設定に不備がある、または入っていない場合は無視する
        pass