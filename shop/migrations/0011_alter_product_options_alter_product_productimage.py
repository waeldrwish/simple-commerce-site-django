# Generated by Django 4.2.4 on 2023-08-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['productName']},
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(upload_to='photo/%y/%m/%d'),
        ),
    ]
