from django.conf.urls.defaults import *
from simple_qa.models import QAReport


info_dict = {'queryset': QAReport.objects.all(),}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    #url(r'^(?P<object_id>\d+)results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='simple_qa/results.html'), 'simple_qa_results'),
)


# ----
#urlpatterns = patterns('django_gentoo_pkg.simple_qa.views',
    ##(r'^$', 'index'),
    #(r'^$', 'search_qareport'),
    ##(r'^search/$', 'search_package'),
    #(r'^search_qareport/$', 'search_qareport'),
#)
