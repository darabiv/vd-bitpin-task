from django.db import models, transaction
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    rate = models.FloatField(editable=False, default=0)
    rate_count = models.PositiveBigIntegerField(default=0, editable=False)

    def add_rate(self, num, user):
        with transaction.atomic():
            article = Article.objects.select_for_update().filter(pk=self.pk).get()
            try:
                with transaction.atomic():
                    user_rate = UserRate.objects.select_for_update().filter(user=user, article=article).get()
                    article.rate = (article.rate * article.rate_count - user_rate.rate + num) / article.rate_count
                    user_rate.rate = num
                    article.save()
                    user_rate.save()
            except UserRate.DoesNotExist:
                UserRate.objects.create(user=user, article=article, rate=num)
                article.rate = (article.rate * article.rate_count + num) / (article.rate_count+1)
                article.rate_count += 1
                article.save()
            return article


class UserRate(models.Model):
    article = models.ForeignKey(Article, related_name='rates', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.SET_NULL, null=True)
    rate = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('article', 'user')

