# Generated by Django 2.2.9 on 2020-10-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_short_name',
            field=models.CharField(help_text='eg. PHY', max_length=200),
        ),
    ]
