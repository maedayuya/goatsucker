# Generated by Django 3.0.5 on 2022-02-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20220205_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
