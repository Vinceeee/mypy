# Generated by Django 2.1.7 on 2019-02-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='c_id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='price',
            name='p_id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
