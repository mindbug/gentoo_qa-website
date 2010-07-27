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


from itertools import chain
def search(request):
    # If the page is "posted", i.e. the form is submitted.
    if request.method == 'GET':
        # Create a form with the "posted" values,
        # so that the user does not have to retype anything.
        form = SearchForm(request.GET)
        # Check if the form is valid.
        if form.is_valid():
            query = form.cleaned_data['query']
            category_list = QAReport.objects.filter(
                            category__icontains=query)
            package_list = QAReport.objects.filter(
                            package__icontains=query)
            version_list = QAReport.objects.filter(
                            version__icontains=query)
            keywords_list = QAReport.objects.filter(
                            keywords__icontains=query)
            qa_class_list = QAReport.objects.filter(
                            qa_class__icontains=query)
            results = list(chain(category_list, package_list, version_list,
                                 keywords_list, qa_class_list))

            if results:
                result_message = "".join(
                        ["Results for ", form.cleaned_data['query'], ":"])
            else:
                result_message = "No results for %s!" % form.cleaned_data['query']

            # Do some Pagination
            paginator = Paginator(results, 50) # Show 50 reports per page

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
