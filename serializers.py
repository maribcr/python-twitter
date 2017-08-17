from apps.analytics_twitter.models import *
from rest_framework import serializers


class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ('username', 'total')


class HashtagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtags
        fields = ('tag', 'total')


class TermosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termos
        fields = ('termo', 'total')


class ProjetoSerializer(serializers.ModelSerializer):
    pessoas = serializers.SerializerMethodField()
    hashtags = serializers.SerializerMethodField()
    termos = serializers.SerializerMethodField()

    class Meta:
        model = Projeto
        fields = ('name', 'real_time', 'pessoas', 'hashtags', 'termos')

    def get_pessoas(self, obj):
        pessoas = obj.get_pessoas()
        return PessoasSerializer(pessoas, many=True).data

    def get_hashtags(self, obj):
        tags = obj.get_hashtags()
        return HashtagsSerializer(tags, many=True).data

    def get_termos(self, obj):
        termos = obj.get_termos()
        return TermosSerializer(termos, many=True).data
