# Generated by Django 4.0.2 on 2022-03-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('rent', models.IntegerField()),
                ('move_in', models.CharField(max_length=250)),
                ('move_out', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=40000)),
            ],
        ),
    ]