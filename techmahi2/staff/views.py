from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def is_admin(request):
    return True if request.user.is_staff else False

def is_superuser(request):
    return True if request.user.is_superuser else False

def home(request):
    context = {
        'active_employ' : Employee.objects.filter(status=True).count(),
        'inactive_employ' : Employee.objects.filter(status=False).count()     
    }            

    return render(request, 'staff/dashboard.html', context)


def student_view(request):
    if not is_admin(request):
        messages.error(request, 'Your don not have access', extra_tags='red')
        return HttpResponseRedirect('/home/')
    form = Employee.objects.filter(status=False)
    edu_form = Education.objects.all()
    return render(request, 'staff/student_view.html', {'form':form, 'edu_form':edu_form})
    
def ActiveEmployee(request):
    if not is_admin(request):
        messages.error(request, 'Your don not have access', extra_tags='red')
        return HttpResponseRedirect('/home/')
    form = Employee.objects.filter(status=True)
    return render(request, 'staff/student_view.html', {'form':form})

def student_view1(request, p_id):
    if not is_admin(request):
        return HttpResponseRedirect('/home/')

    context = {
        'form_p':Employee.objects.get(id = p_id),
        'form':Education.objects.filter(name_id = p_id).exclude(education__isnull=True),
        'countries_travelled' : Countries_travelled.objects.filter(employee_id = p_id).exclude(country_travelled__isnull=True),
        'countries_refused' : Countries_refused.objects.filter(employee_id = p_id).exclude(country__isnull=True),
        'language_form' : Languages.objects.filter(employee_id = p_id).exclude(language__exact=''),        
        'present' : Present_address.objects.get(employee_id = p_id),
        'permanent' : Permanent_address.objects.get(employee_id = p_id),
        'employee_history' : Employee_history.objects.filter(employee_id = p_id).exclude(name__isnull=True),
        'previous_Employment' : Previous_Employment.objects.filter(employee_id = p_id).exclude(name__isnull=True),
        'reference' : Reference.objects.filter(employee_id = p_id).exclude(name__isnull=True),
        'general' : General.objects.filter(employee_id = p_id).exclude(name_of_company__isnull=True),
        'emoluments' : Emoluments.objects.filter(employee_id = p_id),
        'persanal_detailForm' : Persanal_detail.objects.filter(employee_id = p_id),
        'associates_addressForm' : Associates_address.objects.filter(employee_id = p_id).exclude(building_apt_name__isnull=True),
        'declaration_form' : Candidate_declaration_form.objects.filter(employee_id = p_id),
        'candidate_acceptance' : Candidate_acceptance_form.objects.filter(employee_id = p_id),
        
    }
    
    return render(request, 'staff/student_view1.html', context)
