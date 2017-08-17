from django.conf.urls import url, include
from apps.analytics_twitter.api import ProjetoViews
from rest_framework import routers
from apps.analytics_twitter.views import ProjetoDetalheLoggado

router = routers.DefaultRouter()
router.register(r'projetos', ProjetoViews)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^(?P<pk>[\w\-]+)/detalhe', ProjetoDetalheLoggado.as_view()),

]
