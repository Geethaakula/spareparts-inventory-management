# Generated by Django 3.2.13 on 2023-09-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0003_alter_stuff_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='id',
        ),
        migrations.AlterField(
            model_name='stuff',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
