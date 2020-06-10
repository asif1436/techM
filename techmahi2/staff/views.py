from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def home(request):
    return render(request, 'student/thankq.html')


def student_view(request):
    form = Employee.objects.all()

    return render(request, 'student/student_view.html', {'form':form})

def student_view1(request, p_id):
    form_p = Employee.objects.get(id = p_id)
    form = Education.objects.filter(name_id = p_id) 
    return render(request, 'student/student_view1.html', {'form_p':form_p, 'form':form})



def student(request):
    education_form_set = formset_factory(EducationForm, extra=5)
    countries_travelledForm_set = formset_factory(Countries_travelledForm, extra=3)
    countries_refusedForm_set = formset_factory(Countries_refusedForm, extra=3)
    languagesForm_set = formset_factory(LanguagesForm, extra=3)
    referenceForm_set = formset_factory(ReferenceForm, extra=3)
    generalForm_set = formset_factory(GeneralForm, extra=3)
    associates_addressForm = formset_factory(Associates_addressForm, extra=4)

    if request.method == 'POST':
        try:
            employee_form = EmployeeForm(request.POST , request.FILES)
            education_form = education_form_set(request.POST)
            # check whether it's valid:
            print("befor valid")
            if all([employee_form.is_valid(), education_form.is_valid()]):
                # get basemodel values
                
                employee_form.instance.modified_by = request.user
                e_user = employee_form.save(commit = False)                
                e_user.save()

                for ef in education_form :
                    f = ef.save(commit=False)
                    f.name = e_user
                    f.save()
                
                messages.success(request, 'Employee added successfully', extra_tags='green')
                return render(request, 'student/thankq.html')

            else:
                messages.error(request, 'Employee adding failed!', extra_tags='red')
                return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
            # invalid something!
        
        except IntegrityError as e:
            messages.error(request, 'There was a problem adding the Staff - please try again', extra_tags='red')
            return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
    # if a GET (or any other method) we'll create a blank form
    else:
        employee_form = EmployeeForm()
        edu_form = education_form_set()
        countries_travelled = countries_travelledForm_set()
        countries_refused = countries_refusedForm_set()
        language_form = languagesForm_set()
        employee_history = Employee_historyForm()
        previous_Employment = Previous_EmploymentForm()
        reference = referenceForm_set()
        general = generalForm_set()
        emoluments = EmolumentsForm()


        context = { 'mode': 'Add',
        'form_p':employee_form,
        'edu_form':edu_form,
        'countries_travelled' : countries_travelled,
        'countries_refused' : countries_refused,
        'language_form' : language_form,
        'employee_history' : employee_history,
        'previous_Employment' : previous_Employment,
        'reference' : reference,
        'general' : general,
        'emoluments' : emoluments,
        'present_address' : Present_addressForm(),
        'permanent_address' : Permanent_addressForm(),
        'persanal_detailForm' :persanal_detailForm(),
        'associates_addressForm' : associates_addressForm(),
        'candidate_acceptance' : Candidate_acceptance_formForm()

        }
        # paginator = Paginator(form_list, 2)
        # page_no = request.GET.get('page')
        # try:
        #     form_p = paginator.page(page_no)
        # except PageNotAnInteger:
        #     form_p = paginator.page(1)
        # except EmptyPage:
        #     form_p = paginator.page(paginator.num_pages)
        return render(request, 'student/add_student1.html', context)



def demo(request):
    education_form_set = formset_factory(EducationForm, extra=3)
    
    edu_form = education_formset()
    if request.method == 'POST':
        edu_form = education_formset(request.POST)
        if all([edu_form.is_valid()]):
            for form in edu_form :
                form.save()
            messages.success(request, 'Employee added successfully', extra_tags='green')
            return render(request, 'student/thankq.html')
    context = {
        ""
    }

    return render(request, 'student/manage_children.html', {'edu_form': edu_form})