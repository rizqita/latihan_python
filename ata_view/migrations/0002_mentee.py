# Generated by Django 2.2.3 on 2019-07-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ata_view', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('gambar', models.CharField(max_length=255)),
                ('quote', models.TextField()),
            ],
        ),
    ]
