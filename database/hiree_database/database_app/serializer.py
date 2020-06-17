from .models import UserLogin
from .models import EmployerDetails
from .models import EmployeeDetails
from .models import JobPost
from .models import JobOffer
from .models import JobApplied
from .models import ShortListed


from rest_framework import serializers

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = (
        'id',
        'user_phone_no',
        'user_email',
        'user_password',
        'user_login_data_time',
        'user_type',
        'user_otp',
        'user_section',
        'user_pay',
        'user_pay_expery')


class EmployerDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployerDetails
        fields = (
        'id',
        'user_id',
        'eyer_phone',
        'eyer_gst_no',
        'eyer_hotel_name',
        'eyer_address_1',
        'eyer_address_2',
        'eyer_city',
        'eyer_state',
        'eyer_website',
        'eyer_type',
        'eyer_category',
        'eyer_cuisines',
        'eyer_no_seats',
        'eyer_active_job_post',
        'eyer_tot_no_job_post',
        'eyer_job_offer',
        'eyer_job_hier')

class EmployeeDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = (
        'id',
        'user_id',
        'eyee_phone',
        'eyee_name',
        'eyee_aadhar_no',
        'eyee_age',
        'eyee_gender',
        'eyee_address_1',
        'eyee_address_2',
        'eyee_city',
        'eyee_state',
        'eyee_type_hotel',
        'eyee_education',
        'eyee_choice',
        'eyee_time',
        'eyee_pre_experience',
        'eyee_place_pre_experience',
        'eyee_add_skills',
        'eyee_salary_expected',
        'eyee_no_appiled',
        'eyee_no_accept',
        'eyee_no_rejected',
        'eyee_no_post_liked')


class JobPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = (
        'id',
        'eyer_id',
        'eyer_name',
        'eyer_location',
        'eyer_number',
        'job_post',
        'job_salary',
        'job_experience',
        'job_employment',
        'job_gender',
        'job_age',
        'job_education',
        'job_skills',
        'job_discription',
        'job_working_days',
        'job_working_shifts',
        'job_benefits',
        'job_posted_by',
        'job_posted_designation',
        'job_no_emplyee_appilied',
        'job_no_emplyee_offered',
        'job_post_opened',
        'job_active')

class JobOfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = (
        'id',
        'eyer_id',
        'eyer_name',
        'job_id',
        'job_post',
        'eyee_id',
        'eyee_name',
        'job_active',
        'offer_letter')

class JobAppliedSerializers(serializers.ModelSerializer):
    class Meta:        
        model = JobApplied
        fields = (
        'id',
        'eyee_id',
        'eyee_name',
        'eyer_id',
        'eyer_name',
        'job_id',
        'job_post',
        'reason',
        'what_can_he_do',
        'quries',
        'job_active',
        'short_listed',
        )

class ShortListedSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShortListed
        fields = (
        'id',
        'job_id',
        'eyee_id',
        'short_list_type',
        'short_list_type_id',
        'job_active',
        'confirmed',
        )
