# Generated by Django 4.2.5 on 2023-09-14 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_carro'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TO', 'Troca de óleo'), ('VA', 'Troca de válvula'), ('BA', 'Balanceamento')], max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituto', models.CharField(max_length=50)),
                ('data_init', models.DateField(null=True)),
                ('data_end', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=40, null=True)),
                ('categorias_manutencao', models.ManyToManyField(to='servico.categoriamanutencao')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]
