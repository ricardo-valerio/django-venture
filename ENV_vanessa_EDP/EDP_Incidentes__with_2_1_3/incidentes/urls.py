from django.urls import path

from . import views

app_name = "incidentes"

urlpatterns = [
    path('', views.index, name='index'),
    path('get_incidentes', views.get_incidentes, name='get_incidentes'),
    path('get_modelo_de_dados_unificados', views.get_modelo_de_dados_unificados, name='get_modelo_de_dados_unificados'),
    path('incident_detail/<int:incident_id>', views.incident_detail, name='incident_detail'),
    path('mdu_detail/<int:mdu_id>', views.mdu_detail, name='mdu_detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
]


# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

######################################################
