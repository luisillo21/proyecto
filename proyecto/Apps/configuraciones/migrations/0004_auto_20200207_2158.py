# Generated by Django 2.2.5 on 2020-02-08 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0003_auto_20200207_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='id_padre',
        ),
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]