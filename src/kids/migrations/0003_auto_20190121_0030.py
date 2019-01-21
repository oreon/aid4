# Generated by Django 2.0.9 on 2019-01-21 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0002_auto_20190121_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kid',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='kid',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kid',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
