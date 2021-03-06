import functools
import operator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import PersonForm
from .models import myRecord


def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")


def person_list(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        # Rudimentary case-insensitive search across some fields
        searching = request.POST.get('searchStr')
        if not searching:
            records_list = myRecord.objects.filter().order_by('last_nm_txt')
        else:
            q_list = [Q(last_nm_txt__icontains=searching),
                      Q(first_nm_txt__icontains=searching),
                      Q(address_street1__icontains=searching),
                      Q(phone1_number__icontains=searching),
                      ]
            records_list = myRecord.objects.filter(functools.reduce(operator.or_, q_list)).filter().order_by('add_dt')
        paginator = Paginator(records_list, 10)  # Show 10 records per page

        page = request.GET.get('page')
        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            records = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'myapp/person_list.html', {'records': records})


def person_detail(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        record = get_object_or_404(myRecord, pk=pk)
        return render(request, 'myapp/person_detail.html', {'record': record})


def person_new(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        if request.method == "POST":
            form = PersonForm(request.POST)
            if form.is_valid():
                person = form.save(commit=False)
                person.added_by = request.user
                person.edited_by = request.user
                person.edit_dt = timezone.now()
                person.save()
                return redirect('person_detail', pk=person.pk)
        else:
            form = PersonForm()
        return render(request, 'myapp/person_edit.html', {'form': form})


def person_edit(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        record = get_object_or_404(myRecord, pk=pk)
        if request.method == "POST":
            form = PersonForm(request.POST, instance=record)
            if form.is_valid():
                person = form.save(commit=False)
                # person.edited_by = request.user
                person.edit_dt = timezone.now()
                person.save()
                return redirect('person_detail', pk=person.pk)
        else:
            form = PersonForm(instance=record)
        return render(request, 'myapp/person_edit.html', {'form': form})
