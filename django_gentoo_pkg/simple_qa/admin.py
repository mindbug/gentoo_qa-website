from django_gentoo_pkg.simple_qa.models import *
from django.contrib import admin


#admin.site.register(Package)

#admin.site.register(QAReport)
class QAReportAdmin(admin.ModelAdmin):
    fieldsets = [('Package information', {'fields': ['category', 'package', 
                                                    'version']}), 
                 ('QA information', {'fields': ['keywords', 'qa_class']})]
    list_display = ('category', 'package', 'version', 'keywords', 'qa_class')
    list_filter = ['qa_class']
    search_fields = ['category', 'package', 'version', 'keywords', 'qa_class']

admin.site.register(QAReport, QAReportAdmin)
