# Generated by Django 4.2 on 2023-04-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка Instagram для показа'),
        ),
    ]