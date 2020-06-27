from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','e_name', 'e_gender','e_photo', 'e_father_name', 'e_mother_name', 'e_dob', 'e_place_of_birth', 'e_marital_status', 'e_nationality', 'e_passport_no', 'e_place_of_pp_issue', 'e_date_of_pp_issue', 'e_date_of_pp_expiry', 'e_applied_for_pp', 'e_pp_application_no', 'e_date_of_application', 'e_email', 'e_working_relative', 'e_name_of_relatiove', 'e_relationship', 'e_company')

admin.site.register(Employee ,EmployeeAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'education', 'college', 'name_of_degree', 'duration_from', 'duration_to', 'specialization', 'percentage')
    
admin.site.register(Education ,EducationAdmin)

class Countries_travelledAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Countries_travelled ,Countries_travelledAdmin)

class Countries_refusedAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Countries_refused ,Countries_refusedAdmin)

class LanguagesAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Languages, LanguagesAdmin)

class Employee_historyAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Employee_history, Employee_historyAdmin)

class Previous_EmploymentAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Previous_Employment, Previous_EmploymentAdmin)

class ReferenceAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Reference, ReferenceAdmin)

class GeneralAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(General, GeneralAdmin)

class EmolumentsAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Emoluments, EmolumentsAdmin)

class Permanent_addressAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Permanent_address, Permanent_addressAdmin)

class Present_addressAdmin(admin.ModelAdmin):
  display = "__all__"
admin.site.register(Present_address, Present_addressAdmin)

class Persanal_detailAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Persanal_detail, Persanal_detailAdmin)

class Associates_addressAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Associates_address, Associates_addressAdmin)

class Candidate_declaration_formAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Candidate_declaration_form, Candidate_declaration_formAdmin)

class Candidate_acceptance_formAdmin(admin.ModelAdmin):
  exclude = ['employee']
admin.site.register(Candidate_acceptance_form, Candidate_acceptance_formAdmin)        