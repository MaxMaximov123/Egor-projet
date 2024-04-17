# Generated by Django 4.2.6 on 2024-03-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_art_exh_id_titles_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='exh_id',
        ),
        migrations.RemoveField(
            model_name='art',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='art',
            name='genre',
            field=models.CharField(max_length=50, null=True, verbose_name='Жанр'),
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
    ]