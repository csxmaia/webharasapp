# Generated by Django 4.0.4 on 2022-11-21 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0013_cavalo_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, null=True)),
                ('cpf', models.CharField(max_length=14, null=True)),
                ('telefone', models.CharField(max_length=16, null=True)),
                ('whatsapp', models.CharField(max_length=16, null=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cidade', verbose_name='Cidade')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
