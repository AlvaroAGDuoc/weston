# Generated by Django 4.0.5 on 2022-07-01 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Correo electronico')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre completo')),
                ('telefono', models.IntegerField(null=True, verbose_name='Telefono del usuario')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la categoria')),
                ('nombre', models.CharField(max_length=15, null=True, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la compra')),
                ('completada', models.BooleanField(default=False, null=True)),
                ('transaccion_id', models.CharField(max_length=200, null=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la comuna')),
                ('nombre', models.CharField(max_length=30, null=True, verbose_name='Nombre de la comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la region')),
                ('nombre', models.CharField(max_length=30, null=True, verbose_name='Nombre de la region')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('nombre', models.CharField(max_length=40, null=True, verbose_name='Nombre del producto')),
                ('precio', models.IntegerField(null=True, verbose_name='Precio del producto')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('stock', models.IntegerField(null=True, verbose_name='Stock del producto')),
                ('descripcionCorta', models.TextField(max_length=200, null=True, verbose_name='Descripcion corta del producto')),
                ('descripcion', models.TextField(max_length=200, null=True, verbose_name='Descripcion del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de rol')),
                ('descripcion', models.CharField(max_length=40, null=True, verbose_name='Nombre de la direccion')),
                ('compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.compra')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad')),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.compra')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region'),
        ),
    ]
