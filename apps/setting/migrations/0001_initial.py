# Generated by Django 4.2 on 2023-04-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=244, verbose_name='Название сайта')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logo_site')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('locate', models.CharField(max_length=255, verbose_name='Адрес')),
                ('locate_url', models.URLField(verbose_name='Ссылка для адресса')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('whatsapp', models.URLField(verbose_name='Whatsapp')),
                ('youtube', models.URLField(verbose_name='Youtube')),
                ('app', models.URLField(verbose_name='Ссылка для приложения')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
