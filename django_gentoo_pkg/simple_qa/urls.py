from django.conf.urls.defaults import *
from django.views.generic import list_detail
from simple_qa.models import QAReport
from simple_qa.views import *
from django.conf import settings


qareport_info = {'queryset': QAReport.objects.all(),
             'template_object_name' : 'qareport',
             'paginate_by': 50,
}


urlpatterns = patterns('',
    (r'^$', home),
    (r'^search/$', search),
    (r'^search/advanced/$', search_advanced),
    (r'^search/model/$', search_model),
    (r'^reports/id/(?P<report_id>\d+)/$', report_detail),
    (r'^reports/(?P<arch>\S+)/(?P<category>\S+)/(?P<package>\S+)/$', 
        reports),
    (r'^reports/(?P<arch>\S+)/(?P<category>\S+)/$', reports),
    (r'^reports/(?P<arch>\S+)/$', reports),
    (r'^reports/$', arches),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
