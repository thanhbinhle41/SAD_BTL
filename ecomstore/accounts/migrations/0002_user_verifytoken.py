# Generated by Django 4.1.7 on 2023-05-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verifyToken',
            field=models.CharField(default=None, max_length=200),
        ),
    ]