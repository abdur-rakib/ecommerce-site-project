# Generated by Django 2.2.5 on 2019-09-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190920_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avater',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]