# Generated by Django 5.1.4 on 2024-12-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.AutoField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
