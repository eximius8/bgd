# Generated by Django 3.0.3 on 2020-02-28 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeftMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SitePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTitle', models.CharField(max_length=40)),
                ('postName', models.TextField()),
                ('postText', models.TextField()),
                ('postUrl', models.CharField(max_length=30)),
                ('LastUpdated', models.DateField()),
                ('leftMenuName', models.CharField(max_length=30)),
                ('leftMenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.LeftMenu')),
            ],
        ),
    ]
