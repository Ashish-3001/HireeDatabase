from django.shortcuts import render
from rest_framework import viewsets
from .models import UserLogin
from .models import EmployerDetails
from .models import EmployeeDetails
from .models import JobPost
from .models import JobOffer
from .models import JobApplied
from .models import ShortListed
from .serializer import UserLoginSerializers
from .serializer import EmployerDetailsSerializers
from .serializer import EmployeeDetailsSerializers
from .serializer import JobPostSerializers
from .serializer import JobOfferSerializers
from .serializer import JobAppliedSerializers
from .serializer import ShortListedSerializers
from rest_framework import filters
import django_filters.rest_framework
# Create your views here.

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
    filter_fields = ('user_id',)

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('eyer_id', 'job_active')

class JobOfferViewSet(viewsets.ModelViewSet):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id', 'job_active', )


class JobAppliedViewSet(viewsets.ModelViewSet):
    queryset = JobApplied.objects.all()
    serializer_class = JobAppliedSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id', 'job_active', 'short_listed')   

class ShortListedViewSet(viewsets.ModelViewSet):
    queryset = ShortListed.objects.all()
    serializer_class = ShortListedSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('job_id','confirmed', 'job_active')   


