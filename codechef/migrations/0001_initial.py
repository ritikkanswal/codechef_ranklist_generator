# Generated by Django 3.2.6 on 2021-09-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('highest_rating', models.IntegerField()),
                ('global_rank', models.IntegerField()),
                ('country_rank', models.IntegerField()),
            ],
        ),
    ]
