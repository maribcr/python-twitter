from rest_framework import viewsets
from apps.analytics_twitter.serializers import *
from apps.analytics_twitter.models import *


class ProjetoViews(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
