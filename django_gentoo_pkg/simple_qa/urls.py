from django.conf.urls.defaults import *


urlpatterns = patterns('django_gentoo_pkg.simple_qa.views',
    (r'^$', 'index'),
    (r'^search/$', 'search_package'),
    (r'^search_qareport/$', 'search_qareport'),
)
