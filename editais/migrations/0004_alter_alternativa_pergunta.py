# Generated by Django 3.2.6 on 2021-09-26 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editais', '0003_alter_alternativa_pergunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativa',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busca_alternativa', to='editais.pergunta'),
        ),
    ]
