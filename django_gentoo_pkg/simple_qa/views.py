from django.shortcuts import render_to_response
from django.template import RequestContext

from django_gentoo_pkg.simple_qa.models import Package, QAReport
from django_gentoo_pkg.simple_qa.models import SearchForm


def index(request):
    content = 'simple_qa!'
    return render_to_response('simple_qa/index.html', locals())


def search(request):
    # If the page is "posted", i.e. the form is submitted.
    if request.method == 'POST':
        # Create a form with the "posted" values.
        form = SearchForm(request.POST)
        # Check if the form is valid.
        if form.is_valid():
            result_message = "".join(["Results for ",
                                      form.cleaned_data['query'],
                                      ":"])
            results = Package.objects.filter(
                            name__icontains=form.cleaned_data['query'])
    # Else create a new form.
    else:
        form = SearchForm()
    return render_to_response('simple_qa/search.html', locals())
