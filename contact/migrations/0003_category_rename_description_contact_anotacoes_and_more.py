# Generated by Django 5.0.2 on 2024-02-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_picture_contact_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='anotacoes',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='sobrenome',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='telefone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='picture',
        ),
        migrations.AddField(
            model_name='contact',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
