# Generated by Django 5.0.2 on 2024-02-24 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_auteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
    ]