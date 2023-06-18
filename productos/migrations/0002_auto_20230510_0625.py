# Generated by Django 3.2.18 on 2023-05-10 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('disponibilidad', models.CharField(choices=[('Disponible', 'D'), ('No disponible', 'ND')], max_length=20, verbose_name='Disponibilidad')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.tipoproducto', verbose_name='Nombre'),
        ),
    ]
