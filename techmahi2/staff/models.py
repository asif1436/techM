from django.db import models
from datetime import datetime, timedelta

# Create your models here.


GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other'),
)
MARITAL_STATUS = (
  ('YES', 'Yes'),
  ('NO', 'No')
)
EDUCATION_TYPE = (
  ('Matriculation/SSC/Equivalent', 'Matriculation/SSC/Equivalent'),
  ('Intermediate/HSC/Equivalent', 'Intermediate/HSC/Equivalent'),
  ('Diploma/Equivalent', 'Diploma/Equivalent'),
  ('Graduation/Equivalent', 'Graduation/Equivalent'),
  ('Post-Graduation/Equivalent', 'Post-Graduation/Equivalent'),
)
SOURCE = (
  ('Agency', 'Agency'),
  ('Buddy', 'Buddy'),
  ('Direct', 'Direct'),
  ('Porta', 'Portal'),
  ('Advt', 'Advt'),
  ('Reference', 'Refrence'),
  ('Contract/sub Contract', 'Contract/Sub Contract'),
  ('Others','Others')
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



class Employee(models.Model):
  e_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name Mr./Ms.")
  e_photo = models.ImageField(upload_to='staff/photo/', null=True, blank=True, verbose_name="Photo")
  e_gender = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Sex", choices=GENDER_CHOICES)
  e_father_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  e_mother_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Mother")
  e_dob = models.DateField(null=True, blank=True, verbose_name="Date Of Birth")
  e_place_of_birth = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Place of Birth")
  e_marital_status = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Marital Status", choices=MARITAL_STATUS)
  e_nationality = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Nationality")
  e_passport_no  = models.CharField(max_length = 100, null=True, blank=True, verbose_name='passport No')
  e_place_of_pp_issue = models.CharField(max_length = 100,  null=True, blank=True, verbose_name="Place of PP Issue")
  e_date_of_pp_issue = models.DateField(null=True, blank=True, verbose_name="Date Of PP Issue")
  e_date_of_pp_expiry = models.DateField(null=True, blank=True, verbose_name="Date Of PP Expiry")
  e_applied_for_pp = models.BooleanField(default=False, blank=True, verbose_name="if you don't have valid PP, have you applied for one ?")
  e_pp_application_no = models.CharField(max_length = 100, null=True, blank=True, verbose_name="Application No")
  e_date_of_application = models.DateField(null=True, blank=True, verbose_name="Date of Application") 
  e_email = models.EmailField(null=True, blank=True, verbose_name="demo@gmail.com")
  e_working_relative = models.BooleanField(default=False, blank=True, verbose_name="Do you have any relative(s) working with any of Mahindra Group Companies ?")
  e_name_of_relatiove = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Relative")
  e_relationship = models.CharField(max_length=100, null=True, blank=True, verbose_name="Relationship")
  e_company = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Company")
  e_salary_expected = models.CharField(max_length=100, null=True, blank=True, verbose_name='Salary Expected')
  e_joining_time_required = models.CharField(max_length = 100, null=True, blank=True, verbose_name='Joining Time Required')
  e_declaration = models.BooleanField(blank=True, default=False, verbose_name='I certify that: \n 1. The information furnished above is factually correct and subject to verification by Tech Mahindra Ltd. 2. lam at present in sound mental and physical condition to undertake employment with Tech Mahindra Ltd. 3. I accept that an appointment given to me on this basis can be revoked, if any information has been misstated or unstated')
  country_refused = models.BooleanField( blank=True, default=False, verbose_name="Have you been refused/denied visa any time ?")
  applied = models.BooleanField(blank=True, default=False, verbose_name= 'Have you ever applied for a job with Mahindra Group Company. in last 6 months ?')

  status = models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Employees"
    verbose_name = "Employee"

  def __str__(self):
    return self.e_name


class Permanent_address(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  building_apt_name1 = models.CharField(max_length = 100, null=True,  blank=True, verbose_name = 'Building/Apt. Name:')
  H_D_Flat_No1 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'H.No/D.No/Flat.No')
  street_colony1 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Street/Colony Name')
  landmark1 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Landmark')
  city1 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'City')
  state1 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'State')
  pincode1 = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Pincode')
  phonoe1 = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Phone No' )


class Present_address(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  building_apt_name0 = models.CharField(max_length = 100, null=True,  blank=True, verbose_name = 'Building/Apt. Name:')
  H_D_Flat_No0 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'H.No/D.No/Flat.No')
  street_colony0 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Street/Colony Name')
  landmark0 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Landmark')
  city0 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'City')
  state0 = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'State')
  pincode0 = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Pincode')
  phonoe0 = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Phone No' )

  class Meta:
    verbose_name_plural = "Present_addresses"
    verbose_name = "Present_address"

  def __str__(self):
    return self.building_apt_name0


class Education(models.Model):
  name = models.ForeignKey(Employee,  on_delete=models.CASCADE)
  education = models.CharField(max_length=100, null=True, blank=True, verbose_name="Education", choices=EDUCATION_TYPE)
  college = models.CharField(max_length=100, null=True, blank=True, verbose_name="College/University")
  name_of_degree = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Degree")
  duration_from = models.DateField(null=True, blank=True, verbose_name="From")
  duration_to = models.DateField(null=True, blank=True, verbose_name="To")
  specialization = models.CharField(max_length=100, null=True, blank=True, verbose_name="Specialization")
  percentage = models.FloatField(null=True, blank=True, verbose_name="Percentage")
  certificates = models.FileField(upload_to ='Certificates/Project',  default=None, null=True, blank=True, verbose_name="Certificates")

  status = models.BooleanField(default=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Educations"
    verbose_name = "Education"
  
  def __str__(self):
    return self.education


class Countries_travelled(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  country_travelled = models.CharField(max_length = 255, null = True, blank=True, verbose_name = 'Country Travelled')
  duration_of_travel = models.DateField(null=True, blank=True, verbose_name = 'Duration of Travel')
  purpus_of_travel = models.CharField(max_length = 255, null=True, blank=True, verbose_name = 'Purpus of Travel')


class Countries_refused(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  
  country = models.CharField(max_length = 255, blank=True, null = True ,verbose_name = 'Country')
  date_of_application = models.DateField(null = True, blank=True, verbose_name = 'Date of Application') # shoud contain null=True
  type_of_visa = models.CharField(blank=True, max_length = 255, null=True, verbose_name = 'Type of Visa') 
  resion_of_refused = models.CharField(max_length = 255, blank=True, null=True, verbose_name = 'Reason of Refusl/Denial')


class Languages(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  language = models.CharField(max_length = 255, null=True, blank=True, verbose_name = 'Language')
  speek = models.BooleanField(default=False, blank=True)
  read = models.BooleanField(default=False, blank=True)
  write = models.BooleanField(default=False, blank=True)

  def __str__(self):
    return self.language


class Employee_history(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  change_leaving = models.CharField(max_length = 255, null = True, blank=True, verbose_name = 'Reason for Seeking change/leaving')
  phonoe = models.CharField(max_length=100, blank=True,null=True, verbose_name = 'Phone No.')
  current_designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Current Designation')
  industry_type = models.CharField(max_length = 100,  null=True, blank=True, verbose_name='Industry Type')
  employee_service_from = models.DateField(null=True, blank=True, verbose_name='from')
  employee_service_to = models.DateField(null=True, blank=True, verbose_name='to')
  starting_salary = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Starting Salary')
  current_salary = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Current Salary')
  supervisor = models.CharField(max_length = 255, blank=True, null=True, verbose_name = 'Name $ Designation of Supervisor')


class Previous_Employment(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  email = models.EmailField(max_length=250,   null=True, blank=True, verbose_name="demo@gmail.com")
  period_of_service_from = models.DateField(null=True, blank=True, verbose_name='from')
  period_of_service_to = models.DateField(null=True, blank=True, verbose_name='to')
  designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Designation')
  nature_of_duties = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Nature of Duties')
  salary = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Last Salary Drawn')


class Reference(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name")
  designation = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Designation')
  address = models.TextField( null=True, blank=True, verbose_name="Address")
  email = models.EmailField(max_length=250,  null=True, blank=True, verbose_name="demo@gmail.com")
  phonoe = models.CharField (max_length = 100, blank=True, null=True, verbose_name = 'Phone No.')
  nature_of_association = models.CharField(max_length = 100,  null=True, blank=True, verbose_name='Nature of Association')


class General(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  
  name_of_company = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Company")
  position_applied_for = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Position Applied For")
  date_of_application = models.DateField(null=True, blank=True, verbose_name='Date of Application')
  reason = models.CharField(max_length = 100,  null=True, blank=True, verbose_name= 'Reasion for NOt joining')


class Emoluments(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  basic = models.CharField (max_length = 100,blank=True, null=True, verbose_name = 'Basic')
  da = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'DA')
  cca = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'CCA')
  hra = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'HRA')
  conveyance = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'Conveyance')
  lta = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'LTA')
  anyother_allowences = models.CharField(max_length = 100,blank=True, null=True, verbose_name = 'Anyother')
  cross_income = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Gross Income')
  pf = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'PF')
  medical = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Medical')
  insurance = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Insurance')
  any_other_deductions = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Any Other Deduction')
  gross_deduction = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Gross Deduction')
  net_salary = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Net Salary per Annum')


class Persanal_detail(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name Mr./Ms.")
  father_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  gender = models.CharField(max_length=250,  null=True, blank=True, verbose_name="Sex", choices=GENDER_CHOICES)
  employe_id = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Employee ID')
  husband_name = models.CharField(max_length=100,  null=True, blank=True, verbose_name="Name of Father")
  p_dob = models.DateField(null=True, blank=True, verbose_name="Date Of Birth")
  p_joining_date = models.DateField(blank=True, null=True, max_length = 100, verbose_name = 'Joining Date')
  joining_location = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Joining Location')
  social_security_Number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Social Security Number (If applicable)")


class Associates_address(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  building_apt_name = models.CharField(max_length = 100, null=True,  blank=True, verbose_name = 'Building/Apt. Name:')
  H_D_Flat_No = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'H.No/D.No/Flat.No')
  street_colony = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Street/Colony Name')
  landmark = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'Landmark')
  city = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'City')
  state = models.CharField(max_length = 100, null=True, blank=True, verbose_name = 'State')
  pincode = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Pincode')
  phonoe = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Phone No' )
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  duration_of_stay_from = models.DateField(null=True, blank=True,  verbose_name= 'Duration of stay From')
  duration_of_stay_to = models.DateField(null=True, blank=True, verbose_name= 'Duration of stay To')


class Candidate_declaration_form(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
  source = models.CharField(max_length=100, null=True, blank=True, verbose_name='Source')
  date = models.DateField(null=True, blank=True, verbose_name='Date')
  declaration_1 = models.BooleanField(default=False, blank=True, verbose_name =" My resumeis a trusted document that confirms the authenticity of my assignments, education & other credentials and will be used to decide my remuneration (needs to be supported by documentation). The same is true to my knowledge and has not been modified in any way by any employee or channel partner. I also acknowledge the fact completely without any exception that iflam found to have misrepresented or withheld any information, it will lead to disqualification of my candidature permanentlyor termination of employment with immediate effect.")
  declaration_2 = models.BooleanField(default=False, blank=True, verbose_name= "The details in my resume/application form will be used to complete a reference check which is a process comprising criminal antecedents, previous employments & address verifications. (If you feel your resume has a discrepancy, then please bring it to the notice of the Talent Acquisition Team)")
  declaration_3 = models.BooleanField(default=False, blank=True,verbose_name= "I Thereby confirm that I have not paid anything incash or kind to any employee/affiliates/vendors of Tech Mahindra Ltd./Tech Mahindra Business Services Ltd. to get my job offer")
  declaration_4 = models.BooleanField(default=False, blank=True, verbose_name= "I Thereby declare that I'm not a defaulter with any of the banks operating in India")
  declaration_5a = models.BooleanField(default=False,blank=True, verbose_name= "HSC/Graduation Mark sheet")
  declaration_5b = models.BooleanField(default=False, blank=True, verbose_name= "Offer Letter (previous employer/s)")
  declaration_5c = models.BooleanField(default=False, blank=True, verbose_name= "Experience Letter (previous employer/s)")
  declaration_5d = models.BooleanField(default=False, blank=True, verbose_name= "Salary/Bank Statements (last 3 Months - last/current employer)")
  declaration_5e = models.BooleanField(default=False, blank=True, verbose_name= "PAN Card")
  declaration_5f = models.BooleanField(default=False, blank=True, verbose_name= "Address Proof")
  declaration_5g = models.BooleanField(default=False, blank=True, verbose_name= "Date of Birth Proof")
  declaration_5h = models.BooleanField(default=False, blank=True, verbose_name= "Photo ID Proof")
  declaration_6 = models.BooleanField(default=False, blank=True, verbose_name= "Self-attested photocopies of Candidate documents willbe used for Internal checks and Background Verification purpose hence will not be returned.")
  declaration_7 = models.BooleanField(default=False, blank=True, verbose_name= "I live within Tech Mahindra Ltd. /Tech Mahindra Business Services Ltd. Transport boundaries and have confirmed the same with the recruiting SPOC: (If not then please respond to the statement below)")
  declaration_8 = models.BooleanField(default=False, blank=True, verbose_name= "If I live beyond the above mentioned transport boundaries I am willing to relocate. Note: Tech Mahindra Ltd./ Tech Mahindra Business Services Ltd. will not entertain any request for Transport outside the transport boundaries during your tenure.")
  declaration_9 = models.BooleanField(default=False, blank=True, verbose_name= "I am aware of the transport deduction in casel avail the company transport(For Hyderabad/Noida/Chandigarh Only)")
  declaration_10 = models.BooleanField(default=False, blank=True, verbose_name= "I am willing to work in 24*7 (rotational shifts as per the business need) with split weekly offs")
  declaration_11 = models.BooleanField(default=False, blank=True, verbose_name= "Notwithstanding anything to the contrarystated elsewhere in the employment contract, I understand that I cannot availanyleaves in the first 6 months of employment.")
  declaration_12 = models.BooleanField(default=False, blank=True, verbose_name= "I will adhere to theinduction/Trainingshift timings / office working hoursincluding but not limited to Log-in/Logout and will comply with the same. I shall not violate the same for reason whatsoever including but not limited to religious activities.")
  declaration_13 = models.BooleanField(default=False, blank=True, verbose_name= "I hereby declare that I'm not a Full time/ Part Timeregular college student and would not requireleaves for any exams forthe next 6 months. I admit I have no plans to pursue further studies andl do not have any backlogs of exams pending.")
  declaration_14 = models.BooleanField(default=False, blank=True, verbose_name= "I agree that I do not suffer from any medical condition that will hinder my On Job performance.")
  declaration_15 = models.BooleanField(default=False, blank=True, verbose_name= "I am not required to undertake any planned hospitalization for any medical conditioninthe next 6 months.")
  declaration_16 = models.BooleanField(default=False, blank=True, verbose_name= "I understand that I will be eligible for any IJP/growth only posts 18 months (minimum) from my date of joining.")
  declaration_17 = models.BooleanField(default=False, blank=True, verbose_name= "I have not been or notlisted by any government agency as being barred, suspended, proposed for suspension or debarment, or otherwise ineligible for participation in any government procurement programmes or contracts.")
  declaration_18 = models.BooleanField(default=False, blank=True, verbose_name= "I have not at any time been found by a courtin any jurisdiction to have engagedin any offence involving bribery, corruption or similar activity.")
  declaration_19 = models.BooleanField(default=False, blank=True, verbose_name= "To the best of my knowledge, I have at any time not been investigated or been suspected in anyjurisdiction of having engagedin any corrupt or other similar activity.")
  declaration_20= models.BooleanField(default=False, blank=True, verbose_name= "I am not a government Official; or officials of a foreign political party or any candidate for any foreign political office or other persons who might assert a corruptor illegal influence on behalf of either party to this Agreement or on behalf of principals, directors, employees, partners, consultants, agents, representatives, officers or shareholders of any existing or potential customer; andl will immediately notify Tech Mahindra Ltd. /Tech Mahindra Business Services Ltd. in writingifl become aware of anybreach of the above clauses.")
  declaration_21 = models.BooleanField(default=False, blank=True, verbose_name= "I hereby declare to comply with the Business Data Protection policy of Tech Mahindra Ltd. / Tech Mahindra Business Services Ltd. which prohibits the usage of mobile phones, tablets, phablets or any other similar device on the operations floor & other work related areas a part from cafeterias/snacketerias. These devices have to be keptin switched off mode (applicable to Advisors and TC/Execs)")


class Candidate_acceptance_form(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
  application_id = models.CharField(max_length = 100, null=True, blank=True, verbose_name='Application ID')
  source = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Source', choices=SOURCE)
  name_of_source = models.CharField(max_length=100, blank=True, null=True, verbose_name = 'Name of Source')
  officer_code = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Officee Code', choices=OFFICER_CODE)
  employee_class = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Employee Class', choices=EMPLOYEE_CLASSES)
           ########### Relevent Experience Fixation #########
  type_of_experience = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Type of Experience', choices=TYPE_OF_EXPERIENCE)
  total_experience = models.CharField(max_length=100, null=True, blank=True, verbose_name='Total Experience')
  relevant_experience = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Revelant Experience')
  remarks  = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Remarks ')
    ######## Employment & Fitment Related Information  ########
  current_location = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Current Location')
  location_constraints = models.CharField(max_length = 100, null=True, blank=True, verbose_name= 'Location Constraints', choices=MARITAL_STATUS)
  location_preference = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Location Preference',)
  is_passport_valid = models.CharField(max_length = 100, blank=True,null=True, verbose_name = 'Is Passport valid ?', choices=MARITAL_STATUS)
  ready_to_travel = models.CharField(max_length = 100, blank=True, null=True, verbose_name = ' Ready to Travel (including Onsite)?', choices=MARITAL_STATUS)
  visa_rejected = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Was visa ever rejected ?', choices=MARITAL_STATUS)
  offered_ctc_excluding = models.CharField(max_length=100, null=True, blank=True, verbose_name='Offered CTC (excluding Gratuity & Insurance) ')
  offered_ctc_including = models.CharField(max_length=100, null=True, blank=True, verbose_name='Offered CTC (including Gratuity & Insurance) ')
  expected_ctc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Expected CTC (Annual)')
  current_ctc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Current CTC (Annual)')
  job_role = models.CharField(max_length=100, null=True, blank=True, verbose_name='Proposed Band & Job Role/ Designation')
  type_of_employment = models.CharField(max_length = 100,null=True, blank=True, verbose_name = ' Type of Employment', choices=EMPLOY_TYPE)
  contract_start_date = models.DateField(null = True, blank=True, verbose_name = 'Contract Start Date')
  contract_duration = models.CharField(max_length = 100,null=True, blank=True, verbose_name = 'Contract Duration (in months)')
  joining_date = models.DateField(null = True, blank=True, verbose_name = 'Joining Date')
  joining_location = models.CharField(max_length = 100, blank=True,null=True, verbose_name = 'Joining Location')
    ############ Commitments & Relevant Information ########
  guest_house_accommodation = models.CharField(max_length = 100,null=True, blank=True, verbose_name = 'Guest House Accommodation? ', choices=MARITAL_STATUS)
  willing_work = models.CharField(max_length = 100, blank=True, null=True, verbose_name = 'Willing to work in Shifts ? 24x7 ', choices=MARITAL_STATUS)
  notice_period = models.CharField(max_length = 100, blank=True,null=True, verbose_name = 'Notice Period in Months')
  expected_joining_date = models.DateField(null = True, blank=True, verbose_name = 'Expected Date Of Joining ')
  comments = models.TextField(blank=True, null=True, verbose_name = 'Any Other Commitment(s) (Pls specify here)')
  declaration = models.BooleanField(default=False, blank=True, verbose_name = 'I hereby, confirm that I understand all above details/information and I have no observation of any kind on any of the above information/commitments.')
  recruter_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Recruiter's Name")
  authority_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Name of Approving Authority")






