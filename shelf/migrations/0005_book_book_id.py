# Generated by Django 3.2 on 2021-07-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20210709_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
