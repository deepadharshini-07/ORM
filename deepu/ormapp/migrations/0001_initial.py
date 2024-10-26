# Generated by Django 5.1.2 on 2024-10-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('Name', models.CharField(max_length=15)),
                ('accountno', models.IntegerField(primary_key='accountno', serialize=False)),
                ('loan_amount', models.IntegerField()),
                ('interest', models.FloatField()),
            ],
        ),
    ]