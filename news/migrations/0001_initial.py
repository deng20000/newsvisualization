# Generated by Django 4.1 on 2023-11-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=100, null=True)),
                ('source_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('url_to_image', models.URLField(null=True)),
                ('published_at', models.DateTimeField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'News Article',
                'verbose_name_plural': 'News Articles',
                'ordering': ['-published_at'],
            },
        ),
    ]
