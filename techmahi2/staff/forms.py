from django import forms
from staff.models import *
from django.forms import ModelForm
from django.conf import settings
import re

class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    fields = ['e_name', 'e_gender','e_photo','e_father_name', 'e_mother_name', 'e_dob', 'e_place_of_birth', 'e_marital_status', 'e_nationality', 'e_passport_no', 'e_place_of_pp_issue', 'e_date_of_pp_issue', 'e_date_of_pp_expiry', 'e_applied_for_pp', 'e_pp_application_no', 'e_date_of_application', 'e_email', 'e_working_relative', 'e_name_of_relatiove', 'e_relationship', 'e_company','country_refused','applied','e_declaration','e_salary_expected','e_joining_time_required']
  
  e_dob = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'date_picker'}), input_formats=settings.DATE_INPUT_FORMATS )
  e_date_of_pp_expiry = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'date_picker'}), input_formats=settings.DATE_INPUT_FORMATS )
  e_date_of_pp_issue = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'date_picker'}), input_formats=settings.DATE_INPUT_FORMATS )

class EducationForm(ModelForm):
  class Meta:
    model = Education
    fields = ['education', 'college', 'name_of_degree', 'duration_from', 'duration_to', 'specialization', 'percentage','certificates']

  duration_from = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'date_picker'}), input_formats=settings.DATE_INPUT_FORMATS )
  duration_to = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'date_picker'}), input_formats=settings.DATE_INPUT_FORMATS )

class Countries_travelledForm(ModelForm):
  class Meta:
    model = Countries_travelled
    exclude = ['employee']

class Countries_refusedForm(ModelForm):
  class Meta:
    model = Countries_refused
    exclude = ['employee']

class LanguagesForm(ModelForm):
  class Meta:
    model = Languages
    exclude = ['employee']

class Employee_historyForm(ModelForm):
  class Meta:
    model = Employee_history
    exclude = ['employee']

class Previous_EmploymentForm(ModelForm):
  class Meta:
    model = Previous_Employment
    exclude = ['employee']

class ReferenceForm(ModelForm):
  class Meta:
    model = Reference
    exclude = ['employee']

class GeneralForm(ModelForm):
  class Meta:
    model = General
    exclude = ['employee']

class EmolumentsForm(ModelForm):
  class Meta:
    model = Emoluments
    exclude = ['employee']

class Permanent_addressForm(ModelForm):
  class Meta:
    model = Permanent_address
    exclude = ['employee']

class Present_addressForm(ModelForm):
  class Meta:
    model = Present_address
    exclude = ['employee']

class persanal_detailForm(ModelForm):
  class Meta:
    model = persanal_detail
    exclude = ['employee']

class Associates_addressForm(ModelForm):
  class Meta:
    model = Associates_address
    exclude = ['employee']

class Candidate_declaration_formForm(ModelForm):
  class Meta:
    model = Candidate_declaration_form
    exclude = ['employee']

class Candidate_acceptance_formForm(ModelForm):
  class Meta:
    model = Candidate_acceptance_form
    exclude = ['employee']



