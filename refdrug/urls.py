
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('timesheet/', include('timesheet.urls')),
    path('admin/', admin.site.urls),
]
