from django.db import models

# Create your models here.


class App(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nome")
    consumer_key = models.CharField(max_length=200)
    consumer_secret = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_secret = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "App"
        verbose_name_plural = "Apps"


class Projeto(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nome")
    real_time = models.BooleanField(default=True, verbose_name="Tempo Real", help_text='Este campo influência' 
                                                                                       ' no tempo de atualização'
                                                                                       ' dos dados.')
    app = models.ForeignKey(App)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = "Projetos"
