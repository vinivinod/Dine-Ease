# Generated by Django 4.2.4 on 2023-10-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='status',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
