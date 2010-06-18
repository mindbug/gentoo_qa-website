# Create your views here.
# View is a web page in a Django application that serves a specific 
# function and has a specific template.
# Each View is represented by a function, with the same name as 
# referenced in urls.py.

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Search form
def index(request):
    # return render_to_response('pkgcore/index.html')
    return HttpResponse("This is the search form.")

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
