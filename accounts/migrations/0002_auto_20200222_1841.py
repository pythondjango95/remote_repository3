# Generated by Django 2.1 on 2020-02-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
