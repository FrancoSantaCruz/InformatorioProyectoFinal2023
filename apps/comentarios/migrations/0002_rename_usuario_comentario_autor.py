# Generated by Django 4.2.7 on 2023-12-14 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuario',
            new_name='autor',
        ),
    ]
