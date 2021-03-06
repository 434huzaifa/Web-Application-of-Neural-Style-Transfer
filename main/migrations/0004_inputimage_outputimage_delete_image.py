# Generated by Django 4.0.2 on 2022-04-15 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_image_result_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_image', models.ImageField(upload_to='files/style')),
                ('source_image', models.ImageField(upload_to='files/source')),
            ],
        ),
        migrations.CreateModel(
            name='OutputImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_image', models.ImageField(blank=True, null=True, upload_to='files/result')),
                ('input', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.inputimage')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
