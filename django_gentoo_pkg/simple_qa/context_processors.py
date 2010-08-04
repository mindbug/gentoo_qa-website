def media_url(request):
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL,
            'detail_url': '/simple_qa/qareports/',
            'search_url': '/simple_qa/search/',
    }
