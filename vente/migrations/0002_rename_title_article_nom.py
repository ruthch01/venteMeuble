# Generated by Django 4.2.3 on 2023-07-24 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='nom',
        ),
    ]