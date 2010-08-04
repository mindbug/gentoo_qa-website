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
    (r'^$', welcome),
    (r'^search/$', search),
    (r'^search/advanced/$', search_advanced),
    (r'^reports/id/(?P<report_id>\d+)/$', report_detail),
    (r'^reports/(?P<arch>\S+)/(?P<category>\S+)/(?P<package>\S+)/$', 
        listing),
    (r'^reports/(?P<arch>\S+)/(?P<category>\S+)/$', listing),
    (r'^reports/(?P<arch>\S+)/$', listing),
    (r'^search/model/$', search_model),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
