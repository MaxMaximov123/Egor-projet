# Generated by Django 4.2.6 on 2024-03-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название картины')),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Картина')),
                ('describition', models.CharField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название выставки')),
                ('describition', models.TextField(verbose_name='Описание')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
            },
        ),
    ]
