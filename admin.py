from django.contrib import admin
from apps.analytics_twitter.models import *
from apps.analytics_twitter import functions
from django.contrib import messages

# Register your models here.


class AppAdmin(admin.ModelAdmin):
    model = App

admin.site.register(App, AppAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    actions = ['teste']

    def teste(self, request, queryset):
        try:
            for projeto in queryset:
                functions.search(projeto)

            messages.add_message(request, messages.SUCCESS, 'Operação realizada com sucesso')

        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Erro: ' + str(e))


admin.site.register(Projeto, ProjetoAdmin)
