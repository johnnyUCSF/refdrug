from django.shortcuts import render
from django.http import HttpResponse

from .forms import CodeForm
from .models import ENTRY

def index(request):

	if request.method == 'POST':
		form = CodeForm(request.POST)
		if form.is_valid():
			unique_code = form.cleaned_data['unique_code']
			### write into db
			ENTRY(unique_code)
			return HttpResponse('Thanks. Your timesheet entry has been saved.')
	else:
		form = CodeForm()
	return render(request, 'form.html',{'form':form})

