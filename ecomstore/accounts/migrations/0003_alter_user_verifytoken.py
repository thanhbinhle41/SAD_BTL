# Generated by Django 4.1.7 on 2023-05-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_verifytoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verifyToken',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
