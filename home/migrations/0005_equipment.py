# Generated by Django 2.2.7 on 2020-03-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200307_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufact', models.CharField(max_length=50)),
                ('leftMenuName', models.CharField(max_length=30)),
                ('urlimage', models.CharField(max_length=250)),
                ('urlmenu', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('lastUpdated', models.DateField()),
            ],
        ),
    ]
