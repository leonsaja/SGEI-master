# Generated by Django 3.2.6 on 2021-08-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(max_length=10, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Usuário'),
        ),
    ]