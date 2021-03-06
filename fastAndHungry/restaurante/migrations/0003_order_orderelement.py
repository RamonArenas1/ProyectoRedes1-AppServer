# Generated by Django 3.0.3 on 2020-06-09 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20200605_1941'),
        ('restaurante', '0002_auto_20200605_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('CT', 'CARRITO'), ('PD', 'PENDIENTE'), ('LT', 'LISTA'), ('EC', 'EN CAMINO'), ('ET', 'ENTREGADO')], max_length=2)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Element')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Order')),
            ],
        ),
    ]
