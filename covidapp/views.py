

from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import HospitalForm

# Create your views here.
from .models import Hospital
#from chartit import DataPool, Chart

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
	num_hospital = Hospital.objects.all().count()
	context = {
		"object_list": queryset, 
		"num_hospital": num_hospital,  
		#'hospitalCurrently': queryset,
    	# 'num_instances': num_instances,
    	# 'num_instances_available': num_instances_available,
    	# 'num_authors': num_authors,   # object_list is the key and queryset is the value
	}
	return render(request, "covidapp/hospital_list.html", context)

def hospital_index_view(request):
	
	num_hospital = Hospital.objects.all().count()
	context = {
		
		"num_hospital": num_hospital,  
		#'hospitalCurrently': queryset,
    	# 'num_instances': num_instances,
    	# 'num_instances_available': num_instances_available,
    	# 'num_authors': num_authors,   # object_list is the key and queryset is the value
	}
	return render(request, "covidapp/hospital_index.html", context)


# def dynamic_lookup_view(request, id):
# 	#obj = Product.objects.get(id=id)
# 	#obj = get_object_or_404(Product, id=id)
# 	try:
# 		obj = Product.objects.get(id=id)
# 	except Product.DoesNotExist:
# 		raise Http404
# 	context = {
# 		"object": obj
# 	}
# 	return render(request, "products/product_detail.html", context)

# def hospital_chart_view(request):
#     #Step 1: Create a DataPool with the data we want to retrieve.
#     hospitaldata = \
#         DataPool(
#            series=
#             [{'options': {
#                'source': Hospital.objects.all()},
#               'terms': [
#                 'date_time',
#                 'hospital_currently',
#                 'ICU_currently', 
#                 'hospital_increase', 
#                 'dead_daily',  
#                 'tested_today']}
#              ])

#     #Step 2: Create the Chart object
#     cht = Chart(
#             datasource = hospitaldata,
#             series_options =
#               [{'options':{
#                   'type': 'column',
#                   'stacking': False},
#                 'terms':{
#                   'daily': [
#                     'date_time',
#                     'hospital_currently',
#                     'ICU_currently', 
#                     'hospital_increase', 
#                     'dead_daily',  
#                     'tested_today']
#                   }}],
#             chart_options =
#               {'title': {
#                    'text': 'hospital data'},
#                'xAxis': {
#                     'title': {
#                        'text': 'daily number'}}})

#     #Step 3: Send the chart object to the template.
#     return render(request, 'hospitalchart.html', {'chart_list': [cht]})
