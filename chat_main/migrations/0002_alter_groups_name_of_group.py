# Generated by Django 3.2.2 on 2021-06-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='name_of_group',
            field=models.CharField(max_length=50),
        ),
    ]
