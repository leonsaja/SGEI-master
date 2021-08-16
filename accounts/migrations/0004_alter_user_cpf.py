# Generated by Django 3.2.6 on 2021-08-14 23:09

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=11, verbose_name='CPF'),
        ),
    ]
