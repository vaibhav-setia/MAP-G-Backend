# Generated by Django 2.2 on 2020-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_auto_20200319_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]