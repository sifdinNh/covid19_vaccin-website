# Generated by Django 3.1.7 on 2021-03-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210313_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='citoyen',
            name='is_RDV',
            field=models.BooleanField(default=False),
        ),
    ]