# Generated by Django 3.2.7 on 2021-11-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('typeofitem', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('datelost', models.DateField()),
                ('contactinfo', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
