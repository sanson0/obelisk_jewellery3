# Generated by Django 3.2.9 on 2021-12-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='refunds',
            options={'verbose_name_plural': 'Refunds'},
        ),
        migrations.AlterModelOptions(
            name='tandcs',
            options={'verbose_name_plural': 'Tandcs'},
        ),
    ]