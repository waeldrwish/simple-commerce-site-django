# Generated by Django 4.2.4 on 2023-08-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(upload_to='template/photos/%y/%m/%d'),
        ),
    ]
