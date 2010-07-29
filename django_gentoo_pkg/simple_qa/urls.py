from django.conf.urls.defaults import *
from django.views.generic import list_detail
from simple_qa.models import QAReport
from simple_qa.views import *
from django.conf import settings


qareport_dict = {'queryset': QAReport.objects.all(),
             'template_object_name' : 'qareport',
             'paginate_by': 50,
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, qareport_dict),
    #(r'^qareports/page(?<page>[0-9]+)/$', qareports),
    (r'^qareports/$', qareports),
    (r'^search/$', search),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
