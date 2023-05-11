from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user_rate = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class RatingSerializer(serializers.Serializer):
    rate = serializers.IntegerField()

    def validate_rate(self, value):
        if not (value<=5 and value>=0):
            raise ValidationError('Rate number must be an integer between 0 and 5.')
        return value

