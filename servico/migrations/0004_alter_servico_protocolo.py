# Generated by Django 4.2.5 on 2023-09-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0003_rename_tituto_servico_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]
