from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Incidentes, ModeloDeDadosUnificados


def index(request):
    return render(request, 'incidentes/index.html')


def get_incidentes(request):
    incidentes_list = Incidentes.objects.order_by("-create_time")
    context = {'incidentes_list': incidentes_list}
    return render(request, 'incidentes/get_incidentes.html', context)


def get_modelo_de_dados_unificados(request):
    modelo_de_dados_unificados_list = ModeloDeDadosUnificados.objects.order_by("-open_date")
    context = {'modelo_de_dados_unificados_list': modelo_de_dados_unificados_list}
    return render(request, 'incidentes/get_modelo_de_dados_unificados.html', context)


def incident_detail(request, incident_id):
    incident = get_object_or_404(Incidentes, pk=incident_id)
    return render(request, 'incidentes/incident_detail.html', {'incident': incident})


def mdu_detail(request, mdu_id):
    mdu = get_object_or_404(ModeloDeDadosUnificados, pk=mdu_id)
    return render(request, 'incidentes/mdu_detail.html', {'mdu': mdu})
