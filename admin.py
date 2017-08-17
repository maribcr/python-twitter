from django.contrib import admin
from apps.analytics_twitter.models import *
from apps.analytics_twitter import functions
from django.contrib import messages

# Register your models here.


class AppAdmin(admin.ModelAdmin):
    model = App


admin.site.register(App, AppAdmin)


class TagInline(admin.TabularInline):
    model = Hashtags


class TermoInline(admin.TabularInline):
    model = Termos


class PessoaInline(admin.TabularInline):
    model = Pessoas


class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    actions = ['init_stream', 'search', 'get_user_info']
    inlines = [TagInline, TermoInline, PessoaInline]

    def search(self, request, queryset):
        try:
            for projeto in queryset:
                consumer_key = projeto.app.consumer_key
                consumer_secret = projeto.app.consumer_secret
                access_token = projeto.app.access_token
                access_secret = projeto.app.access_secret

                functions.search(projeto, consumer_key, consumer_secret, access_token, access_secret)

            messages.add_message(request, messages.SUCCESS, 'Operação realizada com sucesso')

        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Erro: ' + str(e))
    search.short_description = "Pesquisar"

    def init_stream(self, request, queryset):
        try:
            for projeto in queryset:
                consumer_key = projeto.app.consumer_key
                consumer_secret = projeto.app.consumer_secret
                access_token = projeto.app.access_token
                access_secret = projeto.app.access_secret
                functions.stream(projeto, consumer_key, consumer_secret, access_token, access_secret)
            messages.add_message(request, messages.SUCCESS, 'Operação realizada com sucesso')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Erro: ' + str(e))
    init_stream.short_description = "Iniciar Stream"

    def get_user_info(self, request, queryset):
        try:
            for projeto in queryset:
                functions.get_user_info()

            messages.add_message(request, messages.SUCCESS, 'Operação realizada com sucesso')

        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Erro: ' + str(e))


admin.site.register(Projeto, ProjetoAdmin)


class TweetsAdmin(admin.ModelAdmin):
    model = Tweet


admin.site.register(Tweet, TweetsAdmin)
