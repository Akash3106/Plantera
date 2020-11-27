# Generated by Django 3.0.8 on 2020-09-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='relprod',
            fields=[
                ('rel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('rate', models.IntegerField(default=0)),
                ('img', models.ImageField(default='', upload_to='shop/related')),
            ],
        ),
    ]
