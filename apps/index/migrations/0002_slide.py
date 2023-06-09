# Generated by Django 4.2 on 2023-04-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image', verbose_name='Фотография для слайда')),
                ('name', models.CharField(max_length=255, verbose_name='Название для слайда')),
                ('descriptions', models.TextField(verbose_name='Описание для слайда')),
            ],
        ),
    ]
