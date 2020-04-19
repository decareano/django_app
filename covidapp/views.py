

from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import HospitalForm

# Create your views here.
from .models import Hospital

def hospital_create_view(request):
	form = HospitalForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = HospitalForm()
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'form': form
	}
	return render(request, "covidapp/hospital_create.html", context) 

def hospital_detail_view(request, id):
	obj = Hospital.objects.get(id=id)
	
	# context = {
	# 	'hospitalCurrently': obj.hospital_currently,
	# 	'deadDaily': obj.dead_daily,
	# 	'hospitalIncrease': obj.hospital_increase,
	# 	'ICUincrease': obj.ICU_currently,
	# }
	# try:
	# 	obj = Hospital.objects.get(id=id)
	# except Hospital.DoesNotExist:
	# 	raise Http404
	context = {
		"object": obj
	}
	return render(request, "covidapp/hospital_detail.html", context)

def hospital_list_view(request):
	queryset = Hospital.objects.all() #list of objects 
	context = {
		"object_list": queryset       # object_list is the key and queryset is the value
	}
	return render(request, "covidapp/hospital_list.html", context)
