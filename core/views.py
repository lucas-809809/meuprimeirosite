from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data()
        contexto['funcionarios'] = Funcionario.objects.all()
        return contexto

