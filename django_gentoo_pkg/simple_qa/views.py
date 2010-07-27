from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django_gentoo_pkg.simple_qa.models import QAReport
#from django_gentoo_pkg.simple_qa.models import Package
from django_gentoo_pkg.simple_qa.forms import SearchForm
# Note about querying the databases: if using MySQL, do not chain queries.
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def public(request):
    content = 'simple_qa!'
    return render_to_response('simple_qa/index.html', locals())


def qareports(request):
    qareports = QAReport.objects.all()
    paginator = Paginator(qareports, 20) # Show 20 qareports per page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        obj_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        obj_page = paginator.page(paginator.num_pages)

    return render_to_response('simple_qa/qareports.html', locals())


from django.db.models import Q
from itertools import chain
def search(request):
    # If the page is submitted with the correct method: GET.
    if request.method == 'GET':
        # Create a form with the GET values,
        # so that the user does not have to retype anything.
        form = SearchForm(request.GET)
        # Check if the form is valid.
        if form.is_valid():
            # Prepare the query.
            query_string = form.cleaned_data['query']
            queries = query_string.split()
            queryset = QAReport.objects.all()
            # We want the results which contain all of the queries,
            # which means we want to filter the results for all queries,
            # meaning: for all queries: filter the result.
            for query in queries:
                q = (Q(category__icontains=query) | 
                     Q(package__icontains=query) | 
                     Q(version__icontains=query) | 
                     Q(keywords__icontains=query) | 
                     Q(qa_class__icontains=query))

                queryset = queryset.filter(q)

            results = list(queryset)
            if results:
                result_message = ("Results for '%s':" % query_string)
            else:
                result_message = ("No results for '%s'!" % query_string)

            # Do some Pagination
            obj_per_page = 30 # Show 30 reports per page
            paginator = Paginator(results, obj_per_page) 
            # Make sure page request is an int. If not, deliver first page.
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            # If page request is out of range, deliver last page of results.
            try:
                result_page = paginator.page(page)
            except (EmptyPage, InvalidPage):
                result_page = paginator.page(paginator.num_pages)

    # Else create a new form.
    else:
        form = SearchForm()
    return render_to_response('simple_qa/search.html', locals())
