# Generated by Django 3.1.7 on 2021-03-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rdv_center_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='citoyen',
            name='RAMID',
            field=models.CharField(default=0, max_length=10, unique=True),
        ),
    ]
