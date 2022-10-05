# Generated by Django 4.1.2 on 2022-10-05 14:32

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
            name='UrlShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_url', models.URLField(unique=True)),
                ('short_url', models.URLField(unique=True)),
                ('hash_url', models.CharField(max_length=255)),
                ('clicked', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
