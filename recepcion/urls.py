from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'procedencias', views.ProcedenciaViewSet)
router.register(r'remitentes', views.RemitenteViewSet)
router.register(r'documentos', views.DocumentoViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact),
    # path('', views.index, name='index')
    path('', include(router.urls)),
    path('procedencia/count/', views.procedencia_count, name='procedencia-count'),
    path('documento/filtrar/tipo/', views.documento_tipo, name='documento_tipo'),
    path('documento/reporte/', views.reporte_documento, name='reporte_documento'),
]