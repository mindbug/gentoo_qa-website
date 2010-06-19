from django.shortcuts import render_to_response


def index(request):
    content = 'oh, hai thar!'
    return render_to_response('pkgcore/index.html', locals())


# Results from the search
def results(request):
    return HttpResponse("This is the results of your search.")


# Path, search by
def path(request):
    # This view should parse the url and return a page that
    # is rendered from searching the packages with the full
    # name matching the url. For example, the url 
    # http://gentoo-pkg/pkgcore/dev-python/snakeoil/
    # would render a view just as if the string
    # dev-python/snakeoil, or , just snakeoil,
    # had been entered in the index (search) View above.
    # This also makes it easy to bookmark packages.
    return HttpResponse("This is the results of a quick path search query.")
