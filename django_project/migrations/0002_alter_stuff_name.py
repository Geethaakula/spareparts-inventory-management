# Generated by Django 3.2.13 on 2022-10-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]