from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import QueryDict, Http404

from django_gentoo_pkg.simple_qa.models import QAReport
from django_gentoo_pkg.simple_qa.forms import SimpleSearch, AdvancedSearch
from django_gentoo_pkg.simple_qa.forms import QAReportForm
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


def qareport_detail(request, qareport_id):
    return_dict = {}
    qareport = QAReport.objects.get(id__iexact=qareport_id)
    return_dict['qareport'] = qareport
    return render_to_response('simple_qa/qareport.html', return_dict)


from django.db.models import Q
from itertools import chain


def advanced_search(request):
    # Return:
    # return_dict['form']
    # return_dict['result_message']
    # return_dict['result_page']
    return_dict = {}

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
            #query_dict = query_dict.copy()
            try:
                del query_dict['page']
            except KeyError:
                pass
            #query_dict.appendlist(request.GET.getlist('query'))
            #query_dict.appendlist(request.GET.getlist('fields').urlencode())
            return_dict['query_url'] = query_dict.urlencode()

        else:
            pass

        return_dict['form'] = form

    elif request.method == 'POST':
        pass
    else:
        return_dict['form'] = AdvancedSearch()

    return_dict['css_url'] = "../../media/css/base_wave.css"
    return render_to_response('simple_qa/search.html', return_dict)


def simple_search(request):
    return_dict = {}

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

            return_dict = {'result_message': result_message,
                           'result_page': result_page,
                           'query_string': query_string,
                           'form': form}

            query_dict = request.GET.copy()
            try:
                del query_dict['page']
            except:
                pass
            return_dict['query_url'] = query_dict.urlencode()

        else:
            return_dict = {'result_message': "The entry is not valid.",
                           'form': form}
    else:
        form = SimpleSearch()
        return_dict = {'form': form}

    return_dict['css_url'] = "../media/css/base_wave.css"
    return render_to_response('simple_qa/search.html', return_dict)


def model_search(request):
    return_dict = {}
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
    return_dict['css_url'] = "../../media/css/base_wave.css"
    return render_to_response('simple_qa/search.html', return_dict)
