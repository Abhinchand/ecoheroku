# Generated by Django 3.1.4 on 2021-01-29 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20210129_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paytrack',
            options={'ordering': ['-timestamp', '-update']},
        ),
        migrations.AddField(
            model_name='paytrack',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paytrack',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]