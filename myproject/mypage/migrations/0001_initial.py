# Generated by Django 3.2.3 on 2021-07-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(default='', max_length=45)),
                ('timetable', models.CharField(default='', max_length=200)),
                ('keyword', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=45)),
            ],
        ),
    ]
