from django.db import models
from datetime import datetime, timedelta

# Create your models here.


GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other'),
)
MARITAL_STATUS = (
  ('YES', 'yes'),
  ('NO', 'no')
)
EDUCATION_TYPE = (
  ('Matriculation/SSC/Equivalent', 'Matriculation/SSC/Equivalent'),
  ('Intermediate/HSC/Equivalent', 'Intermediate/HSC/Equivalent'),
  ('Diploma/Equivalent', 'Diploma/Equivalent'),
  ('Graduation/Equivalent', 'Graduation/Equivalent'),
  ('Post-Graduation/Equivalent', 'Post-Graduation/Equivalent'),
)
SOURCE = (
  ('Agency', 'agency'),
  ('Buddy', 'buddy'),
  ('Direct', 'direct'),
  ('Porta', 'portal'),
  ('Advt', 'advt'),
  ('Reference', 'refrence'),
  ('Contract/sub Contract', 'contract/sub contract'),
  ('Others','others')
)

OFFICER_CODE = (
  ('Lateral','Lateral'),
  ('Direct Contract', 'Direct Contract'),
  ('Mature Trainee', 'Mature Trainee')
)
EMPLOYEE_CLASSES = (
  ('Technical ', 'Technical '),
  ('Sales & Marketing', 'Sales & Marketing'),
  ('Support','Support'),
  ('Managerial','Managerial')
)
TYPE_OF_EXPERIENCE = (
  ('IT Industry', 'IT Industry'),
  ('Non IT Industry', 'Non IT Industry'),
  ('Weightage for Qualification (+/-)', 'Weightage for Qualification (+/-)'),
  ('Net Total Relevant Experience (TRE) ', 'Net Total Relevant Experience (TRE) ')
)
EMPLOY_TYPE = (
  ('Permanent', 'Permanent'),
  ('Fixed Term Contract','Fixed Term Contract')
)

class Address(models.Model):
  building_apt_name = models.CharField(max_length = 100, verbose_name = 'Building/Apt. Name:')
  H_D_Flat_No = models.CharField(max_length = 100, verbose_name = 'H.No/D.No/Flat.No')
  street_colony = models.CharField(max_length = 100, verbose_name = 'Street/Colony Name')
  landmark = models.CharField(max_length = 100, verbose_name = 'Landmark')
  city = models.CharField(max_length = 100, verbose_name = 'City')
  state = models.CharField(max_length = 100, verbose_name = 'State')
  pincode = models.IntegerField( verbose_name = 'Pincode')
  phonoe = models.IntegerField( verbose_name = 'Phone No' )
  
  class Meta:
    abstract=True


class Employee(models.Model):
  e_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name Mr./Ms.")
  e_photo = models.ImageField(upload_to='staff/photo/',   null=True, blank=True, verbose_name="Photo")
  e_gender = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Sex", choices=GENDER_CHOICES)
  e_father_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  e_mother_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Mother")
  e_dob = models.DateField(   null=True, blank=True, verbose_name="Date Of Birth")
  e_place_of_birth = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Place of Birth")
  e_marital_status = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Marital Status", choices=MARITAL_STATUS)
  e_nationality = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Nationality")
  e_passport_no  = models.IntegerField( null=True, blank=True, verbose_name='passport No')
  e_place_of_pp_issue = models.CharField(max_length = 100,  null=True, blank=True, verbose_name="Place of PP Issue")
  e_date_of_pp_issue = models.DateField(   null=True, blank=True, verbose_name="Date Of PP Issue")
  e_date_of_pp_expiry = models.DateField(   null=True, blank=True, verbose_name="Date Of PP Expiry")
  e_applied_for_pp = models.BooleanField( blank=True, verbose_name="if you don't have valid PP, have you applied for one ?")
  e_pp_application_no = models.IntegerField( null=True, blank=True, verbose_name="Application No")
  e_date_of_application = models.DateField(  null=True, blank=True, verbose_name="Date of Application") 
  e_email = models.EmailField(max_length=250,   null=True, blank=True, verbose_name="Email")
  e_working_relative = models.BooleanField( blank=True, verbose_name="Do you have any relative(s) working with any of Mahindra Group Companies ?")
  e_name_of_relatiove = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Name of Relative")
  e_relationship = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Relationship")
  e_company = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Name of Company")
  e_salary_expected = models.IntegerField( default=True, null=True, blank=True, verbose_name='Salary Expected')
  e_joining_time_required = models.IntegerField( null=True, blank=True, verbose_name='Joining Time Required')
  e_declaration = models.BooleanField(blank=True, verbose_name='I certify that: \n 1. The information furnished above is factually correct and subject to verification by Tech Mahindra Ltd. 2. lam at present in sound mental and physical condition to undertake employment with Tech Mahindra Ltd. 3. I accept that an appointment given to me on this basis can be revoked, if any information has been misstated or unstated')
  country_refused = models.BooleanField( blank=True, verbose_name="Have you been refused/denied visa any time ?")
  applied = models.BooleanField( blank=True, verbose_name= 'Have you ever applied for a job with Mahindra Group Company. in last 6 months ?')

  status = models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Employees"
    verbose_name = "Employee"


class Permanent_address(Address):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Present_address(Address):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Education(models.Model):
  name = models.ForeignKey(Employee,  on_delete=models.CASCADE)
  education = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Education", choices=EDUCATION_TYPE)
  college = models.CharField(max_length=100,   null=True, blank=True, verbose_name="College/University")
  name_of_degree = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Name of Degree")
  duration_from = models.DateField(   null=True, blank=True, verbose_name="From")
  duration_to = models.DateField(   null=True, blank=True, verbose_name="To")
  specialization = models.CharField(max_length=100,   null=True, blank=True, verbose_name="Specialization")
  percentage = models.FloatField(  null=True, blank=True, verbose_name="Percentage")
  certificates = models.FileField(upload_to ='Certificates/Project',  default=None, null=True, blank=True, verbose_name="Certificates")

  status = models.BooleanField(default=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Educations"
    verbose_name = "Education"


class Countries_travelled(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  country_travelled = models.CharField(max_length = 255, null = True ,verbose_name = 'Country Travelled')
  duration_of_travel = models.DateField( verbose_name = 'Duration of Travel')
  purpus_of_travel = models.CharField(max_length = 255, verbose_name = 'Purpus of Travel')


class Countries_refused(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  
  country = models.CharField(max_length = 255, null = True ,verbose_name = 'Country')
  date_of_application = models.DateField( verbose_name = 'Date of Application')
  type_of_visa = models.CharField(max_length = 255, verbose_name = 'Type of Visa')
  resion_of_refused = models.CharField(max_length = 255, verbose_name = 'Reason of Refusl/Denial')


class Languages(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  language = models.CharField(max_length = 255, verbose_name = 'Languages')
  speek = models.BooleanField(verbose_name = 'Speek')
  read = models.BooleanField(verbose_name = 'Read')
  write = models.BooleanField(verbose_name = 'Write')


class Employee_history(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  change_leaving = models.CharField(max_length = 255, null = True, verbose_name = 'Reason for Seeking change/leaving')
  phonoe = models.IntegerField(verbose_name = 'Phone No.')
  current_designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Current Designation')
  industry_type = models.CharField(max_length = 100,  null=True, blank=True, verbose_name='Industry Type')
  period_of_service_from = models.DateField(null=True, blank=True, verbose_name='from')
  period_of_service_to = models.DateField(null=True, blank=True, verbose_name='to')
  starting_salary = models.IntegerField(verbose_name = 'Starting Salary')
  current_salary = models.IntegerField(verbose_name = 'Current Salary')
  supervisor = models.CharField(max_length = 255,  verbose_name = 'Name $ Designation of Supervisor')


class Previous_Employment(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  email = models.EmailField(max_length=250,   null=True, blank=True, verbose_name="Email")
  period_of_service_from = models.DateField(null=True, blank=True, verbose_name='from')
  period_of_service_to = models.DateField(null=True, blank=True, verbose_name='to')
  designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Designation')
  nature_of_duties = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Nature of Duties')
  salary = models.IntegerField(verbose_name = 'Last Salary Drawn')


class Reference(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Designation')
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  email = models.EmailField(max_length=250,   null=True, blank=True, verbose_name="Email")
  phonoe = models.IntegerField(verbose_name = 'Phone No.')
  nature_of_association = models.CharField(max_length = 100,  null=True, blank=True, verbose_name='Nature of Association')


class General(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  
  name_of_company = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Company")
  position_applied_for = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Position Applied For")
  date_of_application = models.DateField(null=True, blank=True, verbose_name='Date of Application')
  reason = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Reasion for NOt joining')


class Emoluments(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  basic = models.IntegerField (verbose_name = 'Basic')
  da = models.IntegerField( verbose_name = 'DA')
  cca = models.IntegerField( verbose_name = 'CCA')
  hra = models.IntegerField( verbose_name = 'HRA')
  conveyance = models.IntegerField( verbose_name = 'Conveyance')
  lta = models.IntegerField( verbose_name = 'LTA')
  anyother_allowences = models.IntegerField( verbose_name = 'Anyother')
  cross_income = models.IntegerField( verbose_name = 'Gross Income')
  pf = models.IntegerField( verbose_name = 'PF')
  medical = models.IntegerField( verbose_name = 'Medical')
  insurance = models.IntegerField( verbose_name = 'Insurance')
  any_other_deductions = models.IntegerField( verbose_name = 'Any Other Deduction')
  gross_deduction = models.IntegerField( verbose_name = 'Gross Deduction')
  net_salary = models.IntegerField( verbose_name = 'Net Salary per Annum')


class persanal_detail(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name Mr./Ms.")
  father_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  gender = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Sex", choices=GENDER_CHOICES)
  employe_id = models.IntegerField(null=True, blank=True, verbose_name = 'Employee ID')
  husband_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  dob = models.DateField(   null=True, blank=True, verbose_name="Date Of Birth")
  joining_date = models.DateField(max_length = 100, verbose_name = 'Joining Date')
  joining_location = models.CharField(max_length = 100, verbose_name = 'Joining Location')
  social_security_Number = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Social Security Number (If applicable)")


class Associates_address(Address):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  duration_of_stay_from = models.DateField(null=True, blank=True,  verbose_name= 'Duration of stay From')
  duration_of_stay_to = models.DateField(null=True, blank=True, verbose_name= 'Duration of stay To')


class Candidate_declaration_form(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
  source = models.CharField(max_length=100, null=True, blank=True, verbose_name='Source')
  date = models.DateField(null=True, blank=True, verbose_name='Date')
  declaration_1 = models.BooleanField(default=False)
  declaration_2 = models.BooleanField(default=False)
  declaration_3 = models.BooleanField(default=False)
  declaration_4 = models.BooleanField(default=False)
  declaration_5 = models.BooleanField(default=False)
  declaration_6 = models.BooleanField(default=False)
  declaration_7 = models.BooleanField(default=False)
  declaration_8 = models.BooleanField(default=False)
  declaration_9 = models.BooleanField(default=False)
  declaration_10 = models.BooleanField(default=False)
  declaration_11 = models.BooleanField(default=False)
  declaration_12 = models.BooleanField(default=False)
  declaration_13 = models.BooleanField(default=False)
  declaration_14 = models.BooleanField(default=False)
  declaration_15 = models.BooleanField(default=False)
  declaration_16 = models.BooleanField(default=False)
  declaration_17 = models.BooleanField(default=False)
  declaration_18 = models.BooleanField(default=False)
  declaration_19 = models.BooleanField(default=False)
  declaration_20= models.BooleanField(default=False)
  declaration_21 = models.BooleanField(default=False)


class Candidate_acceptance_form(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
  application_id = models.IntegerField(null=True, blank=True, verbose_name='Application ID')
  source = models.CharField(max_length = 100, verbose_name = 'Source', choices=SOURCE)
  name_of_source = models.CharField(max_length=100, verbose_name = 'Name of Source')
  officer_code = models.CharField(max_length = 100, verbose_name = 'Officee Code', choices=OFFICER_CODE)
  employee_class = models.CharField(max_length = 100, verbose_name = 'Employee Class', choices=EMPLOYEE_CLASSES)
           ########### Relevent Experience Fixation #########
  type_of_experience = models.CharField(max_length = 100, verbose_name = 'Type of Experience', choices=TYPE_OF_EXPERIENCE)
  total_experience = models.CharField(max_length=100, null=True, blank=True, verbose_name='Total Experience')
  relevant_experience = models.CharField(max_length = 100, verbose_name = 'Revelant Experience')
  remarks  = models.CharField(max_length = 100, verbose_name = 'Remarks ')
    ######## Employment & Fitment Related Information  ########
  current_location = models.CharField(max_length = 100, verbose_name = 'Current Location')
  location_constraints = models.CharField(max_length = 100, null=True, blank=True, verbose_name= 'Location Constraints', choices=MARITAL_STATUS)
  location_preference = models.CharField(max_length = 100, verbose_name = 'Location Preference',)
  is_passport_valid = models.CharField(max_length = 100, verbose_name = 'Is Passport valid ?', choices=MARITAL_STATUS)
  ready_to_travel = models.CharField(max_length = 100, verbose_name = ' Ready to Travel (including Onsite)?', choices=MARITAL_STATUS)
  visa_rejected = models.CharField(max_length = 100, verbose_name = 'Was visa ever rejected ?', choices=MARITAL_STATUS)
  offered_ctc_excluding = models.CharField(max_length=100, null=True, blank=True, verbose_name='Offered CTC (excluding Gratuity & Insurance) ')
  offered_ctc_including = models.CharField(max_length=100, null=True, blank=True, verbose_name='Offered CTC (including Gratuity & Insurance) ')
  expected_ctc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Expected CTC (Annual)')
  current_ctc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Current CTC (Annual)')
  job_role = models.CharField(max_length=100, null=True, blank=True, verbose_name='Proposed Band & Job Role/ Designation')
  type_of_employment = models.CharField(max_length = 100, verbose_name = ' Ready to Travel (including Onsite)?', choices=EMPLOY_TYPE)
  contract_start_date = models.DateField(max_length = 100, verbose_name = 'Contract Start Date')
  contract_duration = models.CharField(max_length = 100, verbose_name = 'Contract Duration (in months)')
  joining_date = models.DateField(max_length = 100, verbose_name = 'Joining Date')
  joining_location = models.CharField(max_length = 100, verbose_name = 'Joining Location')
    ############ Commitments & Relevant Information ########
  guest_house_accommodation = models.CharField(max_length = 100, verbose_name = 'Guest House Accommodation? ', choices=MARITAL_STATUS)
  willing_work = models.CharField(max_length = 100, verbose_name = 'Willing to work in Shifts ? 24x7 ', choices=MARITAL_STATUS)
  notice_period = models.CharField(max_length = 100, verbose_name = 'Notice Period in Months')
  expected_joining_date = models.DateField(max_length = 100, verbose_name = 'Expected Date Of Joining ')
  comments = models.TextField(verbose_name = 'Any Other Commitment(s) (Pls specify here)')
  declaration = models.BooleanField(default=False, verbose_name = 'I hereby, confirm that I understand all above details/information and I have no observation of any kind on any of the above information/commitments.')
  recruter_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Recruiter's Name")
  authority_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Approving Authority")






