from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.views import status
from django.contrib.auth import get_user_model

from .models import Article

User = get_user_model()


class ArticleViewSetTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(username='user1')
        cls.user2 = User.objects.create(username='user2')
        cls.article = Article.objects.create(title='title test 1', content='content test 1')

    def test_list(self):
        url = reverse('article-list')
        self.client.force_login(self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('user_rate' in response.json()[0])
        self.assertEqual(response.json()[0]['user_rate'], None)

    def test_rate(self):
        url = reverse('article-rate', kwargs={'pk': self.article.pk})
        self.client.force_login(self.user1)
        response = self.client.post(url, data={'rate': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.first().rate, 1)
        self.assertEqual(Article.objects.first().rate_count, 1)

        self.client.force_login(self.user2)
        response = self.client.post(url, data={'rate': 4})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.first().rate, 2.5)
        self.assertEqual(Article.objects.first().rate_count, 2)

        self.client.force_login(self.user1)
        response = self.client.post(url, data={'rate': 5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.first().rate, 4.5)
        self.assertEqual(Article.objects.first().rate_count, 2)
