# Generated by Django 2.0.9 on 2019-03-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0012_auto_20190218_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]