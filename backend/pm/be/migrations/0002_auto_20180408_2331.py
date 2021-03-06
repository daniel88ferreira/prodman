# Generated by Django 2.0.4 on 2018-04-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='raw', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='final',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=80, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
