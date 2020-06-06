from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from .models import User
from .models import Workday


@admin.register(User)
class ViewAdmin(ImportExportModelAdmin):
	pass
###
@admin.register(Workday)
class ViewAdmin(ImportExportModelAdmin):
	pass
