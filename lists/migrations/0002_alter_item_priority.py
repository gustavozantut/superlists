# Generated by Django 4.0.4 on 2022-05-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.CharField(choices=[('sem prioridade', 'sem prioridade'), ('alta', 'alta'), ('média', 'média'), ('baixa', 'baixa')], default='sem prioridade', max_length=20),
        ),
    ]
