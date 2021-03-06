# Generated by Django 2.0.6 on 2020-11-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slrtool', '0002_auto_20201028_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_type', models.CharField(max_length=30)),
                ('id_on_web', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('booktitle', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('number', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('abstract', models.CharField(max_length=2000)),
                ('keywords', models.CharField(max_length=1000)),
                ('doi', models.CharField(max_length=100)),
                ('issn', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('pdf_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='document/2020-11-02_18-06-26/'),
        ),
    ]
