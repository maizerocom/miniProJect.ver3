# Generated by Django 2.2.2 on 2020-03-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20200309_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]