from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import QueryDict, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

from django_gentoo_pkg.simple_qa.models import QAReport
from django_gentoo_pkg.simple_qa.forms import SimpleSearch, AdvancedSearch
from django_gentoo_pkg.simple_qa.forms import QAReportForm

# Notes, if using MySQL as the database backend, substitute icontains for
# search in the QuerySet calls. It is allegedly much faster due to indexing.

def home(request):
    return_dict = {}
    return_dict['menu_arches'] = get_arches()
    return render_to_response('simple_qa/bluestrike_home.html', return_dict, 
        context_instance=RequestContext(request))


def report_detail(request, report_id):
    return_dict = {}
    return_dict['menu_arches'] = get_arches()
    report = QAReport.objects.get(id__iexact=report_id)
    return_dict['qareport'] = report
    return render_to_response('simple_qa/bluestrike_detail.html', return_dict, 
                              context_instance=RequestContext(request))


def search_advanced(request):
    # Returns a list of QAReport objects matching the form query.
    return_dict = {}
    return_dict['menu_arches'] = get_arches()

    if request.method == 'GET':
        form = AdvancedSearch(request.GET)
        if form.is_valid():
            query_string = form.cleaned_data['query']
            queries = query_string.split()
            query_fields = form.cleaned_data['fields']

            queryset = QAReport.objects.all()
            queryset_list = []
            for query in queries:
                if 'category' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(category__icontains=query)))
                if 'package' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(package__icontains=query)))
                if 'version' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(version__icontains=query)))
                if 'keywords' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(keywords__icontains=query)))
                if 'qa_class' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(qa_class__icontains=query)))
                if 'short_desc' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(short_desc__icontains=query)))
                if 'arch' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(arch__icontains=query)))
                if 'threshold' in query_fields:
                    queryset_list.append(queryset.filter(
                                            Q(threshold__icontains=query)))

            matches = []
            for qset in queryset_list:
                matches = matches + list(qset)
            matches = set(matches)

            paginator = Paginator(list(matches), 30)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                result_page = paginator.page(page)
            except (EmptyPage, InvalidPage):
                result_page = paginator.page(paginator.num_pages)

            return_dict['result_page'] = result_page
            return_dict['form'] = form
            return_dict['result_message'] = (
                "Results for '%s' in the %s field:" % (
                query_string, " ".join(query_fields)))
            return_dict['get_string'] = request.GET.urlencode()
            return_dict['page'] = page
            return_dict['fields'] = request.GET.getlist('fields')
            query_dict = request.GET.copy()
            try:
                del query_dict['page']
            except KeyError:
                pass
            return_dict['query_url'] = query_dict.urlencode()

        else: # Form is not valid.
            pass

        if form.is_bound:
            return_dict['form'] = form
        else:
            return_dict['form'] = AdvancedSearch()

    elif request.method == 'POST':
        pass
    else:
        return_dict['form'] = AdvancedSearch()

    return render_to_response('simple_qa/bluestrike_search.html', return_dict, 
                              context_instance=RequestContext(request))


def search(request):
    # Returns a list of QAReport objects matching the form query.
    return_dict = {}
    return_dict['menu_arches'] = get_arches()

    if request.method == 'GET':
        form = SimpleSearch(request.GET)

        if form.is_valid():
            query_string = form.cleaned_data['query']
            queries = query_string.split()
            queryset = QAReport.objects.all()

            for query in queries:
                q = (Q(category__icontains=query) | 
                     Q(package__icontains=query) | 
                     Q(version__icontains=query) | 
                     Q(keywords__icontains=query) | 
                     Q(qa_class__icontains=query))

                queryset = queryset.filter(q)

            results = list(queryset)

            if results:
                result_message = ("Results for '%s':" % 
                                   (query_string))
            else:
                result_message = ("No results for '%s'!" % query_string)

            obj_per_page = 30 # Show 30 reports per page
            paginator = Paginator(results, obj_per_page) 
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                result_page = paginator.page(page)
            except (EmptyPage, InvalidPage):
                result_page = paginator.page(paginator.num_pages)

            return_dict['result_message'] = result_message
            return_dict['result_page'] = result_page
            return_dict['query_string'] = query_string
            return_dict['form'] = form

            query_dict = request.GET.copy()
            try:
                del query_dict['page']
            except:
                pass
            return_dict['query_url'] = query_dict.urlencode()

        else:
            return_dict['result_message'] = (
                "No results to display. :(")
            return_dict['form'] = form
    else:
        form = SimpleSearch()
        return_dict['form'] = form

    return render_to_response('simple_qa/bluestrike_search.html', return_dict, 
        context_instance=RequestContext(request))


def reports(request, arch, category=None, package=None):
    return_dict = {}
    return_dict['menu_arches'] = get_arches()
    q = Q(arch__icontains='n/a')
    reports = QAReport.objects.exclude(q)
    # We want objects which have 'arch' in their arch field, surrounded by
    # nothing other than nothing and ' '.
    reports = reports.filter(arch__regex=r'\s*'+arch+r'\s*$')
    if reports:
        if category:
            return_dict['category'] = category
            reports = reports.filter(category__iexact=category)
            pass
            if package:
                return_dict['package'] = package
                reports = reports.filter(package__iexact=package)
                pass

    reports = list(reports)
    paginator = Paginator(reports, 30) 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        result_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        result_page = paginator.page(paginator.num_pages)

    return_dict['result_page'] = result_page
    return_dict['arch'] = arch
    return render_to_response('simple_qa/bluestrike_reports.html', return_dict,
        context_instance=RequestContext(request))


def arches(request):
    return_dict = {}
    #q = (Q(arch__icontains='n/a') | Q(arch__icontains=' '))
    #reports = QAReport.objects.exclude(q)
    #arches = sorted(set(reports.values_list('arch', flat=True)))
    arches = get_arches()
    return_dict['arches'] = arches
    return_dict['menu_arches'] = arches
    return render_to_response('simple_qa/bluestrike_arches.html', return_dict, 
        context_instance=RequestContext(request))


def search_model(request):
    return_dict = {}
    return_dict['menu_arches'] = get_arches()
    if request.method == 'GET':
        form = QAReportForm(request.GET)
        if form.is_valid():
            pass
        else:
            return_dict['form'] = form
    elif request.method == 'POST':
        pass
    else:
        return_dict['form'] = QAReportForm()
    return render_to_response('simple_qa/bluestrike_search.html', return_dict, 
                              context_instance=RequestContext(request))


def get_arches():
    q = (Q(arch__icontains='n/a') | Q(arch__icontains=' '))
    reports = QAReport.objects.exclude(q)
    arches = sorted(set(reports.values_list('arch', flat=True)))
    return arches
