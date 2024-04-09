# Generated by Django 4.2.4 on 2024-02-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='menu_items',
        ),
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
        migrations.AddField(
            model_name='review',
            name='billing_information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='home.billinginformation'),
        ),
    ]
