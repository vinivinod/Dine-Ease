# Generated by Django 4.2.4 on 2024-03-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_medicalleave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalleave',
            name='reason',
            field=models.TextField(null=True),
        ),
    ]
