# Generated by Django 5.0 on 2023-12-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blogmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pages')),
                ('photo', models.ImageField(upload_to='pages')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
