from django.conf.urls.defaults import *


urlpatterns = patterns('django_gentoo_pkg.pkgcore.views',
    (r'^$', 'index'),
    (r'^category/$', 'category'),
    (r'^detail/$', 'detail'),
)
