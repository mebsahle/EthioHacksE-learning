# Generated by Django 2.2.9 on 2020-10-10 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.CharField(max_length=300)),
                ('category_created_at', models.DateTimeField(auto_now=True)),
                ('category_short_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.CharField(max_length=300)),
                ('course_created_at', models.DateTimeField(auto_now=True)),
                ('course_code', models.CharField(max_length=200)),
                ('category_name', models.ForeignKey(default='Categori', on_delete=django.db.models.deletion.CASCADE, to='book.Category')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_file', models.FileField(default='null', upload_to='books/uploads/')),
                ('course_code', models.ForeignKey(default='Cours', on_delete=django.db.models.deletion.CASCADE, to='book.Category')),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
    ]
