# Generated by Django 2.1.7 on 2019-02-15 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=200)),
                ('c_description', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=200)),
                ('p_level', models.IntegerField(default=5)),
                ('p_pic', models.CharField(default='pic_default', max_length=255)),
                ('p_istaken', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('w_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('policy', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.Candidate')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.Price')),
            ],
        ),
    ]