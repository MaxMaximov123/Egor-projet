# Generated by Django 4.2.6 on 2024-03-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_files/', verbose_name='Картина'),
        ),
    ]
