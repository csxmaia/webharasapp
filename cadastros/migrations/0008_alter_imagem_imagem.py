# Generated by Django 4.0.4 on 2022-09-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_cavalo_criado_em_cavalo_criado_por_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='imagens'),
        ),
    ]
