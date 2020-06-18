from django.db import models

# Create your models here.

class UserLogin(models.Model):
    user_phone_no = models.CharField(max_length=10, unique=True)
    user_email = models.EmailField(max_length=50, unique=True)
    user_password = models.CharField(max_length=15)
    user_login_data_time = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=8)
    user_otp = models.CharField(max_length=6)
    user_section = models.IntegerField(default=0)
    user_pay = models.BooleanField(default=False)
    user_pay_expery = models.IntegerField(default=0)
    
class EmployerDetails(models.Model):
    user_id = models.OneToOneField(UserLogin, on_delete=models.CASCADE,limit_choices_to={'user_type': 'employer'})
    eyer_phone = models.CharField(max_length=10)
    eyer_gst_no = models.CharField(max_length=15)
    eyer_hotel_name = models.CharField(max_length=15)
    eyer_address_1 = models.CharField(max_length=50)
    eyer_address_2 = models.CharField(max_length=50)
    eyer_city = models.CharField(max_length=40)
    eyer_state = models.CharField(max_length=40)
    eyer_website = models.CharField(max_length=50)
    eyer_type = models.CharField(max_length=20)
    eyer_category = models.CharField(max_length=50)
    eyer_cuisines = models.CharField(max_length=50)
    eyer_no_seats = models.IntegerField(default=0)
    eyer_active_job_post = models.IntegerField(default=0)
    eyer_tot_no_job_post = models.IntegerField(default=0)
    eyer_job_offer = models.IntegerField(default=0)
    eyer_job_hier = models.IntegerField(default=0)

class EmployeeDetails(models.Model):
    user_id = models.OneToOneField(UserLogin, on_delete=models.CASCADE, limit_choices_to={'user_type': 'employee'})
    eyee_phone = models.CharField(max_length=10)
    eyee_name = models.CharField(max_length=50)
    eyee_aadhar_no = models.CharField(max_length=12)
    eyee_age = models.CharField(max_length=2)
    eyee_gender = models.CharField(max_length=15)
    eyee_address_1 = models.CharField(max_length=50)
    eyee_address_2 = models.CharField(max_length=60)
    eyee_city = models.CharField(max_length=40)
    eyee_state = models.CharField(max_length=40)
    eyee_type_hotel = models.CharField(max_length=80)
    eyee_education = models.CharField(max_length=250)
    eyee_choice = models.CharField(max_length=20)
    eyee_time = models.CharField(max_length=20)
    eyee_pre_experience = models.CharField(max_length=20)
    eyee_place_pre_experience = models.CharField(max_length=20)
    eyee_add_skills = models.CharField(max_length=300)
    eyee_salary_expected = models.CharField(max_length=20)
    eyee_no_appiled = models.IntegerField(default=0)
    eyee_no_accept = models.IntegerField(default=0)
    eyee_no_rejected = models.IntegerField(default=0)
    eyee_no_post_liked = models.IntegerField(default=0)

class JobPost(models.Model):
    eyer_id = models.ForeignKey(EmployerDetails, related_name='eyer_id',  on_delete=models.DO_NOTHING)
    eyer_name = models.CharField(max_length=50)
    eyer_location = models.CharField(max_length=50)
    eyer_number = models.IntegerField(default=0)
    job_post = models.CharField(max_length=50)
    job_salary = models.CharField(max_length=30)
    job_experience = models.CharField(max_length=20)
    job_employment = models.CharField(max_length=20)
    job_gender = models.CharField(max_length=15)
    job_age = models.IntegerField(default=0)
    job_education = models.CharField(max_length=20)
    job_skills = models.CharField(max_length=50)
    job_discription = models.TextField(max_length=300)
    job_working_days = models.CharField(max_length=10)
    job_working_shifts = models.CharField(max_length=30)
    job_benefits = models.CharField(max_length=200)
    job_posted_by = models.CharField(max_length=80)
    job_posted_designation = models.CharField(max_length=50)
    job_no_emplyee_appilied = models.IntegerField(default=0)
    job_no_emplyee_offered = models.IntegerField(default=0)
    job_post_opened = models.IntegerField(default=0)
    job_active = models.BooleanField(default=True)

class JobOffer(models.Model):
    eyer_id = models.ForeignKey(EmployerDetails, on_delete=models.DO_NOTHING)
    eyer_name = models.CharField(max_length=50)
    job_id = models.ForeignKey(JobPost,  on_delete=models.DO_NOTHING)
    job_post = models.CharField(max_length=50)
    eyee_id = models.ForeignKey(EmployeeDetails,  on_delete=models.DO_NOTHING)
    eyee_name = models.CharField(max_length=50)
    job_active = models.BooleanField(default=True)
    offer_letter = models.CharField(max_length=1000)

class JobApplied(models.Model):
    eyee_id = models.ForeignKey(EmployeeDetails,  on_delete=models.DO_NOTHING)
    eyee_name = models.CharField(max_length=50)
    eyer_id = models.ForeignKey(EmployerDetails, on_delete=models.DO_NOTHING)
    eyer_name = models.CharField(max_length=50)
    job_id = models.ForeignKey(JobPost,  on_delete=models.DO_NOTHING)
    job_post = models.CharField(max_length=50)
    reason = models.CharField(max_length=300)
    what_can_he_do = models.CharField(max_length=300)
    quries =  models.CharField(max_length=300)
    job_active = models.BooleanField(default=True)
    short_listed = models.BooleanField(default=False)

class ShortListed(models.Model):
    job_id = models.ForeignKey(JobPost,  on_delete=models.DO_NOTHING)
    eyee_id = models.ForeignKey(EmployeeDetails,  on_delete=models.DO_NOTHING)
    short_list_type = models.CharField(max_length=20)
    short_list_type_id = models.CharField(max_length=20)
    job_active = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)     

class EmployerDetailsFav(models.Model):
    eyer_id = models.ForeignKey(EmployerDetails,  on_delete=models.DO_NOTHING)
    eyer_name = models.CharField(max_length=50)
    eyee_id = models.ForeignKey(EmployeeDetails,  on_delete=models.DO_NOTHING)
    eyee_name = models.CharField(max_length=50)

class EmployeeDetailsFav(models.Model):
    eyee_id = models.ForeignKey(EmployeeDetails,  on_delete=models.DO_NOTHING)
    eyee_name = models.CharField(max_length=50)
    job_id = models.ForeignKey(JobPost,  on_delete=models.DO_NOTHING)
    job_post = models.CharField(max_length=50)
