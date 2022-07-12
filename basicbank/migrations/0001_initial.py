# Generated by Django 4.0.6 on 2022-07-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('accbal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200, null=True)),
                ('reciever', models.CharField(max_length=200, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('date_tran', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
