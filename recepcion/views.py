from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import ProcedenciaSerializer, RemitenteSerializer, DocumentoSerializer, ReporteDocumentoSerializer

from .models import Procedencia, Remitente, Documento

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a la Aplicación de Hojas de Ruta Gestor")

def contact(request, name):
    return HttpResponse(f"Hello, {name}")

class ProcedenciaViewSet(viewsets.ModelViewSet):
    queryset = Procedencia.objects.all()
    serializer_class = ProcedenciaSerializer

class RemitenteViewSet(viewsets.ModelViewSet):
    queryset = Remitente.objects.all()
    serializer_class = RemitenteSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

@api_view(['GET'])
def procedencia_count(request):
    try:
        cantidad = Procedencia.objects.count()
        return JsonResponse({"cantidad": cantidad}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)

@api_view(['GET'])
def documento_tipo(request):
    try:
        tipos = Documento.objects.filter(tipo_documento='CITE')
        return JsonResponse(DocumentoSerializer(tipos, many=True).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)
    
@api_view(['GET'])
def reporte_documento(request):
    try:
        # documentos = Documento.objects.filter(tipo_documento='CITE')
        documentos = Documento.objects.all()
        return JsonResponse(ReporteDocumentoSerializer({"cantidad": documentos.count(), "documentos": documentos}).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)