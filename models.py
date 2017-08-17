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
    initial_date = models.DateTimeField(verbose_name='Data Inicial')
    final_date = models.DateTimeField(verbose_name='Data Final')
    app = models.ForeignKey(App)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    def get_hashtags(self):
        return Hashtags.objects.filter(project=self)

    def get_termos(self):
        return Termos.objects.filter(project=self)

    def get_pessoas(self):
        return Pessoas.objects.filter(project=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Detalhes(models.Model):
    project = models.ForeignKey(Projeto, verbose_name="Projeto")
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        abstract = True


class Hashtags(Detalhes):
    tag = models.CharField(max_length=60, verbose_name="Tag", help_text='Somente texto, não precisa do "#"')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Hashtag"
        verbose_name_plural = "Hashtags"


class Termos(Detalhes):
    termo = models.CharField(max_length=200, verbose_name="Termo")

    def __str__(self):
        return self.termo

    class Meta:
        verbose_name = "Termo"
        verbose_name_plural = "Termos"


class Pessoas(Detalhes):
    username = models.CharField(max_length=60, verbose_name="Username", help_text='Somente texto, não precisa do "@"')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Tweet(models.Model):
    project = models.ForeignKey(Projeto, verbose_name="Projeto")
    id_tweet = models.IntegerField(verbose_name="ID do Tweet")
    posted_at = models.DateTimeField(verbose_name="Postado em")
    retweeted = models.BooleanField(default=False, verbose_name="Retuitado")
    retweeted_count = models.IntegerField(default=0, verbose_name="Total de Retweets")
    screen_name = models.CharField(max_length=100, verbose_name="Autor do Tweet")
    text = models.TextField(max_length=500, verbose_name="Texto")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    def __str__(self):
        return str(self.id_tweet)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
