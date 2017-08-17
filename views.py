from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from apps.analytics_twitter.models import Projeto


class Loggado(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Loggado, self).dispatch(*args, **kwargs)


class ProjetoDetalheLoggado(Loggado, DetailView):
    template_name = 'twitter/index.html'
    queryset = Projeto.objects.all()
    model = Projeto

    def get_context_data(self, **kwargs):
        p = kwargs
        projeto = p['object']
        # editoria = projeto.editoria
        # f = urllib.request.urlopen(editoria.render_block)
        # geraJson(projeto)
        p['projeto'] = projeto
        # p['dev'] = os.environ.get('GCN_DEBUG', '')
        # p['cabecalho'] = f.read()
        return p
