# Generated by Django 3.2.5 on 2021-09-04 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_rename_userprofile_useraccount'),
        ('reviews', '0002_alter_productreview_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.useraccount'),
        ),
    ]
