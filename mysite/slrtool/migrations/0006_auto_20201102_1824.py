# Generated by Django 2.0.6 on 2020-11-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slrtool', '0005_auto_20201102_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='document/2020-11-02_18-24-55/'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pages',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
