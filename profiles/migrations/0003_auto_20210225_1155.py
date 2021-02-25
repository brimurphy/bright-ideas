# Generated by Django 3.1.6 on 2021-02-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210222_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
