# Generated by Django 3.1.2 on 2020-10-29 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
