# Generated by Django 3.2.5 on 2021-09-18 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('nutriscore', models.CharField(max_length=1)),
                ('image_product', models.CharField(max_length=200)),
                ('fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('salt_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product_favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
