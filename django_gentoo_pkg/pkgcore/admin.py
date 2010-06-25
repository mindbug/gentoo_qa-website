from django_gentoo_pkg.pkgcore.models import *
from django.contrib import admin

admin.site.register(Package)
admin.site.register(QAReport)
admin.site.register(Maintainer)
admin.site.register(Repository)
