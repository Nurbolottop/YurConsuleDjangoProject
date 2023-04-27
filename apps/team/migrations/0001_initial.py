# Generated by Django 4.2 on 2023-04-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нашей команде',
                'verbose_name_plural': 'О нашей команде',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ФИО')),
                ('work', models.CharField(max_length=255, verbose_name='Профессия')),
                ('descriptions', models.TextField(verbose_name='Девиз')),
                ('image', models.ImageField(upload_to='team_image')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
