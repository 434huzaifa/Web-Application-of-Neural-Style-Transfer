# Generated by Django 4.0.2 on 2022-04-15 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_inputimage_outputimage_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outputimage',
            name='input',
        ),
    ]
