# Generated by Django 5.0.2 on 2024-02-09 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contact_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='categoria',
            new_name='tipo_de_leito',
        ),
    ]