# Generated by Django 5.0 on 2023-12-19 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_productmodel_product_kit_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_kit_Model',
            new_name='kit_Model',
        ),
        migrations.AlterModelOptions(
            name='kit_model',
            options={'verbose_name': 'kit', 'verbose_name_plural': 'kits'},
        ),
    ]
