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
    (r'^$', list_detail.object_list, qareport_info),
    (r'^qareports/(?P<qareport_id>\d+)/$', qareport_detail),
    (r'^qareports/$', list_detail.object_list, qareport_info),
    (r'^search/advanced/$', advanced_search),
    (r'^search/test/$', model_search),
    (r'^search/$', simple_search),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
