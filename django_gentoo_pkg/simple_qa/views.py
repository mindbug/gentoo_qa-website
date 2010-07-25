from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django_gentoo_pkg.simple_qa.models import QAReport
#from django_gentoo_pkg.simple_qa.models import Package
from django_gentoo_pkg.simple_qa.forms import SearchForm
# Note about querying the databases: if using MySQL, do not chain queries.


def index(request):
    content = 'simple_qa!'
    return render_to_response('simple_qa/index.html', locals())


#def search_package(request):
    ## If the page is "posted", i.e. the form is submitted.
    #if request.method == 'POST':
        ## Create a form with the "posted" values,
        ## so that the user does not have to retype anything.
        #form = SearchForm(request.POST)
        ## Check if the form is valid.
        #if form.is_valid():
            #result_message = "".join(
                    #["Results for ", form.cleaned_data['query'], ":"])
            #results = Package.objects.filter(
                    #name__icontains=form.cleaned_data['query'])
    ## Else create a new form.
    #else:
        #form = SearchForm()
    #return render_to_response('simple_qa/search_package.html', locals())


def search_qareport(request):
    # If the page is "posted", i.e. the form is submitted.
    if request.method == 'POST':
        # Create a form with the "posted" values,
        # so that the user does not have to retype anything.
        form = SearchForm(request.POST)
        # Check if the form is valid.
        if form.is_valid():
            result_message = "".join(
                    ["Results for ", form.cleaned_data['query'], ":"])
            results = []
            results.append(QAReport.objects.filter(
                    #package__package__icontains=form.cleaned_data['query']))
                    package__icontains=form.cleaned_data['query']))
    # Else create a new form.
    else:
        form = SearchForm()
    return render_to_response('simple_qa/search_qareport.html', locals())


def detail(request, object_id):
    p = get_object_or_404(QAReport, pk=object_id)
    return render_to_response('simple_qa/qareport_detail.html', 
                              {'qareport': p})
