# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acordos(models.Model):
    # id = models.AutoField()
    datetime_acordo = models.DateTimeField()
    instituicao = models.CharField(max_length=255)
    foto_instituicao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'acordos'
        unique_together = (('id', 'datetime_acordo'),)


class Administradores(models.Model):
    # id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datetime_ultimo_login = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'administradores'
        unique_together = (('id', 'username'),)


class ConsultasMarcadas(models.Model):
    datetime_confirmacao = models.DateTimeField()
    data_consulta = models.CharField(max_length=10)
    hora_consulta = models.CharField(max_length=10)
    medicos = models.ForeignKey('Medicos', models.DO_NOTHING)
    utentes_email = models.ForeignKey('Utentes', models.DO_NOTHING, db_column='utentes_email')

    class Meta:
        managed = False
        db_table = 'consultas_marcadas'


class ConsultasRealizadas(models.Model):
    datetime_consulta_realizada = models.DateTimeField()
    valor_consulta = models.DecimalField(max_digits=9, decimal_places=2)
    diagnostico = models.CharField(max_length=255)
    prescricao = models.CharField(max_length=255)
    medicos = models.ForeignKey('Medicos', models.DO_NOTHING)
    utentes_email = models.ForeignKey('Utentes', models.DO_NOTHING, db_column='utentes_email')

    class Meta:
        managed = False
        db_table = 'consultas_realizadas'


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=255)
    descricao_especialidade = models.TextField()
    preco_consulta = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'especialidades'


class Horarios(models.Model):
    descricao_horario = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'horarios'


class Medicos(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    contacto_tel = models.CharField(max_length=45)
    foto = models.CharField(max_length=45)
    especialidades = models.ForeignKey(Especialidades, models.DO_NOTHING)
    horarios = models.ForeignKey(Horarios, models.DO_NOTHING)
    salario_mensal = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'medicos'


class MedicosAdministracaoDeConsultas(models.Model):
    # id = models.AutoField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    datetime_ultimo_login = models.DateTimeField()
    medicos = models.ForeignKey(Medicos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicos_administracao_de_consultas'
        unique_together = (('id', 'username'),)


class QuestoesOnline(models.Model):
    nome = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
    datetime_questao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'questoes_online'


class Utentes(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=255)
    contacto_tel = models.CharField(max_length=45)
    datetime_registo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'utentes'


class Vantagens(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo_vantagem = models.TextField()

    class Meta:
        managed = False
        db_table = 'vantagens'
