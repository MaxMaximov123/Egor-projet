# Generated by Django 4.2.6 on 2024-03-06 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_art_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='exh_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.titles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='titles',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
