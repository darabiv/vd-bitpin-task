# Generated by Django 4.1.3 on 2023-05-11 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('rate', models.FloatField(default=0, editable=False)),
                ('rate_count', models.PositiveBigIntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='articles.article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('article', 'user')},
            },
        ),
    ]
