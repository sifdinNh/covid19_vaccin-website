# Generated by Django 3.1.7 on 2021-03-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210309_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdv',
            name='center_id',
            field=models.IntegerField(default=0),
        ),
    ]
