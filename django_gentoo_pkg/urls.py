from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^pkgcore/', include('django_gentoo_pkg.pkgcore.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^simple_qa/', include('django_gentoo_pkg.simple_qa.urls')),
)
