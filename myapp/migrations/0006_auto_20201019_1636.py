# Generated by Django 2.2.5 on 2020-10-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201019_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y'),
        ),
    ]
