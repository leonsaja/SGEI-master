# Generated by Django 3.2.6 on 2021-08-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_user_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='user_foto', verbose_name='Foto'),
        ),
    ]