# Generated by Django 2.2.9 on 2020-10-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(help_text='eg. PHYS0000', max_length=200),
        ),
    ]