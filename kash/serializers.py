from rest_framework import serializers
from .models import News



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title_uz','title_ru','description_uz','description_ru','creator','date_create')

