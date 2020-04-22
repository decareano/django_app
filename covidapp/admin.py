from django.contrib import admin


# Register your models here.
from .models import Hospital

# class HospitalA(admin.ModelAdmin):
# 	list_display = ("hospital", "description")

admin.site.register(Hospital)
admin.site.site_header = "Covid App"

# Register your models here.
