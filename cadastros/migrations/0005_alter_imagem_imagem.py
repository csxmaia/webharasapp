# Generated by Django 4.0.4 on 2022-09-23 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_rename_image_imagem_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
