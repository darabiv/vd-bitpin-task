from django.db.models import OuterRef, Subquery
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from .models import Article, UserRate
from .serializers import ArticleSerializer, RatingSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user_rates = UserRate.objects.filter(article=OuterRef('pk'), user=self.request.user)
        return super().get_queryset().annotate(user_rate=Subquery(user_rates.values('rate')[:1]))

    @action(methods=['post'], detail=True, serializer_class=RatingSerializer)
    def rate(self, request, pk=None):
        instance = self.get_object()
        rating_serializer = self.get_serializer(data=request.data)
        rating_serializer.is_valid(raise_exception=True)
        instance = instance.add_rate(rating_serializer.validated_data['rate'], user=request.user)
        article_serializer = ArticleSerializer(instance)
        return Response(article_serializer.data, status=status.HTTP_201_CREATED)

