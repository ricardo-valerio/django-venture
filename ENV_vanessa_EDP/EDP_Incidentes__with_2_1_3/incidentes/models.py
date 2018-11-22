# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Incidentes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    display_id = models.IntegerField(blank=True, null=True)
    ticket_type = models.CharField(max_length=255, blank=True, null=True)
    stage = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    operation_impact = models.CharField(max_length=255, blank=True, null=True)
    security_classification = models.CharField(max_length=255, blank=True, null=True)
    consequence_severity = models.CharField(max_length=255, blank=True, null=True)
    reporting_level = models.CharField(max_length=255, blank=True, null=True)
    followup_contact = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    incident_closed = models.DateTimeField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    time_of_resolution_in_days = models.IntegerField(blank=True, null=True)
    open_month = models.CharField(max_length=255, blank=True, null=True)
    open_year = models.CharField(max_length=255, blank=True, null=True)
    closed_month = models.CharField(max_length=255, blank=True, null=True)
    closed_year = models.CharField(max_length=255, blank=True, null=True)
    open_month_create_time = models.CharField(max_length=255, blank=True, null=True)
    open_year_create_time = models.CharField(max_length=255, blank=True, null=True)
    malware_detected = models.CharField(max_length=255, blank=True, null=True)
    source_of_logs = models.CharField(max_length=255, blank=True, null=True)
    host_info = models.CharField(max_length=255, blank=True, null=True)
    timestamp_arcsight = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'incidentes'
        verbose_name_plural = "incidentes"


class ModeloDeDadosUnificados(models.Model):
    id = models.IntegerField(primary_key=True)
    incident_code = models.CharField(max_length=255, blank=True, null=True)
    asset_ci = models.CharField(max_length=255, blank=True, null=True)
    security_classification = models.CharField(max_length=255, blank=True, null=True)
    info_security_typification = models.CharField(max_length=255, blank=True, null=True)
    afected_user = models.CharField(max_length=255, blank=True, null=True)
    open_date = models.DateTimeField(blank=True, null=True)
    resolution_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    impact = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.incident_code

    class Meta:
        managed = False
        db_table = 'modelo_de_dados_unificados'
        verbose_name_plural = "Modelo De Dados Unificados"
