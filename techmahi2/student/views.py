
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_list_or_404, get_object_or_404
from staff.models import *
from staff.forms import *
from student.forms import Student_SignUpForm
from django.db import IntegrityError
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.forms.models import modelformset_factory, inlineformset_factory
from django.core.exceptions import ValidationError
import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect

from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('home/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/student/login/')



def register(request):
    if request.method == "POST":
        signup = Student_SignUpForm(request.POST)
        if signup.is_valid():
            signup.save()
            return HttpResponseRedirect('/home/')
    signup = Student_SignUpForm()
    return render(request, 'student/register.html', {'signup': signup})




def demo(request):
    if request.method == "POST":
        e_form = EmployeeForm(request.POST, request.FILES)
        p_form = Present_addressForm(request.POST)
        per_form = Permanent_addressForm(request.POST)

        if e_form.is_valid() and p_form.is_valid() and per_form.is_valid():
            ef = e_form.save(commit=False)
            ef.save()
            pf = p_form.save(commit=False)
            pf.employee = ef
            pf.save()
            pef = per_form.save(commit=False)
            pef.employee = ef
            pef.save()

            messages.success(request, 'Employee added successfully', extra_tags='green')
            return render(request, 'student/thankq.html')

        else:
            messages.error(request, 'Employee adding failed!', extra_tags='red')
            return render(request, 'student/add_student1.html')

    else:
        e_form = EmployeeForm()
        p_form = Present_addressForm()
        per_form = Permanent_addressForm()

        context = {
            "form_p" : e_form,
            "present" : p_form,
            "permanent" : per_form
        }

        return render(request, 'student/demo.html', context)


def Active(request):
    print("asfdf")
    if request.is_ajax and request.method == "GET":
        status_id =int(request.GET.get('demo', None))
        data =  Employee.objects.get(pk=int(status_id))
        result = {}
        if data.status == False:
            data.status = True
            data.save()
            result['active'] = "True"
            print(result)
            print("^&%^*&$^#&%#^%^*&^%^&$^%#%^&*$^$^%$*&**&*^%$")
            return HttpResponse(JsonResponse(result))
        else:
            data.status = False
            data.save()
            result['deactive'] = "True"
            print(result)
            print("^&%^*&$^#&%#^%^*&^%^&$^%#%^&*$^$^%$*&**&*^%$")
            return HttpResponse(JsonResponse(result))



        # if result == "no":
        #     result = Employee.objects.get(id=result)
        #     result.status = True
        #     result.save()
        # else:
        #     result = Employee.objects.get(id=result)
        #     result.status = False
        #     result.save()

        return result



# FORMS = [('form_p', EmployeeForm),
#         ('edu_form', formset_factory(EducationForm, extra=5)),
#         ('countries_travelled', countries_travelledForm_set),
#         ('countries_refused', countries_refusedForm_set),
#         ('language_form', languagesForm_set),
#         ('present_address', Present_addressForm),
#         ('permanent_address', Permanent_addressForm),
#         ('employee_history', Employee_historyForm),
#         ('previous_Employment', Previous_EmploymentForm),
#         ('reference', referenceForm_set),
#         ('general', generalForm_set),
#         ('emoluments', EmolumentsForm)

#         ]

# TEMPLATES = {
#         'form_p' : 'student/add_student1.html',
#         'edu_form' : 'student/add_student1.html',
#         'countries_travelled': 'student/add_student1.html',
#         'countries_refused' : 'student/add_student1.html',
#         'language_form' : 'student/add_student1.html',
#         'present_address': 'student/add_student1.html',
#         'permanent_address' : 'student/add_student1.html',
#         'employee_history' : 'student/employee.html',
#         'previous_Employment' : 'student/employee.html',
#         'reference' : 'student/employee.html',
#         'general' : 'student/employee.html',
#         'emoluments' : 'student/employee.html',
#         }

# class OrderWizard(SessionWizardView):
#     file_storage = FileSystemStorage('media/photos')

#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]

#     def done(self, form_list, **kwargs):
#         do_something_with_the_form_data(form_list)
#         return HttpResponseRedirect('/page-to-redirect-to-when-done/')





@login_required
# def student(request):
#     if request.method == 'POST':
#         employee_form = EmployeeForm(request.POST , request.FILES)
#         education_form = education_form_set(request.POST, request.FILES)
#         countries_travelled = countries_travelledForm_set(request.POST)
#         countries_refused = countries_refusedForm_set(request.POST)
#         language_form   = languagesForm_set(request.POST,)
#         present_address = Present_addressForm(request.POST,)
#         permanent_address = Permanent_addressForm(request.POST,)
#         employee_history = Employee_historyForm(request.POST,)
#         previous_Employment = Previous_EmploymentForm(request.POST,)
#         reference = referenceForm_set(request.POST,)
#         general = generalForm_set(request.POST,)
#         emoluments = EmolumentsForm(request.POST,)
#         persanal_detailForm = Persanal_detailForm(request.POST,)
#         associates_addressForm = associates_addressForm_set(request.POST,)
#         declaration_form = Candidate_declaration_formForm(request.POST,)
#         candidate_acceptance = Candidate_acceptance_formForm(request.POST,)

#         print("before validation")
#         if all([employee_form.is_valid(), education_form.is_valid(), countries_travelled.is_valid(), countries_refused.is_valid(), language_form.is_valid(), present_address.is_valid(), permanent_address.is_valid(), employee_history.is_valid(), previous_Employment.is_valid(), reference.is_valid(), general.is_valid(), emoluments.is_valid(), persanal_detailForm.is_valid(), associates_addressForm.is_valid(), declaration_form.is_valid(), candidate_acceptance.is_valid()]):
#         #     print ("all are valid")

#             employ = employee_form.save(commit=False)
#             employ.save()
#             print("save 1")

#             for form in education_form:
#                 f = form.save(commit=False)
#                 f.name = employ
#                 f.save()
#                 print("save 2")

#             for form in countries_travelled:
#                 f = form.save(commit=False)
#                 f.employee = employ
#                 f.save()
#                 print("save 3")


#             for form in countries_refused:
#                 f = form.save(commit=False)
#                 f.employee = employ
#                 f.save()
#                 print("save 4")

#             for form in language_form:
#                 f = form.save(commit=False)
#                 f.employee = employ
#                 f.save()
#                 print("save 5")
#                 pa = present_address.save( commit=False)
#                 pa.employee = employ
#                 pa.save()
#                 print("save9")
#                 pe = permanent_address.save(commit=False)
#                 pe.employee = employ
#                 pe.save()
#                 print("save 10")
#                 eh = employee_history.save(commit=False)
#                 eh.employee = employ
#                 eh.save()
#                 print("save11")
#                 pee = previous_Employment.save(commit=False)
#                 pee.employee = employ
#                 pee.save()
#                 print("save 12")

#                 for form in reference:
#                     f = form.save(commit=False)
#                     f.employee = employ
#                     f.save()
#                     print("save 10")

#                 for form in general:
#                     f = form.save(commit=False)
#                     f.employee = employ
#                     f.save()
#                     print("save 11")

#                 ef = emoluments.save(commit=False)
#                 ef.employee = employ
#                 ef.save()
#                 print("save 13")


#                 pf = persanal_detailForm.save(commit=False)
#                 pf.employee = employ
#                 pf.save()
#                 print("save 14")


#                 for form in associates_addressForm:
#                     f = form.save(commit=False)
#                     f.employee = employ
#                     f.save()
#                     print("save 14")

#                 df = declaration_form.save(commit=False)
#                 df.employee = employ
#                 df.save()
#                 print("save 15")

#                 caf = candidate_acceptance.save(commit=False)
#                 caf.employee = employ
#                 caf.save()
#                 print("save 16")



#             #send_mail('New Application','New Aplication is added, Pleace go through Aplication if  every thing is  right make it Acitive', 'itsmak100@gmail.com', ['mohd.asif1436@gmail.com'], fail_silently=False)

#             messages.success(request, 'Employee added successfully', extra_tags='green')
#             return render(request, 'student/thankq.html')

#         else:
#             messages.error(request, 'Employee adding failed!', extra_tags='red')
#             return render(request, 'student/add_student1.html')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         context = {
#             'form_p':EmployeeForm(),
#             'edu_form':education_form_set(queryset=Education.objects.none()),
#             'countries_travelled' : countries_travelledForm_set(queryset=Countries_travelled.objects.none()),
#             'countries_refused' : countries_refusedForm_set(queryset=Countries_refused.objects.none()),
#             'language_form' : languagesForm_set(queryset=Languages.objects.none()),
#             'present' : Present_addressForm(),
#             'permanent' : Permanent_addressForm(),
#             'employee_history' : Employee_historyForm(),
#             'previous_Employment' : Previous_EmploymentForm(),
#             'reference' : referenceForm_set(queryset=Reference.objects.none()),
#             'general' : generalForm_set(queryset=General.objects.none()),
#             'emoluments' : EmolumentsForm(),
#             'persanal_detailForm' : Persanal_detailForm(),
#             'associates_addressForm' : associates_addressForm_set(queryset=Associates_address.objects.none()),
#             'declaration_form' : Candidate_declaration_formForm(),
#             'candidate_acceptance' : Candidate_acceptance_formForm()

#         }

#         return render(request, 'student/add_student1.html', context)


# def edit_student(request, p_id):
#     eb = Employee.objects.get(id = p_id)
#     pab = Present_address.objects.filter(employee_id = p_id).first()
#     peb = Permanent_address.objects.filter(employee_id = p_id).first()
#     ehb = Employee_history.objects.filter(employee_id = p_id).first()
#     pemb = Previous_Employment.objects.filter(employee_id = p_id).first()
#     emb = Emoluments.objects.filter(employee_id = p_id).first()
#     pdb = Persanal_detail.objects.filter(employee_id = p_id).first()
#     db = Candidate_declaration_form.objects.filter(employee_id = p_id).first()
#     cb = Candidate_acceptance_form.objects.filter(employee_id = p_id).first()

#     if request.method == "POST":
#         form_p=EmployeeForm(request.POST, request.FILES, instance=eb)
#         edu_form=education_form_set( request.POST, request.FILES, queryset = Education.objects.filter(name_id = eb))
#         countries_travelled = countries_travelledForm_set(request.POST, queryset = Countries_travelled.objects.filter(employee_id = p_id))
#         countries_refused = countries_refusedForm_set( request.POST, queryset = Countries_refused.objects.filter(employee_id = p_id))
#         language_form = languagesForm_set(request.POST, queryset = Languages.objects.filter(employee_id = p_id))
#         present_address = Present_addressForm(request.POST, instance= pab)
#         permanent_address = Permanent_addressForm( request.POST, instance= peb)
#         employee_history = Employee_historyForm(request.POST, instance = ehb)
#         previous_Employment = Previous_EmploymentForm( request.POST, instance = pemb)
#         reference = referenceForm_set( request.POST, queryset = Reference.objects.filter(employee_id = p_id))
#         general = generalForm_set( request.POST, queryset = General.objects.filter(employee_id = p_id))
#         emoluments = EmolumentsForm( request.POST, instance = emb)
#         persanal_detailForm = Persanal_detailForm( request.POST, instance = pdb)
#         associates_addressForm = associates_addressForm_set( request.POST, queryset = Associates_address.objects.filter(employee_id = p_id))
#         declaration_form = Candidate_declaration_formForm( request.POST, instance = db)
#         candidate_acceptance = Candidate_acceptance_formForm( request.POST, instance = cb)

#         if form_p.is_valid():
#             f = form_p.save(commit=False)
#             f.save()
#             print("first")
#             if edu_form.is_valid():
#                 ef = edu_form.save(commit=False)
#                 for f in ef:
#                     f.name_id = f
#                     f.save()
#                     print("save1")

#             if countries_travelled.is_valid():
#                 cf = countries_travelled.save(commit=False)
#                 for cf in cf:
#                     cd.employee_id = f
#                     cd.save()
#                     print("save2")

#             if countries_refused.is_valid():
#                 cr = countries_refused.save(commit=False)
#                 for cr in cr:
#                     cr.employee_id = f
#                     cr.save()
#                     print("save3")

#             if language_form.is_valid():
#                 lf = language_form.save(commit=False)
#                 for l in lf:
#                     l.employee_id = f
#                     l.save()
#                     print("save4")

#             if present_address.is_valid():
#                 pd = present_address.save(commit=False)
#                 pd.employee_id = f
#                 pd.save()
#                 print("save5")

#             if permanent_address.is_valid():
#                 pd = permanent_address.save(commit=False)
#                 pd.employee_id = f
#                 pd.save()
#                 print("save6")

#             if employee_history.is_valid():
#                 eh = employee_history.save(commit=False)
#                 eh.employee_id = f
#                 eh.save()
#                 print("save7")

#             if previous_Employment.is_valid():
#                 pe = previous_Employment.save(commit=False)
#                 pe.employee_id = f
#                 pe.save()
#                 print("save8")

#             if reference.is_valid():
#                 rf = reference.save(commit=False)
#                 for rf in rf:
#                     rf.employee_id = f
#                     rf.save()
#                     print("save9")

#             if general.is_valid():
#                 g = general.save(commit=False)
#                 for g in g:
#                     g.employee_id = f
#                     g.save()
#                     print("save10")


#             if emoluments.is_valid():
#                 emo = emoluments.save(commit=False)
#                 emo.employee_id =f
#                 emo.save()
#                 print("save11")

#             if persanal_detailForm.is_valid():
#                 pdf = persanal_detailForm.save(commit=False)
#                 pdf.employee_id = f
#                 pdf.save()
#                 print("save12")

#             if associates_addressForm.is_valid():
#                 adf = associates_addressForm.save(commit=False)
#                 for adf in adf:
#                     adf.employee_id = f
#                     adf.save()
#                     print("save13")


#             if declaration_form.is_valid():
#                 df = declaration_form.save(commit=False)
#                 df.employee_id = f
#                 df.save()
#                 print("save14")


#             if candidate_acceptance.is_valid():
#                 caf = candidate_acceptance.save(commit=False)
#                 caf.employee_id = f
#                 caf.save()
#                 print("save15")

#             messages.success(request, 'Employee added successfully', extra_tags='green')
#             return render(request, 'student/thankq.html')

#         else:
#             messages.error(request, 'Employee adding failed!', extra_tags='red')
#             return render(request, 'student/add_student1.html')
#     else:

#         context = {
#             'form_p':EmployeeForm(instance = eb),
#             'edu_form':education_form_set(queryset = Education.objects.filter(name_id = p_id)),
#             'countries_travelled' : countries_travelledForm_set(queryset = Countries_travelled.objects.filter(employee_id = p_id)),
#             'countries_refused' : countries_refusedForm_set(queryset = Countries_refused.objects.filter(employee_id = p_id)),
#             'language_form' : languagesForm_set(queryset = Languages.objects.filter(employee_id = p_id)),
#             'present' : Present_addressForm(instance= pab),
#             'permanent' : Permanent_addressForm(instance= peb),
#             'employee_history' : Employee_historyForm(instance = ehb),
#             'previous_Employment' : Previous_EmploymentForm(instance = pemb),
#             'reference' : referenceForm_set(queryset = Reference.objects.filter(employee_id = p_id)),
#             'general' : generalForm_set(queryset = General.objects.filter(employee_id = p_id)),
#             'emoluments' : EmolumentsForm(instance = emb),
#             'persanal_detailForm' : Persanal_detailForm(instance = pdb),
#             'associates_addressForm' : associates_addressForm_set(queryset = Associates_address.objects.filter(employee_id = p_id)),
#             'declaration_form' : Candidate_declaration_formForm(instance = db),
#             'candidate_acceptance' : Candidate_acceptance_formForm(instance = cb)

#             }

#         return render(request, 'student/add_student1.html', context)




# def Employment_history(request):
#     education_form_set = formset_factory(EducationForm, extra=5)
#     referenceForm_set = formset_factory(ReferenceForm, extra=3)
#     generalForm_set = formset_factory(GeneralForm, extra=3)

#     if request.method == 'POST':
#         try:
#             employee_form = EmployeeForm(request.POST , request.FILES)
#             education_form = education_form_set(request.POST, request.FILES)
#             # check whether it's valid:
#             print("befor valid")
#             if all([employee_form.is_valid(), education_form.is_valid()]):
#                 # get basemodel values

#                 employee_form.instance.modified_by = request.user
#                 employ = employee_form.save(commit = False)
#                 employ.save()

#                 for ef in education_form :
#                     f = ef.save(commit=False)
#                     f.name = employ
#                     f.save()

#                 messages.success(request, 'Employee added successfully', extra_tags='green')
#                 return render(request, 'student/thankq.html')

#             else:
#                 messages.error(request, 'Employee adding failed!', extra_tags='red')
#                 return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#             # invalid something!

#         except IntegrityError as e:
#             messages.error(request, 'There was a problem adding the Staff - please try again', extra_tags='red')
#             return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         context = {
#         'form_p':EmployeeForm(),
#         'employee_history' : Employee_historyForm(),
#         'previous_Employment' : Previous_EmploymentForm(),
#         'reference' : referenceForm_set(),
#         'general' : generalForm_set(),
#         'emoluments' : EmolumentsForm(),

#         }
#         # paginator = Paginator(form_list, 2)
#         # page_no = request.GET.get('page')
#         # try:
#         #     form_p = paginator.page(page_no)
#         # except PageNotAnInteger:
#         #     form_p = paginator.page(1)
#         # except EmptyPage:
#         #     form_p = paginator.page(paginator.num_pages)
#         return render(request, 'student/employee.html', context)


# def Background(request):
#     associates_addressForm = formset_factory(Associates_addressForm, extra=4)

#     if request.method == 'POST':
#         try:
#             employee_form = EmployeeForm(request.POST , request.FILES)
#             education_form = education_form_set(request.POST)
#             # check whether it's valid:
#             print("befor valid")
#             if all([employee_form.is_valid(), education_form.is_valid()]):
#                 # get basemodel values

#                 employee_form.instance.modified_by = request.user
#                 employ = employee_form.save(commit = False)
#                 employ.save()

#                 for ef in education_form :
#                     f = ef.save(commit=False)
#                     f.name = employ
#                     f.save()

#                 messages.success(request, 'Employee added successfully', extra_tags='green')
#                 return render(request, 'student/thankq.html')

#             else:
#                 messages.error(request, 'Employee adding failed!', extra_tags='red')
#                 return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#             # invalid something!

#         except IntegrityError as e:
#             messages.error(request, 'There was a problem adding the Staff - please try again', extra_tags='red')
#             return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         context = {
#         'form_p':EmployeeForm(),
#         'persanal_detailForm' :persanal_detailForm(),
#         'associates_addressForm' : associates_addressForm(),

#         }
#         # paginator = Paginator(form_list, 2)
#         # page_no = request.GET.get('page')
#         # try:
#         #     form_p = paginator.page(page_no)
#         # except PageNotAnInteger:
#         #     form_p = paginator.page(1)
#         # except EmptyPage:
#         #     form_p = paginator.page(paginator.num_pages)
#         return render(request, 'student/background.html', context)


# def Declaration(request):
#     if request.method == 'POST':
#         try:
#             employee_form = EmployeeForm(request.POST , request.FILES)
#             education_form = education_form_set(request.POST)
#             # check whether it's valid:
#             print("befor valid")
#             if all([employee_form.is_valid(), education_form.is_valid()]):
#                 # get basemodel values

#                 employee_form.instance.modified_by = request.user
#                 employ = employee_form.save(commit = False)
#                 employ.save()

#                 for ef in education_form :
#                     f = ef.save(commit=False)
#                     f.name = employ
#                     f.save()

#                 messages.success(request, 'Employee added successfully', extra_tags='green')
#                 return render(request, 'student/thankq.html')

#             else:
#                 messages.error(request, 'Employee adding failed!', extra_tags='red')
#                 return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#             # invalid something!

#         except IntegrityError as e:
#             messages.error(request, 'There was a problem adding the Staff - please try again', extra_tags='red')
#             return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         context = {
#         'form_p':EmployeeForm(),
#         'declaration_form' : Candidate_declaration_formForm()

#         }
#         # paginator = Paginator(form_list, 2)
#         # page_no = request.GET.get('page')
#         # try:
#         #     form_p = paginator.page(page_no)
#         # except PageNotAnInteger:
#         #     form_p = paginator.page(1)
#         # except EmptyPage:
#         #     form_p = paginator.page(paginator.num_pages)
#         return render(request, 'student/declaration.html', context)


# def Acceptance(request):
#     if request.method == 'POST':
#         try:
#             employee_form = EmployeeForm(request.POST , request.FILES)
#             education_form = education_form_set(request.POST)
#             # check whether it's valid:
#             print("befor valid")
#             if all([employee_form.is_valid(), education_form.is_valid()]):
#                 # get basemodel values

#                 employee_form.instance.modified_by = request.user
#                 employ = employee_form.save(commit = False)
#                 employ.save()

#                 for ef in education_form :
#                     f = ef.save(commit=False)
#                     f.name = employ
#                     f.save()

#                 messages.success(request, 'Employee added successfully', extra_tags='green')
#                 return render(request, 'student/thankq.html')

#             else:
#                 messages.error(request, 'Employee adding failed!', extra_tags='red')
#                 return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#             # invalid something!

#         except IntegrityError as e:
#             messages.error(request, 'There was a problem adding the Staff - please try again', extra_tags='red')
#             return render(request, 'student/add_student1.html', {'mode': 'Add', 'form_p':employee_form, 'edu_form':education_formset})
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         context = {
#         'form_p':EmployeeForm(),
#         'candidate_acceptance' : Candidate_acceptance_formForm(),

#         }
#         # paginator = Paginator(form_list, 2)
#         # page_no = request.GET.get('page')
#         # try:
#         #     form_p = paginator.page(page_no)
#         # except PageNotAnInteger:
#         #     form_p = paginator.page(1)
#         # except EmptyPage:
#         #     form_p = paginator.page(paginator.num_pages)
#         return render(request, 'student/acceptance.html', context)



# def student_new(request):
#     print("demo1")
#     if request.method == "POST":
#         form_p=EmployeeForm(request.POST, request.FILES)
#         edu_form=education_form_set( request.POST, request.FILES)
#         countries_travelled = countries_travelledForm_set(request.POST)
#         countries_refused = countries_refusedForm_set( request.POST)
#         language_form = languagesForm_set(request.POST)
#         present_address = Present_addressForm(request.POST)
#         permanent_address = Permanent_addressForm( request.POST)
#         employee_history = Employee_historyForm(request.POST)
#         previous_Employment = Previous_EmploymentForm( request.POST)
#         reference = referenceForm_set( request.POST)
#         general = generalForm_set( request.POST)
#         emoluments = EmolumentsForm( request.POST)
#         persanal_detailForm = Persanal_detailForm( request.POST)
#         associates_addressForm = associates_addressForm_set( request.POST)
#         declaration_form = Candidate_declaration_formForm(request.POST)
#         candidate_acceptance = Candidate_acceptance_formForm( request.POST)

#         print("demo2")
#         if form_p.is_valid():
#             f = form_p.save(commit=False)
#             f.save()
#             print("demo3")
#             if edu_form.is_valid():
#                 ef = edu_form.save(commit=False)
#                 for f in ef:
#                     f.name_id = f.id
#                     f.save()
#                     print("demo4")

#             if countries_travelled.is_valid():
#                 cf = countries_travelled.save(commit=False)
#                 for cf in cf:
#                     cd.employee_id = f.id
#                     cd.save()
#                     print("demo5")

#             if countries_refused.is_valid():
#                 cr = countries_refused.save(commit=False)
#                 for cr in cr:
#                     cr.employee_id = f.id
#                     cr.save()
#                     print("demo6")

#             if language_form.is_valid():
#                 lf = language_form.save(commit=False)
#                 for lf in lf:
#                     lf.employee_id = f.id
#                     lf.save()
#                     print("demo7")

#             if present_address.is_valid():
#                 pd = present_address.save(commit=False)
#                 pd.employee_id = f.id
#                 pd.save()
#                 print("demo8")

#             if permanent_address.is_valid():
#                 pd = permanent_address.save(commit=False)
#                 pd.employee_id = f.id
#                 pd.save()

#             if employee_history.is_valid():
#                 eh = employee_history.save(commit=False)
#                 eh.employee_id = f.id
#                 eh.save()

#             if previous_Employment.is_valid():
#                 pe = previous_Employment.save(commit=False)
#                 pe.employee_id = f.id
#                 pe.save()

#             if reference.is_valid():
#                 rf = reference.save(commit=False)
#                 for rf in rf:
#                     rf.employee_id = f.id
#                     rf.save()

#             if general.is_valid():
#                 g = general.save(commit=False)
#                 for g in g:
#                     g.employee_id = f.id
#                     g.save()


#             if emoluments.is_valid():
#                 emo = emoluments.save(commit=False)
#                 emo.employee_id =f.id
#                 emo.save()

#             if persanal_detailForm.is_valid():
#                 pdf = persanal_detailForm.save(commit=False)
#                 pdf.employee_id = f.id
#                 pdf.save()

#             if associates_addressForm.is_valid():
#                 adf = associates_addressForm.save(commit=False)
#                 for adf in adf:
#                     adf.employee_id = f.id
#                     adf.save()


#             if declaration_form.is_valid():
#                 df = declaration_form.save(commit=False)
#                 df.employee_id = f.id
#                 df.save()


#             if candidate_acceptance.is_valid():
#                 caf = candidate_acceptance.save(commit=False)
#                 caf.employee_id = f.id
#                 caf.save()

#             messages.success(request, 'Employee added successfully', extra_tags='green')
#             return render(request, 'student/thankq.html')
#         else:
#             messages.error(request, 'Employee adding failed!', extra_tags='red')
#             return render(request, 'student/add_student1.html')
#     else:

#         context = {
#                 'form_p':EmployeeForm(),
#                 'edu_form':education_form_set(queryset=Education.objects.none()),
#                 'countries_travelled' : countries_travelledForm_set(queryset=Countries_travelled.objects.none()),
#                 'countries_refused' : countries_refusedForm_set(queryset=Countries_refused.objects.none()),
#                 'language_form' : languagesForm_set(queryset=Languages.objects.none()),
#                 'present_address' : Present_addressForm(),
#                 'permanent_address' : Permanent_addressForm(),
#                 'employee_history' : Employee_historyForm(),
#                 'previous_Employment' : Previous_EmploymentForm(),
#                 'reference' : referenceForm_set(queryset=Reference.objects.none()),
#                 'general' : generalForm_set(queryset=General.objects.none()),
#                 'emoluments' : EmolumentsForm(),
#                 'persanal_detailForm' : Persanal_detailForm(),
#                 'associates_addressForm' : associates_addressForm_set(queryset=Associates_address.objects.none()),
#                 'declaration_form' : Candidate_declaration_formForm(),
#                 'candidate_acceptance' : Candidate_acceptance_formForm()

#             }

#     return render(request, 'student/add_student1.html', context)


####************************************inlineformset****************************************#################

def Employe(request):
    education_form_set = inlineformset_factory(Employee, Education, form=EducationForm, extra=5)
    countries_travelledForm_set = inlineformset_factory(Employee, Countries_travelled, form = Countries_travelledForm)
    countries_refusedForm_set = inlineformset_factory(Employee, Countries_refused, form = Countries_refusedForm)
    languagesForm_set = inlineformset_factory(Employee, Languages, form = LanguagesForm)
    referenceForm_set = inlineformset_factory(Employee,Reference, form = ReferenceForm)
    generalForm_set = inlineformset_factory(Employee, General, form = GeneralForm)
    associates_addressForm_set = inlineformset_factory(Employee, Associates_address, form = Associates_addressForm)
    if request.method == "POST":
        present = Present_addressForm(request.POST)
        empo_form =EmployeeForm(request.POST, request.FILES)
        edu_form=education_form_set( request.POST, request.FILES)
        countries_travelled = countries_travelledForm_set(request.POST)
        countries_refused = countries_refusedForm_set(request.POST)
        language_form = languagesForm_set(request.POST)
        permanent = Permanent_addressForm(request.POST)
        employee_history = Employee_historyForm(request.POST)
        previous_Employment = Previous_EmploymentForm(request.POST)
        reference = referenceForm_set(request.POST)
        general = generalForm_set(request.POST)
        emoluments = EmolumentsForm(request.POST)
        persanal_detailForm = Persanal_detailForm(request.POST)
        associates_addressForm = associates_addressForm_set(request.POST)
        declaration_form = Candidate_declaration_formForm(request.POST)
        candidate_acceptance = Candidate_acceptance_formForm(request.POST)

        if all([empo_form.is_valid(), edu_form.is_valid(), countries_travelled.is_valid(), countries_refused.is_valid(), language_form.is_valid(), present.is_valid(), permanent.is_valid(), employee_history.is_valid(), previous_Employment.is_valid(), reference.is_valid(), general.is_valid(), emoluments.is_valid(), persanal_detailForm.is_valid(), associates_addressForm.is_valid(), declaration_form.is_valid(), candidate_acceptance.is_valid()]):
            ef = empo_form.save(commit=False)
            ef.save()

            edu = edu_form.save(commit=False)
            for e in edu:
                e.name = ef
                e.save()

            ctf = countries_travelled.save(commit=False)
            for c in ctf:
                c.employee = ef
                c.save()

            crf = countries_refused.save(commit=False)
            for cr in crf:
                cr.employee = ef
                cr.save()

            lf = language_form.save(commit=False)
            for l in lf:
                l.employee = ef
                print(l.employee_id )
                l.save()

            present_data = present.save(commit=False)
            present_data.employee = ef
            present_data.save()

            permanent_data = permanent.save(commit=False)
            permanent_data.employee = ef
            permanent_data.save()

            eh = employee_history.save(commit=False)
            eh.employee = ef
            eh.save()


            pef = previous_Employment.save(commit=False)
            pef.employee = ef
            pef.save()

            rf = reference.save(commit=False)
            for r in rf:
                r.employee = ef
                r.save()

            gf = general.save(commit=False)
            for g in gf:
                g.employee = ef
                g.save()

            emo = emoluments.save(commit=False)
            emo.employee = ef
            emo.save()

            pdf = persanal_detailForm.save(commit=False)
            pdf.employee = ef
            pdf.save()

            adf = associates_addressForm.save(commit=False)
            for df in adf:
                df.employee = ef
                df.save()

            df = declaration_form.save(commit=False)
            df.employee = ef
            df.save()

            af = candidate_acceptance.save(commit=False)
            af.employee = ef
            af.save()

            messages.success(request, 'Employee added successfully', extra_tags='green')
            return render(request, 'student/thankq.html')
        else:
            messages.error(request, 'Employee adding failed!', extra_tags='red')
            return render(request, 'student/add_student1.html')
    else:
        context = {
            'form_p':EmployeeForm(),
            'edu_form':education_form_set(),
            'countries_travelled' : countries_travelledForm_set(),
            'countries_refused' : countries_refusedForm_set(),
            'language_form' : languagesForm_set(),
            'present' : Present_addressForm(),
            'permanent' : Permanent_addressForm(),
            'employee_history' : Employee_historyForm(),
            'previous_Employment' : Previous_EmploymentForm(),
            'reference' : referenceForm_set(),
            'general' : generalForm_set(),
            'emoluments' : EmolumentsForm(),
            'persanal_detailForm' : Persanal_detailForm(),
            'associates_addressForm' : associates_addressForm_set(),
            'declaration_form' : Candidate_declaration_formForm(),
            'candidate_acceptance' : Candidate_acceptance_formForm()

        }

        return render(request, 'student/add_student1.html', context)



def Employe_edit(request, p_id):
    if not is_admin(request):
        messages.error(request, 'Your don not have access', extra_tags='red')
        return HttpResponseRedirect('/home/')
    emp = Employee.objects.get(pk=p_id)
    education_form_set = inlineformset_factory(Employee, Education, form=EducationForm, extra=5, max_num=5)
    countries_travelledForm_set = inlineformset_factory(Employee, Countries_travelled, form = Countries_travelledForm, max_num=3)
    countries_refusedForm_set = inlineformset_factory(Employee, Countries_refused, form = Countries_refusedForm, max_num=3)
    languagesForm_set = inlineformset_factory(Employee, Languages, form = LanguagesForm, max_num=3)
    referenceForm_set = inlineformset_factory(Employee,Reference, form = ReferenceForm, max_num=3)
    generalForm_set = inlineformset_factory(Employee, General, form = GeneralForm, max_num=3)
    associates_addressForm_set = inlineformset_factory(Employee, Associates_address, form = Associates_addressForm, max_num=3)
    eb = Employee.objects.get(id = p_id)
    paf = Present_address.objects.filter(employee_id = p_id).first()
    lf = Languages.objects.filter(employee_id = p_id).first()
    pef = Permanent_address.objects.filter(employee_id = p_id).first()
    eh = Employee_history.objects.filter(employee_id = p_id).first()
    pem = Previous_Employment.objects.filter(employee_id = p_id).first()
    em = Emoluments.objects.filter(employee_id = p_id).first()
    pd = Persanal_detail.objects.filter(employee_id = p_id).first()
    cd = Candidate_declaration_form.objects.filter(employee_id = p_id).first()
    ca = Candidate_acceptance_form.objects.filter(employee_id = p_id).first()
    edf = Education.objects.filter(name_id = p_id).first()
    ctf = Countries_travelled.objects.filter(employee_id = p_id).first()
    crf = Countries_refused.objects.filter(pk = p_id).first()
    rf = Reference.objects.filter(employee_id = p_id).first()
    gf = General.objects.filter(employee_id = p_id).first()
    adf = Associates_address.objects.filter(employee_id = p_id).first()


    if request.method == "POST":
        try:
            associates_addressForm = associates_addressForm_set(request.POST, instance=emp)
            reference = referenceForm_set(request.POST, instance=emp)
            general = generalForm_set(request.POST, instance=emp)
            edu_form=education_form_set( request.POST, request.FILES, instance=emp)
            countries_travelled = countries_travelledForm_set(request.POST, instance=emp)
            countries_refused = countries_refusedForm_set(request.POST, instance=emp)
            language_form = languagesForm_set(request.POST, instance=emp)
        except ValidationError:
            associates_addressForm =None
            reference = None
            general = None
            edu_form =None
            countries_travelled = None
            language_form = None
            countries_refused = None
        empo_form =EmployeeForm(request.POST, request.FILES, instance=eb)
        present = Present_addressForm(request.POST,  instance=paf)
        permanent = Permanent_addressForm(request.POST, instance=pef)
        employee_history = Employee_historyForm(request.POST, instance=eh)
        previous_Employment = Previous_EmploymentForm(request.POST, instance=pem)
        emoluments = EmolumentsForm(request.POST, instance= em)
        persanal_detailForm = Persanal_detailForm(request.POST, instance=pd)
        declaration_form = Candidate_declaration_formForm(request.POST, instance=cd)
        candidate_acceptance = Candidate_acceptance_formForm(request.POST, instance=ca)



        # if empo_form.is_valid():
        #     f = empo_form.save(commit=False)
        #     f.save()
        #     print("first")
        #     if edu_form.is_valid():
        #         ef = edu_form.save(commit=False)
        #         for f in ef:
        #             f.name_id = f
        #             f.save()
        #             print("save1")

        #     if countries_travelled.is_valid():
        #         cf = countries_travelled.save(commit=False)
        #         for cf in cf:
        #             cd.employee_id = f
        #             cd.save()
        #             print("save2")

        #     if countries_refused.is_valid():
        #         cr = countries_refused.save(commit=False)
        #         for cr in cr:
        #             cr.employee_id = f
        #             cr.save()
        #             print("save3")

        #     if language_form.is_valid():
        #         lf = language_form.save(commit=False)
        #         for l in lf:
        #             l.employee_id = f
        #             l.save()
        #             print("save4")

        #     if present.is_valid():
        #         pd = present.save(commit=False)
        #         pd.employee_id = f
        #         pd.save()
        #         print("save5")

        #     if permanent.is_valid():
        #         pd = permanent.save(commit=False)
        #         pd.employee_id = f
        #         pd.save()
        #         print("save6")

        #     if employee_history.is_valid():
        #         eh = employee_history.save(commit=False)
        #         eh.employee_id = f
        #         eh.save()
        #         print("save7")

        #     if previous_Employment.is_valid():
        #         pe = previous_Employment.save(commit=False)
        #         pe.employee_id = f
        #         pe.save()
        #         print("save8")

        #     if reference.is_valid():
        #         rf = reference.save(commit=False)
        #         for rf in rf:
        #             rf.employee_id = f
        #             rf.save()
        #             print("save9")

        #     if general.is_valid():
        #         g = general.save(commit=False)
        #         for g in g:
        #             g.employee_id = f
        #             g.save()
        #             print("save10")


        #     if emoluments.is_valid():
        #         emo = emoluments.save(commit=False)
        #         emo.employee_id =f
        #         emo.save()
        #         print("save11")

        #     if persanal_detailForm.is_valid():
        #         pdf = persanal_detailForm.save(commit=False)
        #         pdf.employee_id = f
        #         pdf.save()
        #         print("save12")

        #     if associates_addressForm.is_valid():
        #         adf = associates_addressForm.save(commit=False)
        #         for adf in adf:
        #             adf.employee_id = f
        #             adf.save()
        #             print("save13")


        #     if declaration_form.is_valid():
        #         df = declaration_form.save(commit=False)
        #         df.employee_id = f
        #         df.save()
        #         print("save14")


        #     if candidate_acceptance.is_valid():
        #         caf = candidate_acceptance.save(commit=False)
        #         caf.employee_id = f
        #         caf.save()
        #         print("save15")

        if all([empo_form.is_valid(), edu_form.is_valid(), countries_travelled.is_valid(), countries_refused.is_valid(), language_form.is_valid(), present.is_valid(), permanent.is_valid(), employee_history.is_valid(), previous_Employment.is_valid(), reference.is_valid(), general.is_valid(), emoluments.is_valid(), persanal_detailForm.is_valid(), associates_addressForm.is_valid(), declaration_form.is_valid(), candidate_acceptance.is_valid()]):
            ef = empo_form.save(commit=False)
            ef.save()
            edu = edu_form.save(commit=False)
            for e in edu:
                e.name = ef
                e.save()
            ctf = countries_travelled.save(commit=False)
            for c in ctf:
                c.employee = ef
                c.save()
            crf = countries_refused.save(commit=False)
            for cr in crf:
                cr.employee = ef
                cr.save()
            lf = language_form.save(commit=False)
            for l in lf:
                l.employee = ef
                l.save()

            pa = present.save(commit=False)
            pa.employee = ef
            pa.save()
            pe = permanent.save(commit=False)
            pe.employee = ef
            pe.save()
            eh = employee_history.save(commit=False)
            eh.employee = ef
            eh.save()
            pef = previous_Employment.save(commit=False)
            pef.employee = ef
            pef.save()
            rf = reference.save(commit=False)
            for r in rf:
                r.employee = ef
                r.save()
            gf = general.save(commit=False)
            for g in gf:
                g.employee = ef
                g.save()

            emo = emoluments.save(commit=False)
            emo.employee = ef
            emo.save()
            pdf = persanal_detailForm.save(commit=False)
            pdf.employee = ef
            pdf.save()
            adf = associates_addressForm.save(commit=False)
            for df in adf:
                df.employee = ef
                df.save()

            df = declaration_form.save(commit=False)
            df.employee = ef
            df.save()
            af = candidate_acceptance.save(commit=False)
            af.employee = ef
            af.save()

            messages.success(request, 'Employee added successfully', extra_tags='green')
            return render(request, 'student/thankq.html')
        else:
            messages.error(request, 'Employee adding failed!', extra_tags='red')
            return render(request, 'student/add_student1.html')
    else:
        language_form = languagesForm_set(instance=emp)
        context = {
            'form_p':EmployeeForm(instance=eb),
            'edu_form':education_form_set(instance=emp),
            'countries_travelled' : countries_travelledForm_set(instance=emp),
            'countries_refused' : countries_refusedForm_set(instance=emp),
            'language_form' : language_form,
            'present' : Present_addressForm(instance=paf),
            'permanent' : Permanent_addressForm(instance=pef),
            'employee_history' : Employee_historyForm(instance=eh),
            'previous_Employment' : Previous_EmploymentForm(instance=pem),
            'reference' : referenceForm_set(instance = emp),
            'general' : generalForm_set(instance = emp),
            'emoluments' : EmolumentsForm(instance= em),
            'persanal_detailForm' : Persanal_detailForm(instance=pd),
            'associates_addressForm' : associates_addressForm_set(instance = emp),
            'declaration_form' : Candidate_declaration_formForm(instance=cd),
            'candidate_acceptance' : Candidate_acceptance_formForm(instance=ca)

        }

        return render(request, 'student/add_student1.html', context)



def delete_employ(request, p_id):
    if not is_admin(request):
        messages.error(request, 'Your don not have access', extra_tags='red')
        return HttpResponseRedirect('/home/')
    data = Employee.objects.get(id=p_id)
    data.delete()
    messages.success(request, 'Employee deleted successfully', extra_tags='green')
    return redirect('view')


