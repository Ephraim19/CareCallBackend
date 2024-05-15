# Generated by Django 4.2.13 on 2024-05-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('memberName', models.CharField(max_length=50)),
                ('memberDOB', models.DateField(blank=True)),
                ('memberGender', models.CharField(blank=True, max_length=5)),
                ('memberFacility', models.CharField(blank=True, max_length=50)),
                ('memberPhone', models.IntegerField()),
                ('memerEmail', models.EmailField(max_length=50)),
                ('memberPhoneTwo', models.IntegerField(blank=True)),
                ('memberOffice', models.CharField(blank=True, max_length=50)),
                ('memberHome', models.CharField(blank=True, max_length=50)),
                ('memberCounty', models.CharField(blank=True, max_length=15)),
                ('memberTown', models.CharField(blank=True, max_length=15)),
                ('memberDelivery', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]