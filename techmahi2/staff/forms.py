from django import forms
from staff.models import *
from django.forms import ModelForm
from django.conf import settings
import re
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.forms import BaseModelFormSet, BaseInlineFormSet
from django.forms.models import modelformset_factory, inlineformset_factory
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email'] 
        
class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    fields = ['e_name', 'e_gender','e_photo','e_father_name', 'e_mother_name', 'e_dob', 'e_place_of_birth', 'e_marital_status', 'e_nationality', 'e_passport_no', 'e_place_of_pp_issue', 'e_date_of_pp_issue', 'e_date_of_pp_expiry', 'e_applied_for_pp', 'e_pp_application_no', 'e_date_of_application', 'e_email', 'e_working_relative', 'e_name_of_relatiove', 'e_relationship', 'e_company','country_refused','applied','e_declaration','e_salary_expected','e_joining_time_required', 'country_refused', 'applied']
    widgets = {
     'e_dob': DatePicker(),
     'e_date_of_pp_expiry': DatePicker(),
     'e_date_of_pp_issue': DatePicker(),

     }

class EducationForm(ModelForm):
  class Meta:
    model = Education
    fields = ['education', 'college', 'name_of_degree', 'duration_from', 'duration_to', 'specialization', 'percentage','certificates']
    widgets = {
     'duration_from': DatePicker(),
     'duration_to': DatePicker(),

     }


class Countries_travelledForm(ModelForm):
  class Meta:
    model = Countries_travelled
    exclude = ['employee']
    widgets = {
     'duration_of_travel': DatePicker(),

     }
  
 
class Countries_refusedForm(ModelForm):
  class Meta:
    model = Countries_refused
    exclude = ['employee']
    widgets = {
     'date_of_application': DatePicker(),

     }
  

class LanguagesForm(ModelForm):
  class Meta:
    model = Languages
    exclude = ['employee']

# class RequiredFormSet(BaseModelFormSet):
#     def __init__(self, *args, **kwargs):
#         super(RequiredFormSet, self).__init__(*args, **kwargs)
#         for form in self.forms:
#             form.empty_permitted = True


class MyModelFormSet(BaseInlineFormSet):
    def clean(self):
        super(MyModelFormSet, self).clean()
        # example custom validation across forms in the formset
        for form in self.forms:
          if not form.is_valid():
            continue



class Employee_historyForm(ModelForm):
  class Meta:
    model = Employee_history
    exclude = ['employee']
    widgets = {
     'employee_service_from': DatePicker(),
     'employee_service_to': DatePicker(),

     }
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['phonoe'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
 

class Previous_EmploymentForm(ModelForm):
  class Meta:
    model = Previous_Employment
    exclude = ['employee']
    widgets = {
     'period_of_service_from': DatePicker(),
     'period_of_service_to': DatePicker(),

     }


class ReferenceForm(ModelForm):
  class Meta:
    model = Reference
    exclude = ['employee']
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['phonoe'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
  
class GeneralForm(ModelForm):
  class Meta:
    model = General
    exclude = ['employee']
    widgets = {
     'date_of_application': DatePicker(),

     }

class EmolumentsForm(ModelForm):
  class Meta:
    model = Emoluments
    exclude = ['employee']

class Permanent_addressForm(ModelForm):
  class Meta:
    model = Permanent_address
    exclude = ['employee']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['phonoe1'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
    self.fields['pincode1'].widget.attrs.update({'data-inputmask': '"mask": "999-999"'})

class Present_addressForm(ModelForm):
  class Meta:
    model = Present_address
    exclude = ['employee']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['phonoe0'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
    self.fields['pincode0'].widget.attrs.update({'data-inputmask': '"mask": "999-999"'})
    
  #phonoe0 = forms.CharField(widget=forms.TextInput(attrs={'data-inputmask': '"mask": "(999) 999-9999"'}))

class Persanal_detailForm(ModelForm):
  class Meta:
    model = Persanal_detail
    exclude = ['employee']
    widgets = {
     'p_dob': DatePicker(),
     'p_joining_date': DatePicker(),

     }
 

class Associates_addressForm(ModelForm):
  class Meta:
    model = Associates_address
    exclude = ['employee']
    widgets = {
     'duration_of_stay_from': DatePicker(),
     'duration_of_stay_to': DatePicker(),

     }
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['phonoe'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
    self.fields['pincode'].widget.attrs.update({'data-inputmask': '"mask": "999-999"'})
  
 
class Candidate_declaration_formForm(ModelForm):
  class Meta:
    model = Candidate_declaration_form
    exclude = ['employee']

class Candidate_acceptance_formForm(ModelForm):
  class Meta:
    model = Candidate_acceptance_form
    exclude = ['employee']
    widgets = {
     'joining_date': DatePicker(),
     'contract_start_date': DatePicker(),
     'expected_joining_date': DatePicker(),

     }
  

# education_form_set = modelformset_factory(Education, form=EducationForm, formset=MyModelFormSet, extra=5, max_num=5)
# countries_travelledForm_set = modelformset_factory(Countries_travelled, form = Countries_travelledForm, extra=3, max_num=3)
# countries_refusedForm_set = modelformset_factory(Countries_refused, form = Countries_refusedForm, extra=3, max_num=3)
# languagesForm_set = modelformset_factory(Languages, form = LanguagesForm, formset=MyModelFormSet, extra=3)
# referenceForm_set = modelformset_factory(Reference, form = ReferenceForm, extra=3, max_num=3)
# generalForm_set = modelformset_factory(General, form = GeneralForm, extra=3, max_num=3)
# associates_addressForm_set = modelformset_factory(Associates_address, form = Associates_addressForm, extra=3, max_num=3)

