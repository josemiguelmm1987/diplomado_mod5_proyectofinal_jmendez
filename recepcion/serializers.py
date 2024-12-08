from rest_framework import serializers
from .models import Procedencia, Remitente, Documento

class ProcedenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedencia
        fields = "__all__"

class RemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remitente
        fields = "__all__"

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"

class ReporteDocumentoSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    documentos = DocumentoSerializer(many=True)
