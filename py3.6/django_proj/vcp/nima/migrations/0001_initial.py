# Generated by Django 2.1.4 on 2018-12-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=255)),
            ],
        ),
    ]