from django.shortcuts import render_to_response


def index(request):
    content = 'simple_qa!'
    return render_to_response('simple_qa/index.html', locals())


def search(request):
    """
    if 'q' in request.POST:
        content = 'You searched for: %r' % request.POST['q']
    else:
        content = 'You submitted an empty form.'
    return render_to_response('simple_qa/search_result.html', locals())
    """
    content = 'search result1!1'
    return render_to_response('simple_qa/search.html', locals())
