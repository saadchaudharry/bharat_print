# Generated by Django 5.0.2 on 2024-04-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_service_icon_alter_top_content_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='top_content',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
