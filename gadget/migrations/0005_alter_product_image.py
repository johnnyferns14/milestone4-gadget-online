# Generated by Django 3.2.5 on 2021-08-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
