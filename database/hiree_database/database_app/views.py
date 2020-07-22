from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import UserLogin
from .models import EmployerDetails
from .models import EmployeeDetails
from .models import JobPost
from .models import JobOffer
from .models import JobApplied
from .models import ShortListed
from .models import EmployerDetailsFav
from .models import EmployeeDetailsFav
from .models import LoginData
from .serializer import UserLoginSerializers
from .serializer import EmployerDetailsSerializers
from .serializer import EmployeeDetailsSerializers
from .serializer import JobPostSerializers
from .serializer import JobOfferSerializers
from .serializer import JobAppliedSerializers
from .serializer import ShortListedSerializers
from .serializer import EmployerDetailsFavSerializers
from .serializer import EmployeeDetailsFavSerializers
from .serializer import LoginDataSerializers
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as FilterSet
import django_filters.rest_framework
from rest_framework.views import APIView
from datetime import datetime
import requests
import random
# Create your views here.

class UserAuthentication(ObtainAuthToken):
    def post(self, request,):
        serializer = self.serializer_class(data=request.data, context=(request)) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token.created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class ValidatePhoneSendOTP(APIView):
    queryset = LoginData.objects.all()
    serializer_class = LoginDataSerializers
    def post(self, request, *args, **kwargs):
        serializer = LoginDataSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone']
        print(phone_number)
        if phone_number:
            phone = str(phone_number)
            user = UserLogin.objects.filter(user_phone_no__iexact = phone)
            if user.exists():
                key = sendotp(phone)
                if key:
                    data = LoginData.objects.filter(phone__iexact = phone)
                    if data.exists():
                        otp = str(key)
                        url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                        r = requests.get(url)
                        if r.status_code == 200:
                            data = data.first()
                            data.data_time = datetime.now()
                            data.otp = key
                            data.save()
                            return Response({
                                'status': True,
                                'detail': 'phone number is present in both',
                                'otp': key,
                                'time': 'exists'
                            })
                        else :
                            return Response({
                                'status': True,
                                'detail': 'error in sending otp'
                            })
                    else:
                        otp = str(key)
                        url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                        r = requests.get(url)
                        if r.status_code == 200:
                            serializer.save()
                            data = LoginData.objects.filter(phone__iexact = phone)
                            data = data.first()
                            data.data_time = datetime.now()
                            data.otp = key
                            data.save()
                            return Response({
                                'status': True,
                                'detail': 'phone number is present',
                                'otp': key
                            })
                        else:
                            return Response({
                                'status': True,
                                'detail': 'error in sending otp'
                            })
                else:
                    return Response({
                    'status': False,
                    'detail': 'Genrating otp error'
                })
            else :
                key = sendotp(phone)
                if key:
                    otp = str(key)
                    url = 'http://2factor.in/API/V1/99e679bc-cb75-11ea-9fa5-0200cd936042/SMS/'+phone+'/'+otp+'/EZEEJOBS'
                    r = requests.get(url)
                    if r.status_code == 200:
                        serializer.save()
                        data = LoginData.objects.filter(phone__iexact = phone)
                        data = data.first()
                        data.data_time = datetime.now()
                        data.otp = key
                        data.save()
                        return Response({
                        'status': True,
                        'detail': 'phone number added',
                        'otp': key
                    })
                    else:
                        return Response({
                            'status': True,
                            'detail': 'error in sending otp'
                        })
                else:
                    return Response({
                    'status': False,
                    'detail': 'Genrating otp error'
                })
        else:
            return Response({
                    'status': False,
                    'detail': 'phone number not given in the post request'
                })


class JobPostFilterSet(django_filters.FilterSet):
    negated_job_salary = django_filters.Filter('job_salary', exclude=True)
    negated_eyer_location = django_filters.Filter('eyer_location', exclude=True)
    negated_job_gender = django_filters.Filter('job_gender', exclude=True)
    negated_job_education = django_filters.Filter('job_education', exclude=True)
    negated_job_experience = django_filters.Filter('job_experience', exclude=True)
    negated_job_age = django_filters.Filter('job_age', exclude=True)

    class Meta:
        model = JobPost
        fields = ['eyer_id', 'job_active','job_post','job_salary','eyer_location','job_gender','job_education','job_experience','job_age']

class EmployeeDetailsFilterSet(django_filters.FilterSet):
    negated_eyee_salary_expected = django_filters.Filter('eyee_salary_expected', exclude=True)
    negated_eyee_pre_experience = django_filters.Filter('eyee_pre_experience', exclude=True)
    negated_eyee_education = django_filters.Filter('eyee_education', exclude=True)
    negated_eyee_address_2 = django_filters.Filter('eyee_address_2', exclude=True)
    negated_eyee_type_hotel = django_filters.Filter('eyee_type_hotel', exclude=True)
    negated_eyee_age = django_filters.Filter('eyee_age', exclude=True)
    negated_eyee_gender = django_filters.Filter('eyee_gender', exclude=True)

    class Meta:
        model = EmployeeDetails
        fields = ['user_id','eyee_choice','eyee_salary_expected','eyee_pre_experience','eyee_education','eyee_city','eyee_type_hotel','eyee_age','eyee_gender']


class UserLoginViewSet(viewsets.ModelViewSet):
    
    queryset = UserLogin.objects.all().order_by('user_login_data_time')
    serializer_class = UserLoginSerializers
    
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('user_phone_no',)

class EmployerDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployerDetails.objects.all()
    serializer_class = EmployerDetailsSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('user_id',)

class EmployeeDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('user_id','eyee_choice','eyee_salary_expected','eyee_pre_experience','eyee_education','eyee_city','eyee_type_hotel','eyee_age','eyee_gender',)
    ordering_fields = '__all__'
    filter_class = EmployeeDetailsFilterSet
    


class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('eyer_id', 'job_active','job_post','job_salary','eyer_location','job_gender','job_education','job_experience','job_age')
    search_fields = ('eyer_name','eyer_location','job_post')
    ordering_fields = '__all__'
    filter_class = JobPostFilterSet

class JobOfferViewSet(viewsets.ModelViewSet):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id','eyee_id','job_active', 'short_listed','eyer_id' )


class JobAppliedViewSet(viewsets.ModelViewSet):
    queryset = JobApplied.objects.all()
    serializer_class = JobAppliedSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id','eyee_id', 'job_active', 'short_listed')   

class ShortListedViewSet(viewsets.ModelViewSet):
    queryset = ShortListed.objects.all()
    serializer_class = ShortListedSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id','eyee_id','confirmed', 'job_active')   

class EmployerDetailsFavViewSet(viewsets.ModelViewSet):
    queryset = EmployerDetailsFav.objects.all()
    serializer_class = EmployerDetailsFavSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('eyer_id','unliked')   

class EmployeeDetailsFavViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetailsFav.objects.all()
    serializer_class = EmployeeDetailsFavSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('eyee_id','unliked')   

def sendotp(phone):
    if phone:
        key = random.randint(999, 9999)
        return key
    else: 
        return False

