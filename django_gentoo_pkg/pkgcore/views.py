from django.shortcuts import render_to_response


def index(request):
    content = 'oh, hai thar!'
    return render_to_response('pkgcore/index.html', locals())


# QA details about a package.
def detail(request):
    return render_to_response('pkgcore/detail.html', locals())


def category(request):
    return HttpResponse("This is the category.")
