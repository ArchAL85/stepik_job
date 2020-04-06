from django.contrib import admin
from job.models import Specialty, Vacancy, Company
# Register your models here.

admin.site.register(Specialty)
admin.site.register(Vacancy)
admin.site.register(Company)
