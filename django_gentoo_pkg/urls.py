from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django_gentoo_pkg.pkgcore.views',
    (r'^pkgcore/$', 'index'),
    (r'^pkgcore/results/$', 'results'),
    (r'^pkgcore/path/$', 'path'),
    # Example:
    # (r'^django_gentoo_pkg/', include('django_gentoo_pkg.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
