import re
from .models import News
from rest_framework import serializers


# для просмотра берем обычный сериализатор
class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def validate_title(self, title):
        if re.match(r'\d', title):
            raise serializers.ValidationError('The name must not start with a number!')
        return title
