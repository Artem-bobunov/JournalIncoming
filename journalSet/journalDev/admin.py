from django.contrib import admin
from .models import Journal
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class RegisterJournal(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['reg','dateInput','otKogo','vxnumber','isxnumber','summary','executor','perfomance','control','answertMail','note','nd']

admin.site.register(Journal,RegisterJournal)