
from django.conf.urls import url, patterns, include
from django.contrib import admin
from  django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^billa/', include('apps.app1.urls'))
]

if settings.DEBUG :
    import  debug_toolbar

    urlpatterns += patterns(
        'django.view.static',
        url(r'^__debug__', include(debug_toolbar.urls) )
    )


