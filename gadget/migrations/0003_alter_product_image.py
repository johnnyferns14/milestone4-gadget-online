# Generated by Django 3.2.5 on 2021-08-14 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0002_auto_20210803_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
