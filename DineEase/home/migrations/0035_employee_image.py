# Generated by Django 4.2.4 on 2023-09-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_employee_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_profile/'),
        ),
    ]