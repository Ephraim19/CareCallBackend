# Generated by Django 4.2.13 on 2024-05-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0005_alter_dependant_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dependant',
            options={},
        ),
        migrations.RemoveField(
            model_name='dependant',
            name='depandantName',
        ),
        migrations.AddField(
            model_name='dependant',
            name='dependantNames',
            field=models.CharField(default='eph', max_length=50),
            preserve_default=False,
        ),
    ]