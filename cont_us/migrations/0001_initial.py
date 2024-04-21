# Generated by Django 5.0.2 on 2024-04-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999)),
                ('thumbnail', models.ImageField(upload_to='Gallary')),
                ('index', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=999)),
                ('msG', models.TextField(max_length=9999, verbose_name='message')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999)),
                ('thumbnail', models.ImageField(upload_to='social_media')),
                ('url', models.CharField(max_length=999)),
            ],
            options={
                'verbose_name': 'social media',
                'verbose_name_plural': 'social medias',
            },
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999)),
                ('designation', models.CharField(max_length=999)),
                ('phone', models.CharField(blank=True, max_length=999, null=True)),
                ('Email', models.CharField(blank=True, max_length=999, null=True)),
                ('thumbnail', models.ImageField(upload_to='licenses')),
                ('Enable', models.BooleanField(default=True)),
                ('index', models.BooleanField()),
                ('position', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'team member',
            },
        ),
    ]
