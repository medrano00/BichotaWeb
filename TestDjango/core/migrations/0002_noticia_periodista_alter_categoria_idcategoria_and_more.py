# Generated by Django 4.0.4 on 2022-06-09 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('cuerpo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellidos', models.TextField()),
                ('email', models.EmailField(max_length=250)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.noticia')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]
