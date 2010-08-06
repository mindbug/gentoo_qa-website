def media_url(request):
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL,
            'base_url': '/simple_qa/',
            'reports_url': '/simple_qa/reports/',
            'detail_url': '/simple_qa/reports/id/',
            'search_url': '/simple_qa/search/',
    }
