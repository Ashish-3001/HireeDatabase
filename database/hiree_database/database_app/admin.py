from django.contrib import admin
from .models import UserLogin
from .models import EmployerDetails
from .models import EmployeeDetails
from .models import JobPost
from .models import JobOffer
from .models import JobApplied
from .models import ShortListed
# Register your models here.

admin.site.register(UserLogin)
admin.site.register(EmployerDetails)
admin.site.register(EmployeeDetails)
admin.site.register(JobPost)
admin.site.register(JobOffer)
admin.site.register(JobApplied)
admin.site.register(ShortListed)
