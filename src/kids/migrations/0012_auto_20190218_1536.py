# Generated by Django 2.0.9 on 2019-02-18 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0011_sponsorship_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kids_kid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='kid',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='kid_pics/%Y-%m-%d/', verbose_name='Kid picture'),
        ),
    ]