from django.contrib import admin

# Register your models here.
from .models import Incidentes, ModeloDeDadosUnificados

admin.site.site_header = "EDP Admin"
admin.site.site_title = "EDP Admin"
admin.site.index_title = "Welcome to EDP Admin Portal"


class IncidentesAdmin(admin.ModelAdmin):
    list_display = ["name", "reporting_level", "create_time", "consequence_severity"]
    exclude = ["id"]
admin.site.register(Incidentes, IncidentesAdmin)


class ModeloDeDadosUnificadosAdmin(admin.ModelAdmin):
    list_display = ["incident_code", "open_date", "impact"]
    exclude = ["id"]
admin.site.register(ModeloDeDadosUnificados, ModeloDeDadosUnificadosAdmin)
